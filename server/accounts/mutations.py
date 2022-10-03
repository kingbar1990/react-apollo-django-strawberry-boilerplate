import re

import strawberry
from django.core.exceptions import ObjectDoesNotExist
from strawberry.file_uploads import Upload
from strawberry.types import Info
from strawberry_django_jwt.shortcuts import get_token

from server.tasks import send_verification_code

from .models import LastVerificationCode, User
from .types import (
    ErrorType,
    LoginSuccessType,
    RegisterSuccessType,
    SuccessType,
    VerifyForgotPasswordSuccessType,
)

LoginResult = strawberry.union("LoginResult", (LoginSuccessType, ErrorType))
RegisterResult = strawberry.union("RegisterResult", (RegisterSuccessType, ErrorType))
ChangePasswordResult = strawberry.union(
    "ChangePasswordResult", (SuccessType, ErrorType)
)
ForgotPasswordResult = strawberry.union(
    "ForgotPasswordResult", (SuccessType, ErrorType)
)
VerifyForgotPasswordResult = strawberry.union(
    "VerifyForgotPasswordResult", (VerifyForgotPasswordSuccessType, ErrorType)
)
SetAvatarResult = strawberry.union("SetAvatarResult", (SuccessType, ErrorType))


@strawberry.type
class LoginMutation:
    @strawberry.mutation
    def login(self, email: str, password: str) -> LoginResult:

        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            return ErrorType(message="User with specified email does not exists.")

        if not user.check_password(password):
            return ErrorType(
                message="User with specified email"
                " does not exists or password incorrect."
            )

        token = get_token(user)
        # print(token, flush=True)
        # print(get_user_by_token(token), flush=True)
        return LoginSuccessType(user=user, token=token)


@strawberry.type
class RegisterMutation:
    @strawberry.mutation
    def register(
        self, email: str, password_1: str, password_2: str, name: str
    ) -> RegisterResult:
        if not re.match("[^@]+@[^@]+.[^@]+", email):
            return ErrorType(message="Incorrect email.")

        if password_1 != password_2:
            return ErrorType(message="Passwords didn't match.")

        if User.objects.filter(email=email).exists():
            return ErrorType(message="User with specified email already exists.")

        if len(password_1) < 3:
            return ErrorType(message="Password must be more than 3 characters.")

        user = User.objects.create(email=email)
        user.full_name = name
        user.set_password(password_1)
        user.save()
        token = get_token(user)
        return RegisterSuccessType(user=user, token=token)


@strawberry.type
class ChangePasswordMutation:
    @strawberry.mutation
    def change_password(
        self, info: Info, password_1: str, password_2: str
    ) -> ChangePasswordResult:
        user = info.context.request.user
        if password_1 == password_2:
            user.set_password(password_1)
            user.save()
            return SuccessType(message="Password changed success")
        else:
            return ErrorType(message="Passwords didn't match.")


@strawberry.type
class SendForgotPasswordMutation:
    @strawberry.mutation
    def send_forgot_password(self, email: str) -> ForgotPasswordResult:

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
        else:
            return ErrorType(message="User does not exists")

        code = send_verification_code(user.email)
        new_code, status = LastVerificationCode.objects.get_or_create(user=user)
        if new_code.code != code:
            new_code.code = code
        if not status:
            new_code.code = code
        new_code.save()
        return SuccessType(message="Code send successful")


@strawberry.type
class VerifyForgotPasswordMutation:
    @strawberry.mutation
    def verify_forgot_password(
        self, email: str, code: str
    ) -> VerifyForgotPasswordResult:

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
        else:
            return ErrorType(message="User does not exists")
        if LastVerificationCode.objects.filter(user=user).exists():
            last_code = LastVerificationCode.objects.get(user=user)
        else:
            return ErrorType(message="Code does not exists")
        if code == last_code.code:
            if last_code.valid:
                token = get_token(user)
                return VerifyForgotPasswordSuccessType(token=token)
            else:
                return ErrorType(message="Code time out")
        else:
            return ErrorType(message="Code does not match")


@strawberry.type
class SetAvatarMutation:
    @strawberry.mutation
    def set_avatar(self, info: Info, file: Upload) -> SetAvatarResult:
        if not file:
            return ErrorType(message="Not file")
        user = info.context.request.user
        user.avatar = file
        user.save()
        return SuccessType(message="Avatar set successful")
