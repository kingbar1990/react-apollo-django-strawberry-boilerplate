import json

import pytest
from accounts.models import LastVerificationCode, User
from django.test.client import RequestFactory
from strawberry_django_jwt.shortcuts import get_token

from .query_mutations import (
    ChangePassword,
    VerifyForgotPassword,
    login_mutations,
    register_mutation,
    sendForgotPassword,
    setAvatar,
    verifyTokenMutation,
)
from .utils import set_response, temporary_image

factory = RequestFactory()


def set_params(mutation, variables):
    return {"query": f"mutation { mutation }", "variables": variables}


@pytest.mark.django_db
def test_login_mutation():
    user = User.objects.create(email="test@test.com")
    user.set_password("qweqweqwe")
    user.save()
    variables = {"email": "test@test.com", "password": "qweqweqwe"}
    params = set_params(login_mutations, variables)

    request = factory.post("/graphql/", data=params, content_type="application/json")
    data = json.loads(set_response(request).content.decode())

    assert not data.get("errors")
    assert data["data"]["login"]["user"]["email"] == user.email
    assert data["data"]["login"]["token"]

    User.objects.all().delete()


@pytest.mark.django_db
def test_login_password_incorrect_error_mutation():
    user = User.objects.create(email="test@test.com")
    user.set_password("qweqweqwe")
    user.save()
    variables = {"email": "test@test.com", "password": "error"}
    params = set_params(login_mutations, variables)

    request = factory.post("/graphql/", data=params, content_type="application/json")
    data = json.loads(set_response(request).content.decode())

    assert not data.get("errors")
    assert (
        data["data"]["login"]["message"]
        == "User with specified email does not exists or password incorrect."
    )

    User.objects.all().delete()


@pytest.mark.django_db
def test_register_mutation():
    variables = {
        "email": "test@test.com",
        "password1": "qweqweqwe",
        "password2": "qweqweqwe",
        "name": "test",
    }
    params = set_params(register_mutation, variables)

    request = factory.post("/graphql/", data=params, content_type="application/json")
    data = json.loads(set_response(request).content.decode())

    assert not data.get("errors")
    assert data["data"]["register"]["user"]["email"] == variables["email"]
    assert data["data"]["register"]["token"]

    User.objects.all().delete()


@pytest.mark.django_db
def test_register_password_didnt_much_error_mutation():
    variables = {
        "email": "test@test.com",
        "password1": "qweqweqwe",
        "password2": "qweqweqwe1",
        "name": "test",
    }
    params = set_params(register_mutation, variables)

    request = factory.post("/graphql/", data=params, content_type="application/json")
    data = json.loads(set_response(request).content.decode())

    assert not data.get("errors")
    assert data["data"]["register"]["message"] == "Passwords didn't match."

    User.objects.all().delete()


@pytest.mark.django_db
def test_register_user_exist_error_mutation():
    User.objects.create(email="test@test.com")
    variables = {
        "email": "test@test.com",
        "password1": "qweqweqwe1",
        "password2": "qweqweqwe1",
        "name": "test",
    }
    params = set_params(register_mutation, variables)

    request = factory.post("/graphql/", data=params, content_type="application/json")
    data = json.loads(set_response(request).content.decode())

    assert not data.get("errors")
    assert (
        data["data"]["register"]["message"]
        == "User with specified email already exists."
    )

    User.objects.all().delete()


@pytest.mark.django_db
def test_register_user_password_length_error_mutation():
    variables = {
        "email": "test@test.com",
        "password1": "qw",
        "password2": "qw",
        "name": "test",
    }
    params = set_params(register_mutation, variables)

    request = factory.post("/graphql/", data=params, content_type="application/json")
    data = json.loads(set_response(request).content.decode())

    assert not data.get("errors")
    assert (
        data["data"]["register"]["message"]
        == "Password must be more than 3 characters."
    )

    User.objects.all().delete()


