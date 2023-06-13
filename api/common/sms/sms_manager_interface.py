class SmsManagerInterface:

    def __init__(self, from_number):
        self.from_number = from_number

    def send_sms(self, phone_number, content):
        pass
