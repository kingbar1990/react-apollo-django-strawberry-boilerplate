from io import BytesIO

from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image

from server.schema import schema

from .test_views import GraphQLView


def temporary_image() -> SimpleUploadedFile:
    bts = BytesIO()
    img = Image.new("RGB", (100, 100))
    img.save(bts, "jpeg")
    return SimpleUploadedFile("test.jpg", bts.getvalue())


def set_response(request):
    return GraphQLView.as_view(schema=schema)(request)
