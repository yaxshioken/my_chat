import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from pyasn1_modules.rfc2985 import dateOfBirth

from account.models import Account
from chat.models import Room, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room = self.scope["url_route"]["kwargs"]["room"]
        self.group = f'chat_{self.room}'
        await self.channel_layer.group_add(
            self.group, self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.channel_layer,
            self.group
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.group, {
                'type': 'chat',
                "message": data['message'],
                'username': data['username'],
                'room': data['room']
            }

        )
        await self.save_message_to_db(**data)

    async def chat(self, event):
        await self.send(text_data=json.dumps(
            {
                "username": event["username"],
                "message": event["message"],
                "room": event["room"]
            }
        ))

    @sync_to_async
    def save_message_to_db(self, username, room, message):
        if username:
            user = Account.objects.get(username=username)
        else:
            user, created = Account.objects.get_or_create(username="anonim")
            if created:
                user.set_password("12345")
                user.save()
        room = Room.objects.get(slug=room)
        Message.objects.create(user=user, room=room, body=message)
