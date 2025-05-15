import json
from channels.db import database_sync_to_aysnc
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Room, Messages

class ChatCustomer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat{self.room_name}'

        await self.get_or_create_room()
        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        await self.accept()

    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)
   
