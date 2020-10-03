''' @File :routing.py @Author:张宇 @Date :2020/9/30 17:59 @Desc : '''
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from app.consumer.consumer import MessageConsumer
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

# self.scope['type'] 获取协议类型
# channels routing是scope级别的,一个连接只能由一个consumer接收和处理
application = ProtocolTypeRouter({
    # 普通的HTTP协议可以不用写,框架会自动加载
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [path('ws/<str:username>/', MessageConsumer)]
            )
        )
    ),
})
