import django_tables2 as tables
from .models import CustomURL, QRCodeSetting
from netbox.tables import NetBoxTable, columns
from django_tables2.utils import A
from django.utils.translation import gettext_lazy as _


class CustomURLListTable(NetBoxTable):

    pk = columns.ToggleColumn()
    
    assigned_object_type  = tables.Column( 
    )

    assigned_object = tables.Column(
        linkify=True,
        orderable=False
    )
    
    dest_url = tables.Column(

    )


    class Meta(NetBoxTable.Meta):
        model = CustomURL
        fields = ('pk', 'assigned_object', 'dest_url')


class QRCodeSettingListTable(NetBoxTable):

    name  = tables.Column( 
        linkify=True,
    )

    actions = columns.ActionsColumn(
        actions=('edit', ),
    )


    class Meta(NetBoxTable.Meta):
        model = QRCodeSetting
        fields = ('name',)

