import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer


class CountConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        for i in range(1, 11):
            await self.send(text_data=f"[{i}]")
            await asyncio.sleep(1)
        await self.close()
