import json

from django.conf import settings
from django.core.mail import EmailMessage
from django.utils.translation import ugettext_lazy as _

from api.crashes.serializers import CrashJSONSerializer


def send_pdf(crash, recipients):
    pdf = crash.pdf
    email = EmailMessage(
        subject=_("Crash confirmed"),
        body="Content",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipients
    )

    email.attach("crash.json", json.dumps(CrashJSONSerializer(crash).data), "text/plain")
    email.attach(pdf.file.name, pdf.file.read())
    email.send()
