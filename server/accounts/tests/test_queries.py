import json

import pytest
from accounts.models import User
from django.test.client import RequestFactory
from strawberry_django_jwt.shortcuts import get_token

from .query_queries import queryFindUser, queryMe
from .utils import set_response


@pytest.mark.django_db
def test_query_me():
    user = User.objects.create(email="test@test.com")

    factory = RequestFactory()
    request = factory.post(
        "/graphql/", {"query": queryMe}, content_type="application/json"
    )

    request.user = user

    data = json.loads(set_response(request).content.decode())

    assert not data.get("errors")
    assert data["data"]["me"]["user"]["email"] == "test@test.com"

    User.objects.all().delete()


@pytest.mark.django_db
def test_query_me_with_token():

    user = User.objects.create(email="test@test.com")
    token = get_token(user)
    factory = RequestFactory()

    request = factory.post(
        "/graphql/",
        {"query": queryMe},
        content_type="application/json",
        HTTP_AUTHORIZATION=f"JWT {token}",
    )

    data = json.loads(set_response(request).content.decode())

    assert not data.get("errors")
    assert data["data"]["me"]["user"]["email"] == user.email

    User.objects.all().delete()


@pytest.mark.django_db
def test_query_find_user():

    user = User.objects.create(email="test@test.com")

    factory = RequestFactory()

    variables = {"email": user.email}

    request = factory.post(
        "/graphql/",
        {"query": queryFindUser, "variables": variables},
        content_type="application/json",
    )

    data = json.loads(set_response(request).content.decode())

    assert not data.get("errors")
    assert data["data"]["findUser"]["email"] == user.email

    User.objects.all().delete()


@pytest.mark.django_db
def test_query_users():

    user_1 = User.objects.create(email="test1@test.com")
    user_2 = User.objects.create(email="test2@test.com")
    users_emails = [user_1.email, user_2.email]

    factory = RequestFactory()
    query = "{ users{email} }"

    request = factory.post(
        "/graphql/",
        {"query": query},
        content_type="application/json",
    )
    data = json.loads(set_response(request).content.decode())

    assert not data.get("errors")
    assert type(data["data"]["users"]) == list
    for user in data["data"]["users"]:
        assert user["email"] in users_emails
    User.objects.all().delete()
