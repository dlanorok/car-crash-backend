from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

from api.common.serializer import SmsSerializer
from api.common.sms.sms_sender import SmsSender


class SendSMSViewSet(CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = SmsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        content = serializer.validated_data['content']
        recipient = serializer.validated_data['recipient']

        try:
            SmsSender.send_sms(recipient, content)
            return Response({'message': 'SMS sent successfully.'}, status=200)
        except Exception as e:
            return Response({'message': str(e)}, status=500)
