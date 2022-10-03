import strawberry

from typing import List

from .types import UserType
from .resolvers import all_users, active_user, find_user


@strawberry.type
class Query:
    users: List[UserType] = strawberry.django.field(resolver=all_users)
    me: List[UserType] = strawberry.django.field(resolver=active_user)
    find_user: List[UserType] = strawberry.django.field(resolver=find_user)
