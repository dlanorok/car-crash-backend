import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ModelUpdateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.session_id = self.scope["url_route"]["kwargs"]["session_id"]
        self.crash_group_name = f"crash_{self.session_id}"

        await self.channel_layer.group_add(self.crash_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.crash_group_name, self.channel_name)

    async def model_update(self, event):
        await self.send(text_data=json.dumps(event))

    async def model_create(self, event):
        await self.send(text_data=json.dumps(event))



