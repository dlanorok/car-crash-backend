import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ModelUpdateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.session_id = self.scope["url_route"]["kwargs"]["session_id"]
        self.crash_group_name = f"crash_{self.session_id}"

        await self.channel_layer.group_add(self.crash_group_name, self.channel_name)
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        await self.channel_layer.group_send(self.crash_group_name, {
            'type': 'group_message',
            'message': text_data
        })

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.crash_group_name, self.channel_name)

    async def model_update(self, event):
        await self.send(text_data=json.dumps(event))

    async def model_create(self, event):
        await self.send(text_data=json.dumps(event))

    async def group_message(self, event):
        message = event['message']
        await self.send(text_data=message)



