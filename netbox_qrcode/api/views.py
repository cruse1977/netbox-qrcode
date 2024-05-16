from rest_framework.routers import APIRootView
from rest_framework.views import APIView
from netbox.api.viewsets import NetBoxModelViewSet
from .serializers import *
from ..models import *


class CustomURLViewSet(NetBoxModelViewSet):
    queryset = CustomURL.objects.all()
    serializer_class = CustomURLSerializer
#    filterset_class = filtersets.IPAddressFilterSet