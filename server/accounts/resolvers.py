from typing import List

import strawberry
from strawberry.types import Info

from . import models
from .types import ErrorType, MeType, UserType

ME = strawberry.union("ME", (ErrorType, MeType))


def active_user(info: Info) -> ME:
    if info.context.request.user.is_authenticated:
        return MeType(user=info.context.request.user)
    else:
        return ErrorType(message="User is not authenticated")


def find_user(email: str) -> UserType:
    return models.User.objects.get(email=email)


def all_users() -> List[UserType]:
    return models.User.objects.all()
