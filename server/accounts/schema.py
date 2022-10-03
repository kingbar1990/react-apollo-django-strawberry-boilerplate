from typing import List

import strawberry

from .resolvers import active_user, all_users
from .resolvers import find_user as finduser
from .types import UserType


@strawberry.type
class Query:
    users: List[UserType] = strawberry.django.field(resolver=all_users)
    me: List[UserType] = strawberry.django.field(resolver=active_user)
    find_user: List[UserType] = strawberry.django.field(resolver=finduser)
