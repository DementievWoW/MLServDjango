from django.urls import re_path

from MlServDjango.Device.DeviceConsumer import DeviceConsumer
from channels.routing import ProtocolTypeRouter
websocket_urlpatterns = [
    re_path("ws", DeviceConsumer.as_asgi())
]



# application = ProtocolTypeRouter({
#
# })