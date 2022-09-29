import strawberry
import strawberry_django_jwt.mutations as jwt_mutations
from strawberry_django_jwt.middleware import JSONWebTokenMiddleware

from accounts.schema import Query as AccountQuery
from accounts.mutations import (
    LoginMutation,
    RegisterMutation,
    SendForgotPasswordMutation,
    VerifyForgotPasswordMutation,
    SetAvatarMutation
)

# from .middleware import AuthorizationMiddleware


@strawberry.type
class Query(AccountQuery):
    pass


@strawberry.type
class Mutation(LoginMutation, RegisterMutation,
               SendForgotPasswordMutation, VerifyForgotPasswordMutation,
               SetAvatarMutation):
    token_auth = jwt_mutations.ObtainJSONWebToken.obtain
    verify_token = jwt_mutations.Verify.verify
    refresh_token = jwt_mutations.Refresh.refresh
    delete_token_cookie = jwt_mutations.DeleteJSONWebTokenCookie.delete_cookie


schema = strawberry.Schema(query=Query, mutation=Mutation,
                           extensions=[
                               JSONWebTokenMiddleware]
                           )
