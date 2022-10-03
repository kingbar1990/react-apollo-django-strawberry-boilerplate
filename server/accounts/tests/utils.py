from io import BytesIO
from PIL import Image

from django.core.files.uploadedfile import SimpleUploadedFile

from .test_views import GraphQLView
from server.schema import schema


def temporary_image() -> SimpleUploadedFile:
    bts = BytesIO()
    img = Image.new("RGB", (100, 100))
    img.save(bts, 'jpeg')
    return SimpleUploadedFile('test.jpg', bts.getvalue())


def set_response(request):
    return GraphQLView.as_view(schema=schema)(request)
