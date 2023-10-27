import json

from django.conf import settings
from django.core.mail import EmailMessage
from django.utils.translation import ugettext_lazy as _

from api.crashes.serializers import CrashJSONSerializer


def send_pdf(crash, recipients):
    pdf = crash.pdf

    cars = crash.cars.all()
    body = _("""
Spoštovani,


V priponki vam pošiljamo potrjen evropski obrazec o prometni nezgodi, v kateri sta bili
udeleženi vozili z registrsko oznako %(car1)s in %(car2)s


Želimo vam, da boste posledice nezgode čim prej uspešno uredili. 

Lep pozdrav,
Vaš Aksi tim
""") % {'car1': cars[0].registration_plate, 'car2': cars[1].registration_plate}

    email = EmailMessage(
        subject=_("Crash confirmed"),
        body=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipients
    )

    email.attach("crash.json", json.dumps(CrashJSONSerializer(crash).data), "text/plain")
    email.attach(pdf.file.name, pdf.file.read())
    email.send()
