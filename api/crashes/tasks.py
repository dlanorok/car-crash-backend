from api.crashes.helpers.create_pdf import create_pdf_from_crash
from api.crashes.helpers.email_helper import send_pdf
from api.crashes.models import Crash
from config import celery_app

@celery_app.task
def create_pdf_from_crash_async(session_id, recipients):
    crash = Crash.objects.get(session_id=session_id)
    create_pdf_from_crash(crash)
    send_pdf(crash.pdf, recipients)
    crash.closed = True
    crash.save()
