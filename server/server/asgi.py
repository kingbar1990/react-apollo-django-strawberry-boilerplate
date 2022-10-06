import os

from django.core.asgi import get_asgi_application
from django.urls import path, re_path

from channels.routing import ProtocolTypeRouter, URLRouter
from strawberry.channels import GraphQLWSConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "berry.settings")
django_asgi_app = get_asgi_application()


from .schema import schema
from .token_auth import TokenAuthMiddleware

websocket_urlpatterns = [
    re_path(r"graphql", GraphQLWSConsumer.as_asgi(schema=schema)),
]

gql_ws_consumer = GraphQLWSConsumer.as_asgi(schema=schema)

application = ProtocolTypeRouter(
    {
        "websocket": TokenAuthMiddleware(
            URLRouter([path("subscriptions", gql_ws_consumer)]),
        ),
    }
)
