from django import re_path
from .consumers import ChatCustomer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?p<room_name>\w+)/$',ChatCustomer.as_asgi()),
]