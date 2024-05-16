from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from .models import *
from dcim.models import *
from utilities.forms.fields import (
    CommentField, ContentTypeChoiceField, DynamicModelChoiceField, DynamicModelMultipleChoiceField, NumericArrayField,
    SlugField, JSONField
)
from utilities.forms.rendering import FieldSet, InlineFields, ObjectAttribute, TabbedGroups
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CustomURLForm(NetBoxModelForm):

    cable = DynamicModelChoiceField(
        queryset=Cable.objects.all(),
        required=False,
        selector=True,
        label=_('Cable'),
    )
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
        selector=True,
        label=_('Device'),
    )
    location = DynamicModelChoiceField(
        queryset=Location.objects.all(),
        required=False,
        selector=True,
        label=_('Location')
    )
    powerfeed = DynamicModelChoiceField(
        queryset=PowerFeed.objects.all(),
        required=False,
        selector=True,
        label=_('PowerFeed')
    )
    powerpanel = DynamicModelChoiceField(
        queryset=PowerPanel.objects.all(),
        required=False,
        selector=True,
        label=_('PowerPanel')
    )
    rack = DynamicModelChoiceField(
        queryset=Rack.objects.all(),
        required=False,
        selector=True,
        label=_('Rack')
    )
    fieldsets = (
        FieldSet('dest_url', name=_('Destination URL')),
        FieldSet(
            TabbedGroups(
                FieldSet('cable', name=_('Cable')),
                FieldSet('device', name=_('Device')),
                FieldSet('location', name=_('Location')),
                FieldSet('powerfeed', name=_('PowerFeed')),
                FieldSet('powerpanel', name=_('PowerPanel')),
                FieldSet('rack', name=_('Rack')),
            ),
        ),
    )

    class Meta:
        model = CustomURL
        fields = [
            'dest_url',
        ]

    def __init__(self, *args, **kwargs):

        # Initialize helper selectors
        instance = kwargs.get('instance')
        initial = kwargs.get('initial', {}).copy()
        if instance:
            if type(instance.assigned_object) is Cable:
                initial['cable'] = instance.assigned_object
            elif type(instance.assigned_object) is Device:
                initial['device'] = instance.assigned_object
            elif type(instance.assigned_object) is Location:
                initial['location'] = instance.assigned_object
            elif type(instance.assigned_object) is PowerFeed:
                initial['powerfeed'] = instance.assigned_object
            elif type(instance.assigned_object) is PowerPanel:
                initial['powerpanel'] = instance.assigned_object
            elif type(instance.assigned_object) is Rack:
                initial['rack'] = instance.assigned_object

        kwargs['initial'] = initial

        super().__init__(*args, **kwargs)

    def clean(self):
        super().clean()

        # Handle object assignment
        selected_objects = [
            field for field in ('cable', 'device', 'location', 'powerpanel', 'powerfeed', 'rack') if self.cleaned_data[field]
        ]
        if len(selected_objects) > 1:
            raise forms.ValidationError({
                selected_objects[1]: _("An CustomURL can only be assigned to a single object.")
            })
        elif selected_objects:
            assigned_object = self.cleaned_data[selected_objects[0]]
            self.instance.assigned_object = assigned_object
        else:
            self.instance.assigned_object = None
   
        
class QRCodeSettingForm(NetBoxModelForm):
    config = JSONField(required=False)

    class Meta:
        model = QRCodeSetting
        fields = "__all__"