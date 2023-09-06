from django.conf import settings
from django.core.mail import EmailMessage
from django.utils.translation import ugettext_lazy as _


def send_pdf(file, recipients):
    email = EmailMessage(
        subject=_("Crash confirmed"),
        body="Content",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipients
    )

    email.attach(file.file.name, file.file.read())
    email.send()
