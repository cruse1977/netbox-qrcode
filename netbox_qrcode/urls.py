from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import views, models

urlpatterns = (
    path('settings', views.QRCodeSettingListView.as_view(), name="qrcodesetting_list"),
    path('settings/<int:pk>',  views.QRCodeSettingView.as_view(), name="qrcodesetting"),
    path('settings/<int:pk>/edit',  views.QRCodeSettingEditView.as_view(), name="qrcodesetting_edit"),
    path('settings/add',  views.QRCodeSettingView.as_view(), name="qrcodesetting_add"),
    path('settings/<int:pk>/delete',  views.QRCodeSettingView.as_view(), name="qrcodesetting_delete"),
    path('settings/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='qrcodesetting_changelog', kwargs={
        'model': models.QRCodeSetting
    }),
    path('custom-url', views.CustomURLListView.as_view(), name = "customurl_list"),
    path('custom-url/add', views.CustomURLEditView.as_view(), name = "customurl_add"),
    path('custom-url/<int:pk>', views.CustomURLView.as_view(), name = "customurl"),
    path('custom-url/<int:pk>/edit', views.CustomURLEditView.as_view(), name = "customurl_edit"),
    path('custom-url/<int:pk>/delete', views.CustomURLDeleteView.as_view(), name = "customurl_delete"),  
    path('custom-url/delete', views.CustomURLBulkDeleteView.as_view(), name="customurl_bulk_delete"),  
    path('custom-url/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='customurl_changelog', kwargs={
        'model': models.CustomURL
    }),
)