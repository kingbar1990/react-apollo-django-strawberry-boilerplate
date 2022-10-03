from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .utils import generate_four_digit_code


@shared_task(name="send_verification_code")
def send_verification_code(email: str, subject="Test") -> str:
    code = generate_four_digit_code()
    html_message = render_to_string(
        "forgot_password.html",
        {"code": code, "email": email, "support_redirect": settings.SUPPORT_REDIRECT},
    )
    send_mail(
        subject,
        "",
        settings.DEFAULT_FROM_EMAIL,
        [email],
        html_message=html_message,
        fail_silently=False,
    )
    return code
