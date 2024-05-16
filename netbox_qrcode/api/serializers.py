from django.contrib.contenttypes.models import ContentType
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from netbox.api.fields import ContentTypeField
from ..models import *
from ..constants import CUSTOMURL_ASSIGNMENT_MODELS
from utilities.api import get_serializer_for_model
from netbox.api.serializers import NetBoxModelSerializer

class CustomURLSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_qrcode-api:customurl-detail')

    assigned_object_type = ContentTypeField(
        queryset=ContentType.objects.filter(CUSTOMURL_ASSIGNMENT_MODELS),
        required=False,
        allow_null=True
    )
    assigned_object = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomURL
        fields = [
            'id', 'url', 'dest_url', 'display', 'assigned_object_type',
            'assigned_object_id', 'assigned_object', 'created', 'last_updated',
        ]
        brief_fields = ('id', 'url', 'dest_url', 'display')

    @extend_schema_field(serializers.JSONField(allow_null=True))
    def get_assigned_object(self, obj):
        if obj.assigned_object is None:
            return None
        serializer = get_serializer_for_model(obj.assigned_object)
        context = {'request': self.context['request']}
        return serializer(obj.assigned_object, nested=True, context=context).data
    