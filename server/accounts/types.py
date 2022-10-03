from datetime import datetime

import strawberry

from . import models


@strawberry.django.type(models.User)
class UserType:
    id: int
    email: str
    full_name: str
    date_joined: datetime
    is_active: bool
    is_staff: bool
    is_verified: bool

    @strawberry.field
    def avatar(self) -> str:
        return self.avatar.file if self.avatar else ""


@strawberry.type
class LoginSuccessType:
    user: UserType
    token: str


@strawberry.type
class RegisterSuccessType:
    user: UserType
    token: str


@strawberry.type
class VerifyForgotPasswordSuccessType:
    token: str


@strawberry.type
class MeType:
    user: UserType


@strawberry.type
class ErrorType:
    message: str


@strawberry.type
class SuccessType:
    message: str
