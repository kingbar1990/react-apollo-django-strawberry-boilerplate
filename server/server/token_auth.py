from channels.auth import AuthMiddlewareStack

from django.contrib.auth.models import AnonymousUser

from strawberry_django_jwt.shortcuts import get_user_by_token

import urllib.parse


class TokenAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        return TokenAuthMiddlewareInstance(scope, self)


class TokenAuthMiddlewareInstance:
    def __init__(self, scope, middleware):
        self.middleware = middleware
        self.scope = dict(scope)
        self.inner = self.middleware.inner

    def __call__(self, receive, send):
        decoded_qs = urllib.parse.parse_qs(self.scope["query_string"])
        print(decoded_qs, flush=True)
        if b"token" in decoded_qs:
            token = decoded_qs.get(b"token").pop().decode()
            print(token, flush=True)
            self.scope["user"] = get_user_by_token(token)
            print(get_user_by_token(token), flush=True)
        else:
            self.scope["user"] = AnonymousUser()
        return self.inner(self.scope, receive, send)


def TokenAuthMiddlewareStack(inner):
    TokenAuthMiddleware(AuthMiddlewareStack(inner))
