from django.utils.translation import ugettext_lazy as _
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.cars.models import Car
from api.cars.serializers import CarSerializer
from api.common.views.event_view import EventView
from api.crashes.helpers.create_pdf import create_pdf_from_crash
from api.crashes.helpers.email_helper import send_pdf
from api.crashes.models import Crash
from api.crashes.serializers import CrashSerializer
from api.questionnaires.serializers import QuestionnaireSerializer


class CrashViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   EventView):
    queryset = Crash.objects.all()
    serializer_class = CrashSerializer
    lookup_field = 'session_id'

    def perform_create(self, serializer):
        # Create session
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer.validated_data['creator'] = self.request.session.session_key

        super().perform_create(serializer)

    @action(detail=True, methods=['get'])
    def summary(self, request, session_id=None):
        crash = self.get_object()
        session_key = self.request.session.session_key

        cars = Car.objects.filter(crash=crash).exclude(crash__questionnaires__creator__in=[session_key])
        serializer = CarSerializer(cars, many=True)

        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=True, methods=['post'])
    def generate_pdf(self, request, session_id=None):
        crash = self.get_object()
        create_pdf_from_crash(crash)

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def confirm_crash(self, request, session_id=None):
        crash = self.get_object()
        session_key = self.request.session.session_key

        questionnaires = crash.questionnaires.all()
        if len(questionnaires) < 2:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=_("Not enough cars to confirm the crash"))

        if all(_questionnaire.crash_confirmed if _questionnaire.creator != session_key else True for _questionnaire in questionnaires):
            create_pdf_from_crash(crash)
            send_pdf(crash.pdf, list(map(lambda q: q.car.driver.email, questionnaires)))
            crash.closed = True
            crash.save()

        questionnaire = questionnaires.get(creator=session_key, crash=crash)
        if questionnaire:
            questionnaire.crash_confirmed = True
            questionnaire.save()

        serializer = QuestionnaireSerializer(questionnaire, data=request.data, partial=True)
        serializer.is_valid()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
