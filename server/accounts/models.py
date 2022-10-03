import sys
from io import BytesIO

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from PIL import Image

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_("email address"), unique=True)
    full_name = models.CharField(_("full name"), max_length=64, blank=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(_("staff"), default=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def set_avatar(self, file: InMemoryUploadedFile) -> None:
        original_image = Image.open(file)
        image = original_image.convert("RGB")
        filestream = BytesIO()
        image.save(filestream, "JPEG", quality=99)
        self.avatar = InMemoryUploadedFile(
            filestream,
            "ImageField",
            file.name,
            "jpeg/image",
            sys.getsizeof(filestream),
            None,
        )
        self.save()


class LastVerificationCode(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(blank=True, max_length=4)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

    @property
    def valid(self):
        validation = (
            self.code and (self.date + timezone.timedelta(hours=24)) > timezone.now()
        )
        if validation:
            return True
        else:
            self.delete()
            return False
