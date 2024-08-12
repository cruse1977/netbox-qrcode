from netbox.plugins import PluginConfig
from .version import __version__


class QRCodeConfig(PluginConfig):
    name = 'netbox_qrcode'
    verbose_name = 'qrcode'
    description = 'Generate QR codes for the objects'
    version = __version__
    author = 'Nikolay Yuzefovich'
    author_email = 'mgk.kolek@gmail.com'
    required_settings = []
    default_settings = {
        'title': '56mm x 32mm',
        'with_text': True,
        'with_qr': True,
        'text_fields': ['name', 'serial'],
        'font': 'TahomaBold',
        'font_size': '3mm',
        'custom_text': None,
        'text_location': 'right',

        # These parameters are used to create the QR code image file.
        'qr_version': 1, # The higher the value, the more boxes you get.
        'qr_error_correction': 0,
        'qr_box_size': 4, # The smaller the number of pixels, the blurrier the QR code will be if the label dimensions are too large, but the quicker the QR code will be ready.
        'qr_border': 0,

        # Parameters for the label (Horizontal)
        'label_qr_width': '32mm',
        'label_qr_height': '32mm',
        'label_qr_text_distance': '2mm',
        'label_width': '56mm',
        'label_height': '32mm',
        'label_edge_top': '0mm',
        'label_edge_left': '0mm',
        'label_edge_right': '0mm',
        'label_edge_bottom': '0mm',


        'device': {
            'text_fields': ['name', 'serial'],
            'text_template': '{{ obj.name }}<br>Device: {{ obj.id }}',
        },
        'device_2': {
            'title': 'My cusom Title 56mm x 32mm',

            'text_template': '<div style="display: inline-block; height: 5mm; width: 15mm"><img src="{{ logo }}" height="100%" width="100%"></div><br>{{ obj.name }}<br>Device: {{ obj.id|stringformat:"07d" }}',

        
            'font_size': '4mm',

            'label_qr_width': '20mm',
            'label_qr_height': '30mm',
            'label_qr_text_distance': '2mm',
            'label_width': '56mm',
            'label_height': '32mm',
            'label_edge_top': '0mm',
            'label_edge_left': '2mm',
            'label_edge_right': '2mm',
        },
        'device_3': {
            'title': 'My cusom Title 56mm x 32mm',

            'text_template': '<div style="display: inline-block; height: 5mm; width: 15mm"><img src="{{ logo }}" height="100%" width="100%"></div><br>{{ obj.name }}<br>Device: {{ obj.id|stringformat:"07d" }}',

            'font_size': '4mm',

            'label_qr_width': '15mm',
            'label_qr_height': '15mm',
            'label_qr_text_distance': '2mm',
            'label_width': '56mm',
            'label_height': '32mm',
            'label_edge_top': '0mm',
            'label_edge_left': '2mm',
            'label_edge_right': '2mm',
             'text_location': 'left',
        },

        'device_4': {
            'title': 'My cusom Title 56mm x 32mm',

            'text_template': '<div style="display: inline-block; height: 10mm; width: 30mm"><img src="{{ logo }}" height="100%" width="100%"></div><br>{{ obj.name }}<br>Device: {{ obj.id|stringformat:"07d" }}',

            'font_size': '4mm',

            'text_location': 'center',

            'label_qr_width': '20mm',
            'label_qr_height': '20mm',
            'label_qr_text_distance': '0mm',
            'label_width': '56mm',
            'label_height': '32mm',
            'label_edge_top': '0mm',
            'label_edge_left': '0mm',
            'label_edge_right': '0mm',

            'with_text': True,
            'with_qr': False,
        },

        'device_5': {
            'title': 'My cusom Title 56mm x 32mm',

            'text_template': '<div style="display: inline-block; height: 5mm; width: 15mm"><img src="{{ logo }}" height="100%" width="100%"></div><br>{{ obj.name }}<br>Device: {{ obj.id|stringformat:"07d" }}',

            'font_size': '4mm',

            'text_location': 'left',

            'label_qr_width': '20mm',
            'label_qr_height': '20mm',
            'label_qr_text_distance': '0mm',
            'label_width': '56mm',
            'label_height': '32mm',
            'label_edge_top': '0mm',
            'label_edge_left': '2mm',
            'label_edge_right': '0mm',

            'with_text': True,
            'with_qr': False,
        },

        'device_6': {
            'title': 'My cusom Title 56mm x 32mm',

            'text_template': '<div style="display: inline-block; height: 5mm; width: 15mm"><img src="{{ logo }}" height="100%" width="100%"></div><br>{{ obj.name }}<br>Device: {{ obj.id|stringformat:"07d" }}',

            'font_size': '4mm',

            'label_qr_width': '20mm',
            'label_qr_height': '20mm',
            'label_qr_text_distance': '0mm',
            'label_width': '56mm',
            'label_height': '32mm',
            'label_edge_top': '0mm',
            'label_edge_left': '0mm',
            'label_edge_right': '0mm',

            'with_text': False,
            'with_qr': True,
        },

        'device_7': {
            'title': 'My cusom Title 32mm x 56mm',

            'text_template': '<div style="display: inline-block; height: 5mm; width: 15mm"><img src="{{ logo }}" height="100%" width="100%"></div><br>{{ obj.name }}<br>Device: {{ obj.id|stringformat:"07d" }}',

            'font_size': '4mm',

            'label_qr_width': '20mm',
            'label_qr_height': '20mm',
            'label_qr_text_distance': '0mm',
            'label_width': '32mm',
            'label_height': '56mm',
            'label_edge_top': '2mm',
            'label_edge_left': '0mm',
            'label_edge_right': '0mm',
            'text_location': 'up',
            'label_edge_bottom': '2mm',
        },

        'device_8': {
            'title': 'My cusom Title 32mm x 56mm',

            'text_template': '<div style="display: inline-block; height: 5mm; width: 15mm"><img src="{{ logo }}" height="100%" width="100%"></div><br>{{ obj.name }}<br>Device: {{ obj.id|stringformat:"07d" }}',

            'font_size': '4mm',

            'label_qr_width': '20mm',
            'label_qr_height': '20mm',
            'label_qr_text_distance': '2mm',
            'label_width': '32mm',
            'label_height': '56mm',
            'label_edge_top': '2mm',
            'label_edge_left': '0mm',
            'label_edge_right': '0mm',
             'text_location': 'down',
        },

        'device_9': {
            'title': 'My cusom Title 25mm x 10mm',
            'text_template': '<div style="display: inline-block; height: 3mm; width: 9mm"><img src="{{ logo }}" height="100%" width="100%"></div><br>{{ obj.name }}<br>Device: {{ obj.id|stringformat:"07d" }}',

            'font_size': '1.2mm',

            'label_qr_width': '9mm',
            'label_qr_height': '9mm',
            'label_qr_text_distance': '0.5mm',
            'label_width': '25mm',
            'label_height': '10mm',
            'label_edge_top': '0mm',
            'label_edge_left': '1mm',
            'label_edge_right': '0mm',
        },
        'rack': {
            'text_fields': ['name'],
        },
        'cable': {
            'text_fields': [
                '_termination_a_device',
                'termination_a',
                '_termination_b_device',
                'termination_b',
                'a_terminations.device',
                'a_terminations',
                'b_terminations.device',
                'b_terminations'
                ]
        },
        'location': {
            'text_fields': ['name']
        },
        'powerfeed': {
            'text_fields': ['name'],
        },
        'powerpanel': {
            'text_fields': ['name']
        },    

        'logo': 'data:image/png;base64,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'

    }

config = QRCodeConfig # noqa E305