@pytest.mark.django_db
def test_verify_token_mutation():
    user = User.objects.create(email="test@test.com")
    token = get_token(user)
    variables = {"token": token}
    params = set_params(verifyTokenMutation, variables)

    request = factory.post("/graphql/", data=params, content_type="application/json")
    data = json.loads(set_response(request).content.decode())

    assert not data.get("errors")
    assert data["data"]["verifyToken"]["payload"]["email"] == user.email

    User.objects.all().delete()


@pytest.mark.django_db
def test_send_forgot_password_code_mutation():
    user = User.objects.create(email="test@test.com")
    variables = {"email": user.email}
    params = set_params(sendForgotPassword, variables)

    request = factory.post("/graphql/", data=params, content_type="application/json")
    data = json.loads(set_response(request).content.decode())

    assert not data.get("errors")
    assert data["data"]["sendForgotPassword"]["message"] == "Code send successful"

    User.objects.all().delete()


@pytest.mark.django_db
def test_send_forgot_password_code_error_mutation():
    User.objects.create(email="test@test.com")
    variables = {"email": "error@email"}
    params = set_params(sendForgotPassword, variables)

    request = factory.post("/graphql/", data=params, content_type="application/json")
    data = json.loads(set_response(request).content.decode())

    assert not data.get("errors")
    assert data["data"]["sendForgotPassword"]["message"] == "User does not exists"

    User.objects.all().delete()


@pytest.mark.django_db
def test_verify_forgot_password_code_mutation():
    user = User.objects.create(email="test@test.com")
    variables = {"email": user.email}
    params = set_params(sendForgotPassword, variables)

    request = factory.post("/graphql/", data=params, content_type="application/json")
    json.loads(set_response(request).content.decode())

    code = LastVerificationCode.objects.get(user=user).code

    variables = {"email": user.email, "code": code}
    params = set_params(VerifyForgotPassword, variables)

    request = factory.post("/graphql/", data=params, content_type="application/json")
    data = json.loads(set_response(request).content.decode())

    assert not data.get("errors")
    assert data["data"]["verifyForgotPassword"]["token"]

    User.objects.all().delete()


@pytest.mark.django_db
def test_change_password_mutation():
    user = User.objects.create(email="test@test.com")
    user.set_password("test")
    user.save()
    variables = {"password1": "changed", "password2": "changed"}
    params = set_params(ChangePassword, variables)

    request = factory.post("/graphql/", data=params, content_type="application/json")
    request.user = user
    data = json.loads(set_response(request).content.decode())

    assert not data.get("errors")
    assert data["data"]["changePassword"]["message"] == "Password changed success"

    User.objects.all().delete()


@pytest.mark.django_db
def test_change_password_didnt_much_error_mutation():
    user = User.objects.create(email="test@test.com")
    user.set_password("test")
    user.save()
    variables = {"password1": "changed", "password2": "error"}
    params = set_params(ChangePassword, variables)

    request = factory.post("/graphql/", data=params, content_type="application/json")
    request.user = user
    data = json.loads(set_response(request).content.decode())

    assert not data.get("errors")
    assert data["data"]["changePassword"]["message"] == "Passwords didn't match."

    User.objects.all().delete()


@pytest.mark.django_db
def test_set_avatar_mutation():
    photo_file = temporary_image()

    file = json.dumps(str(photo_file))
    user = User.objects.create(email="test@test.com")
    variables = {"file": file}
    params = set_params(setAvatar, variables)

    request = factory.post("/graphql/", data=params, content_type="application/json")
    request.user = user
    data = json.loads(set_response(request).content.decode())

    assert not data.get("errors")
    assert user.avatar
    assert data["data"]["setAvatar"]["message"] == "Avatar set successful"

    User.objects.all().delete()


@pytest.mark.django_db
def test_set_avatar_not_file_error_mutation():
    user = User.objects.create(email="test@test.com")

    variables = {"file": ""}
    params = set_params(setAvatar, variables)

    request = factory.post("/graphql/", data=params, content_type="application/json")
    request.user = user
    data = json.loads(set_response(request).content.decode())

    assert not data.get("errors")
    assert data["data"]["setAvatar"]["message"] == "Not file"

    User.objects.all().delete()
