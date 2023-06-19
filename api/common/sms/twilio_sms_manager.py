from twilio.rest import Client

from api.common.sms.sms_manager_interface import SmsManagerInterface
from rest_framework.response import Response

class TwilioSmsManager(SmsManagerInterface):

    def __init__(self, api_key, api_key_secret, account_sid, from_number):
        super().__init__(from_number)
        self.client = Client(api_key, api_key_secret, account_sid)

    def send_sms(self, to_phone_number, content):
        try:
            self.client.messages.create(
                body=content,
                from_=self.from_number,
                to=to_phone_number
            )
            return Response({'message': 'SMS sent successfully.'}, status=200)
        except Exception as e:
            return Response({'message': str(e)}, status=500)

