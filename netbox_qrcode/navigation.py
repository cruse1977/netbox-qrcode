"""
Define the plugin menu buttons & the plugin navigation bar enteries.
"""

from django.conf import settings
from netbox.plugins import PluginMenu, PluginMenuButton, PluginMenuItem

plugin_settings = settings.PLUGINS_CONFIG["netbox_qrcode"]

#
# Define plugin menu buttons
#
menu_buttons = (
    PluginMenuItem(
        link="plugins:netbox_qrcode:customurl_list",
        link_text="Custom URLs",
        permissions=["netbox_qrcode.view"],
        buttons=(
            PluginMenuButton(
                link="plugins:netbox_qrcode:customurl_add",
                title="Add",
                icon_class="mdi mdi-plus-thick",
                permissions=["netbox_qrcode.add"],
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_qrcode:qrcodesetting_list",
        link_text="Settings",
        permissions=["netbox_qrcode.view"],
    ),
)

if plugin_settings.get("top_level_menu"):
    menu = PluginMenu(
        label="NetBox QR-Code",
        groups=(("Items", menu_buttons),),
        icon_class="mdi mdi-lock",
    )
else:
    menu_items = menu_buttons