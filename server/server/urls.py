from strawberry_django_jwt.decorators import jwt_cookie
from strawberry_django_jwt.views import StatusHandlingGraphQLView as GQLView

from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from .schema import schema
# from strawberry.django.views import GraphQLView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('graphql/', jwt_cookie(GQLView.as_view(schema=schema))),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
