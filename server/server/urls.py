from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from strawberry_django_jwt.decorators import jwt_cookie
from strawberry_django_jwt.views import StatusHandlingGraphQLView as GQLView

from .schema import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql/", jwt_cookie(GQLView.as_view(schema=schema))),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
