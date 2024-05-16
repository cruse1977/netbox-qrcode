from django.urls import path

from netbox.api.routers import NetBoxRouter
from . import views

app_name = "netbox_qrcode"

router = NetBoxRouter()
router.register('customurls', views.CustomURLViewSet)


urlpatterns = router.urls

