from packaging import version

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.template import engines

from netbox.plugins import PluginTemplateExtension

from .utilities import get_img_b64, get_qr

##################################
# Class for creating the plugin content
class QRCode(PluginTemplateExtension):

    ##################################
    # A user-defined design specification of the text is provided in ninja2 format.
    # --------------------------------
    # Parameter:
    #   config: From the Netbox configuration file
    #   obj: Data from the model (e.g. device, rack, etc.)
    #   qrCode: QR-Code Image 
    def get_text_template(config, obj, qrCode):

        django_engine = engines["django"]
        template = django_engine.from_string(config.get('text_template'))
        logo = config.get('logo')

        return template.render({'obj': obj, 
                                'logo': logo,
                                'qrCode': qrCode})
    
    ##################################
    # Retrieves all values from the object (e.g. device, rack, etc.)
    # depending on the configuration parameter that are to be displayed in list form and prepares them.
    # --------------------------------
    # Parameter:
    #   config: From the Netbox configuration file
    #   obj: Data from the model (e.g. device, rack, etc.)
    def get_text_fields(config, obj):

        text = []

        for text_field in config.get('text_fields', []):
            cfn = None
            if '.' in text_field:
                try:
                    text_field, cfn = text_field.split('.')
                except ValueError:
                    cfn = None
            if getattr(obj, text_field, None):
                if cfn:
                    try:
                        if getattr(obj, text_field).get(cfn):
                            text.append('{}'.format(getattr(obj, text_field).get(cfn)))
                    except AttributeError:
                        # fix for nb3.3: trying to get cable termination and device in same way as custom field
                        if type(getattr(obj, text_field)) is list:
                            first_element = next(iter(getattr(obj, text_field)), None)
                            if first_element and getattr(first_element, cfn, None):
                                text.append('{}'.format(getattr(first_element, cfn)))
                else:
                    text.append('{}'.format(getattr(obj, text_field)))

        # Append user-defined text to the end.
        custom_text = config.get('custom_text')

        if custom_text:
            text.append(custom_text)

        # Convert text list to string with line breaks.
        text = '<br>'.join(text)

    ##################################          
    # Creates a plug-in view for a label.
    # --------------------------------
    # Parameter:
    #   labelDesignNo: Which label design should be loaded.
    def Create_SubPluginContent(self, labelDesignNo):
        
        config = self.context['config'].copy() # Netbox

        obj = self.context['object'] # An object of the type Device, Rack etc.
        request = self.context['request'] # HTML Request Informations
        url = request.build_absolute_uri(obj.get_absolute_url()) # URL of the page

        # Create suffix to read the correct module configuration.
        confModulsufix = str() # None if the first standard label
        if(labelDesignNo >= 2):
            confModulsufix = '_' + str(labelDesignNo)

        # Collect the QR code plugin configuration for the specific object such as device, rack etc.
        # and overwrite the default configuration fields.
        obj_cfg = config.get(self.model.replace('dcim.', '') + confModulsufix) # get spezific object settings
        if obj_cfg is None: return '' # Abort if no config data. 
        config.update(obj_cfg) # Ovverride default confiv Values

        # Collect the configuration entries that begin with "qr_.
        # These are required to generate the QR code.
        qr_args = {}
        for k, v in config.items():
            if k.startswith('qr_'):
                qr_args[k.replace('qr_', '')] = v

        # Create a QR code
        qrCode = get_qr(url, **qr_args)
        qrCode = get_img_b64(qrCode)

        # Create the text for the label if required.
        text = str()
        if config.get('with_text'):
            if config.get('text_template'):
                text = QRCode.get_text_template(config, obj, qrCode) # Create text content based on the Ninja2 template from the user
            else:
                text = QRCode.get_text_fields(config, obj) # Use the list of variables from the Config.

        # Create plugin using template
        try:
            if version.parse(settings.VERSION).major >= 3:

                render = self.render(
                    'netbox_qrcode/qrcode3.html', extra_context={
                                                                    'title': config.get('title'),
                                                                    'labelDesignNo': labelDesignNo,
                                                                    'qrCode': qrCode, 
                                                                    'with_text': config.get('with_text'),
                                                                    'text': text,
                                                                    'text_location': config.get('text_location'),
                                                                    'font': config.get('font'),
                                                                    'font_size': config.get('font_size'),
                                                                    'with_qr': config.get('with_qr'),
                                                                    'label_qr_width': config.get('label_qr_width'),
                                                                    'label_qr_height': config.get('label_qr_height'),
                                                                    'label_qr_text_distance': config.get('label_qr_text_distance'),
                                                                    'label_width': config.get('label_width'),
                                                                    'label_height': config.get('label_height'), 
                                                                    'label_edge_top': config.get('label_edge_top'),
                                                                    'label_edge_left': config.get('label_edge_left'),
                                                                    'label_edge_right': config.get('label_edge_right'),
                                                                    'label_edge_bottom': config.get('label_edge_bottom')
                                                                    
                                                                }
                )
            
                return render
            else:
                # Versions 1 and 2 are no longer supported.
                return self.render(
                    'netbox_qrcode/qrcode.html', extra_context={'image': img}
                )
        except ObjectDoesNotExist:
            return ''

    ##################################
    # Create plugin content
    # - First, a plugin view is created for the first label.
    # - If there are further configuration entries for the object/model (e.g. device, rack etc.),
    #   further label views are also created as additional plugin views.
    def Create_PluginContent(self):

        # First Plugin Content
        pluginContent = QRCode.Create_SubPluginContent(self, 1) 

        # Check whether there is another configuration for the object, e.g. device, rack, etc.
        # Support up to 10 additional label configurations (objectName_2 to ..._10) per object (e.g. device, rack, etc.).

        config = self.context['config'] # Django configuration

        for i in range(2, 11):

            configName = self.model.replace('dcim.', '') + '_' + str(i)
            obj_cfg = config.get(configName) # Load configuration for additional label if possible.

            if(obj_cfg):
                pluginContent += QRCode.Create_SubPluginContent(self, i) # Add another plugin view
            else:
                break
        
        return pluginContent

