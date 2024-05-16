
from netbox.views.generic import (
    ObjectListView, 
    ObjectView, 
    ObjectEditView, 
    ObjectDeleteView,
    BulkDeleteView
)

from dcim.tables import InterfaceTable
from dcim.models import Interface
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import CustomURL, QRCodeSetting
from .forms import CustomURLForm, QRCodeSettingForm
#ustomURLFilterForm
from .tables import CustomURLListTable, QRCodeSettingListTable
#from .filtersets import CustomURLFilterSet 

''' Views for: CustomURL '''
class CustomURLListView(PermissionRequiredMixin, ObjectListView):
    permission_required = (
        'qrcode.view'
    )
    queryset = CustomURL.objects.all()
    table = CustomURLListTable
    #filterset = CustomURLFilterSet
    #filterset_form = CustomURLFilterForm

class QRCodeSettingListView(PermissionRequiredMixin, ObjectListView):
    permission_required = (
        'qrcode.view'
    )
    queryset = QRCodeSetting.objects.all()
    table = QRCodeSettingListTable    

class CustomURLView(PermissionRequiredMixin, ObjectView):
    permission_required = (
        'qrcode.view'
    )
    queryset = CustomURL.objects.all()\

class QRCodeSettingView(PermissionRequiredMixin, ObjectView):
    permission_required = (
        'qrcode.view'
    )
    queryset = QRCodeSetting.objects.all()

class CustomURLEditView(PermissionRequiredMixin, ObjectEditView):
    permission_required = (
        'qrcode.edit'
    )

    queryset = CustomURL.objects.all()
    form = CustomURLForm

class QRCodeSettingEditView(PermissionRequiredMixin, ObjectEditView):
    permission_required = (
        'qrcode.edit'
    )

    queryset = QRCodeSetting.objects.all()
    form = QRCodeSettingForm

    
class CustomURLDeleteView(PermissionRequiredMixin, ObjectDeleteView):
    permission_required = (
        'qrcode.delete'
    )
    queryset = CustomURL.objects.all()

class CustomURLBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    permission_required = (
        'qrcode.delete'
    )
    queryset = CustomURL.objects.all()
    table = CustomURLListTable