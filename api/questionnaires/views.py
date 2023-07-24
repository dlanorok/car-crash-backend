import json
import os

from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.common.views.event_view import EventView
from api.common.views.session_view import SessionView
from api.questionnaires.data.questionnaire import QUESTIONNAIRE
from api.questionnaires.models import Questionnaire
from api.questionnaires.serializers import QuestionnaireSerializer


class QuestionnaireViewSet(SessionView,
                           mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           EventView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

    def get_by_session(self, session_id):
        return Questionnaire.objects.all()

    @action(detail=False, methods=['get'])
    def load_or_create(self, request):
        # Create session
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        session_key = self.request.session.session_key
        crash_id = self.get_crash_id_from_headers()

        if not crash_id:
            return Response(data='SessionId is missing', status=status.HTTP_400_BAD_REQUEST)

        existing_questionnaires = Questionnaire.objects.filter(creator=session_key, crash__session_id=crash_id)

        if existing_questionnaires:
            serializer = QuestionnaireSerializer(existing_questionnaires, many=True)
        else:
            questionnaire = Questionnaire()
            questionnaire.creator = session_key
            questionnaire.data = QUESTIONNAIRE
            questionnaire.crash = self.get_crash_from_session()
            questionnaire.save()
            serializer = QuestionnaireSerializer([questionnaire], many=True)


        return Response(data=serializer.data, status=status.HTTP_200_OK)

