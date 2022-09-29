from strawberry_django_jwt.shortcuts import (
    get_user_by_token
)
from graphql import GraphQLResolveInfo
from strawberry_django_jwt.middleware import BaseJSONWebTokenMiddleware


class AuthorizationMiddleware(BaseJSONWebTokenMiddleware):
    def resolve(self, _next, root, info: GraphQLResolveInfo, *args, **kwargs):
        headers = info.context.request.headers
        session_oauth = info.context.request.session.get('Authorization', None)

        if session_oauth:
            user = get_user_by_token(session_oauth)
            info.context.request.user = user

        if 'Authorization' in headers.keys() and len(headers['Authorization']):
            token = headers['Authorization'].split(' ')[1]
            user = get_user_by_token(token)
            info.context.request.user = user
        return _next(root, info, **kwargs)
