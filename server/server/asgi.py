import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import re_path
from strawberry.channels import GraphQLWSConsumer
from .token_auth import TokenAuthMiddleware


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings.dev")
django_asgi_app = get_asgi_application()

# Import your Strawberry schema after creating the django ASGI application
# This ensures django.setup() has been called before any ORM models are imported
# for the schema.

from .schema import schema

websocket_urlpatterns = [
    re_path(r"subscription", GraphQLWSConsumer.as_asgi(schema=schema)),
]

application = ProtocolTypeRouter(
    {
        "websocket": TokenAuthMiddleware(URLRouter(websocket_urlpatterns)),
    }
)
