import urllib.parse
from typing import Optional

from channels.auth import AuthMiddlewareStack
from channels.db import database_sync_to_async

from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ObjectDoesNotExist

from strawberry_django_jwt import utils

from accounts.models import User


@database_sync_to_async
def get_user(email: str) -> Optional[User]:
    """
    Get authenticated user or return anonymous user.
    """
    try:
        user = User.objects.get(email=email)
        return user
    except ObjectDoesNotExist:
        return AnonymousUser()


class TokenAuthMiddleware:
    """
    Custom middleware (insecure) that takes user IDs from the query string.
    """

    def __init__(self, app):
        # Store the ASGI application we were passed
        self.app = app

    async def __call__(self, scope, receive, send):
        """
        Look up token in headers and check authenticated user).
        """
        email = ""
        decoded_qs = urllib.parse.parse_qs(scope["query_string"])
        headers = dict(scope["headers"])
        auth_headers_bytes = headers.get(b"authorization")
        if auth_headers_bytes:
            decode_auth = auth_headers_bytes.decode("utf-8")
            if decode_auth and "JWT" in decode_auth:
                token = decode_auth.split("JWT")[1].strip()
                email = utils.jwt_decode(token).email
        if not email:
            if b"token" in decoded_qs:
                token = decoded_qs.get(b"token").pop().decode()
                email = utils.jwt_decode(token).email
        if email:
            scope["user"] = await get_user(email)
        else:
            scope["user"] = AnonymousUser()
        return await self.app(scope, receive, send)


def TokenAuthMiddlewareStack(inner):
    return TokenAuthMiddleware(AuthMiddlewareStack(inner))
