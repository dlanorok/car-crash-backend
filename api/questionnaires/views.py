from django.views.decorators.csrf import csrf_exempt
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

        crash_questionnaires = Questionnaire.objects.filter(crash__session_id=crash_id)
        my_questionnaires = list(filter(lambda questionnaire: questionnaire.creator == session_key, crash_questionnaires))

        if my_questionnaires:
            serializer = QuestionnaireSerializer(crash_questionnaires, many=True)
        else:
            questionnaire = Questionnaire()
            questionnaire.creator = session_key
            questionnaire.data = QUESTIONNAIRE
            questionnaire.crash = self.get_crash_from_session()
            questionnaire.save()
            serializer = QuestionnaireSerializer(list(crash_questionnaires) + [questionnaire], many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['patch'])
    def update_inputs(self, request, pk=None):
        questionnaire = self.get_object()
        for key, value in request.data.items():
            index = next((i for i, item in enumerate(questionnaire.data['inputs']) if item["id"] == int(key)), None)
            questionnaire.data['inputs'][index].update(value=value)

        serializer = QuestionnaireSerializer(questionnaire, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        super().perform_update(serializer)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

