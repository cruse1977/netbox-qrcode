from django.core.management.base import BaseCommand
from netbox_qrcode.models import QRCodeSetting
import json

class Command(BaseCommand):
    help = "Create or recreate the default settings"
    
    default_settings = {
        'with_text': True,
        'text_fields': ['name', 'serial'],
        'font': 'TahomaBold',
        'custom_text': None,
        'text_location': 'right',
        'qr_version': 1,
        'qr_error_correction': 0,
        'qr_box_size': 6,
        'qr_border': 4,
        'device': {
            'text_fields': ['name', 'serial']
        },
        'rack': {
            'text_fields': ['name']
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
        }        
    }

    def handle(self, *model_names, **options):
        settings = QRCodeSetting.objects.all()
        if settings.count() == 0:
            # create a config
            QRCodeSetting.objects.create(
                name = "default settings",
                config = self.default_settings)
        else:
            # should only ever be one here but this is safety
            for setting in settings:
                setting.config = self.default_settings
                setting.save(update_fields=["config"])