##################################
# The following section serves to integrate the plugin into Netbox Core.
        
# Class for creating a QR code for the model: Device
class DeviceQRCode(QRCode):
    model = 'dcim.device' # Info for Netbox in which model the plugin should be integrated.

    def right_page(self):
        return self.Create_PluginContent()

# Class for creating a QR code for the model: Rack
class RackQRCode(QRCode):
    model = 'dcim.rack' # Info for Netbox in which model the plugin should be integrated.

    def right_page(self):
        return self.Create_PluginContent()

# Class for creating a QR code for the model: Cable
class CableQRCode(QRCode):
    model = 'dcim.cable' # Info for Netbox in which model the plugin should be integrated.

    def left_page(self):
        return self.Create_PluginContent()

# Class for creating a QR code for the model: Location
class LocationQRCode(QRCode):
    model = 'dcim.location' # Info for Netbox in which model the plugin should be integrated.

    def left_page(self):
        return self.Create_PluginContent()

# Class for creating a QR code for the model: Power Feed
class PowerFeedQRCode(QRCode):
    model = 'dcim.powerfeed' # Info for Netbox in which model the plugin should be integrated.

    def right_page(self):
        return self.Create_PluginContent()

# Class for creating a QR code for the model: Power Panel
class PowerPanelQRCode(QRCode):
    model = 'dcim.powerpanel' # Info for Netbox in which model the plugin should be integrated.

    def right_page(self):
        return self.Create_PluginContent()

# Connects Netbox Core with the plug-in classes
template_extensions = [DeviceQRCode, RackQRCode, CableQRCode, LocationQRCode, PowerFeedQRCode, PowerPanelQRCode]
