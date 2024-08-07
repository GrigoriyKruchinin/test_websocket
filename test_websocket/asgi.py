import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from core.consumers import CountConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_websocket.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/count/', CountConsumer.as_asgi()),
        ])
    ),
})
