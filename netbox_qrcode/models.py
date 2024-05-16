from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from netbox.models import NetBoxModel
from .constants import *
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType

class CustomURL(NetBoxModel):
    ''' class to override a url for a particular QR code '''
    dest_url = models.URLField(max_length=255)


    # borrowed from netbox ipaddress :)
    assigned_object_type = models.ForeignKey(
        to='contenttypes.ContentType',
        limit_choices_to=CUSTOMURL_ASSIGNMENT_MODELS,
        on_delete=models.CASCADE,
        related_name='+',
    )
    assigned_object_id = models.PositiveBigIntegerField(
    )
    assigned_object = GenericForeignKey(
        ct_field='assigned_object_type',
        fk_field='assigned_object_id'
    )

    class Meta:
        ordering = ('assigned_object_type','pk')  # Name may be non-unique
        indexes = (
            models.Index(fields=('assigned_object_type', 'assigned_object_id')),
        )
        unique_together = ('assigned_object_type', 'assigned_object_id')
        verbose_name = _('Custom URL')
        verbose_name_plural = _('Custom URLs')

    def get_absolute_url(self):
        return reverse('plugins:netbox_qrcode:customurl', args=[self.pk])    
    
    def __str__(self):
        return f"{self.pk} - {self.assigned_object_type}:{self.assigned_object}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
                 
    def clean(self):
        super().clean()

        customurl_count = CustomURL.objects.filter(
            assigned_object_type=self.assigned_object_type,
            assigned_object_id=self.assigned_object_id).count()
        if customurl_count != 0:
            raise ValidationError("More than 1 URL cannot be assigned to any individual object")

class QRCodeSetting(NetBoxModel):
    ''' move settings out of files '''

    name = models.CharField(
        max_length=200,
        default = "default settings"
    )
    config = models.JSONField(
        blank = True,
        null = True
    )

    def get_absolute_url(self):
        return reverse('plugins:netbox_qrcode:qrcodesetting', args=[self.pk])  
    def __str__(self):
        return f"{self.name}"