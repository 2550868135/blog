''' @File :consumer.py @Author:张宇 @Date :2020/9/30 18:08 @Desc : '''
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class MessageConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        if not self.scope['url_route']['kwargs']['username']:
            # 未登录的用户拒绝连接
            await self.close()
        else:
            await self.channel_layer.group_add(self.scope['url_route']['kwargs']['username'], self.channel_name)
            await self.accept()
    async def receive(self, text_data=None, bytes_data=None):
        # 将数据发送到前端
        if text_data['sender'] != self.scope['url_route']['kwargs']['username']:
            await self.send(text_data=json.dumps(text_data))

    async def disconnect(self, code):
        # 断开时离开组
        await self.channel_layer.group_discard(self.scope['url_route']['kwargs']['username'],self.channel_name)