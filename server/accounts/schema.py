import strawberry
from typing import List
from strawberry.types import Info
from .types import UserType, ErrorType, MeType


ME = strawberry.union("ME", (ErrorType, MeType))


def active_user(info: Info) -> ME:
    if info.context.request.user.is_authenticated:
        return MeType(user=info.context.request.user)
    else:
        return ErrorType(message='User is not authenticated')


@strawberry.type
class Query:
    users: List[UserType] = strawberry.django.field()
    me: List[UserType] = strawberry.django.field(resolver=active_user)
