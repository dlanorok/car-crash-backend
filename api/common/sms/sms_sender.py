from django.conf import settings


class SmsSender:

    @staticmethod
    def send_sms(phone_number, text):
        return settings.SMS_MANAGER.send_sms(phone_number, text)
