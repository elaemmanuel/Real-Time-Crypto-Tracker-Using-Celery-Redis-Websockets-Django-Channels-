
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CryptoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("crypto_updates", self.channel_name)
        await self.accept()
        

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("crypto_updates", self.channel_name)

    async def crypto_price_update(self, event):
        """Handles messages broadcasted to the group."""
        await self.send(text_data=json.dumps(event['message']))