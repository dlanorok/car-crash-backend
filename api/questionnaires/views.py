import copy

from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.cars.models import Car
from api.common.views.event_view import EventView
from api.common.views.session_view import SessionView
from api.questionnaires.data.constants import circumstances_input_ids
from api.questionnaires.data.helpers import circumstance_input_to_arrow
from api.questionnaires.data.prefilled_questionnaire import dario
from api.questionnaires.data.questionnaire import QUESTIONNAIRE_MAP, QUESTIONNAIRE
from api.questionnaires.models import Questionnaire
from api.questionnaires.serializers import QuestionnaireSerializer
from api.questionnaires.tasks import map_questionnaire_to_models


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
            serializer_many = QuestionnaireSerializer(crash_questionnaires, many=True)
        else:
            crash = self.get_crash_from_session()
            car = Car(crash=crash, creator=session_key)
            car.save()
            questionnaire = copy.deepcopy(QUESTIONNAIRE)
            if request.query_params.get("user") == "dario":
                for input_id, value in dario.items():
                    questionnaire['inputs'][input_id]['value'] = value

            data = {
                "creator": session_key,
                "data": questionnaire,
                "crash": crash.id,
                "car": car.id
            }

            if len(crash_questionnaires) > 0:
                data.get("data").update(sections=list(filter(lambda section: section.get("id") not in ["starting_questions", "invite"],
                                                             data.get("data").get("sections"))))
                self.update_all_shared_inputs(data, crash_questionnaires.first())

            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            questionnaires = Questionnaire.objects.filter(crash=serializer.instance.crash)
            ids = list(map(lambda questionnaire: questionnaire.id, questionnaires))
            for _questionnaire in questionnaires:
                sketch_input = _questionnaire.data['inputs']["37"]
                value = sketch_input.get("value", {})
                if not value:
                    value = {"cars": []}

                value.update(cars=[{"questionnaire_id": id} for id in ids])
                # Reset confirmed ediotrs
                value.update(confirmed_editors=[])
                serializer = QuestionnaireSerializer(_questionnaire, data={}, partial=True)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)


            serializer_many = QuestionnaireSerializer(questionnaires, many=True)


        return Response(data=serializer_many.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['patch'])
    def update_inputs(self, request, pk=None):
        questionnaire = self.get_object()
        shared_input_ids = []

        for input_id, value in request.data.items():
            inputs_changed = self.input_actions(input_id, value, questionnaire)
            for input_changed in inputs_changed:
                shared_input_ids.append(input_changed)

            questionnaire.data['inputs'][input_id].update(value=value)
            if questionnaire.data['inputs'][input_id].get("shared_input"):
                shared_input_ids.append(input_id)

        if shared_input_ids:
            questionnaires = Questionnaire.objects.filter(crash=questionnaire.crash).exclude(id=questionnaire.id)
            for _questionnaire in questionnaires:
                for shared_input_id in shared_input_ids:
                    _questionnaire.data['inputs'][shared_input_id] = questionnaire.data['inputs'][shared_input_id]
                serializer = QuestionnaireSerializer(_questionnaire, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                super().perform_update(serializer)

        serializer = QuestionnaireSerializer(questionnaire, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        super().perform_update(serializer)

        map_questionnaire_to_models(request.data, questionnaire)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def update_all_shared_inputs(self, questionnaire_data, questionnaire):
        inputs = list(filter(lambda input: input.get("shared_input"), list(questionnaire.data.get("inputs").values())))
        for input in inputs:
            questionnaire_data.get("data").get("inputs")[str(input.get("id"))] = input


    def input_actions(self, input_id, value, questionnaire):
        if input_id in circumstances_input_ids and questionnaire.data.get("inputs")[input_id].get("value") != value:

            input_to_restore = self.connected_input_ids(input_id, [])
            for input_id in input_to_restore:
                questionnaire.data.get("inputs")[input_id].update(value=None)

            new_arrow = circumstance_input_to_arrow(value)
            if new_arrow:
                current_value = questionnaire.data.get("inputs")["37"].get("value", {})
                current_value.update(confirmed_editors=[])
                for car in current_value['cars']:
                    if car.get("questionnaire_id") == questionnaire.id:
                        car["arrow"] = new_arrow
                questionnaire.data.get("inputs")["37"].update(value=current_value)
                return ["37"]

        return []

    def connected_input_ids(self, input_id, acc_arr):
        map = QUESTIONNAIRE_MAP

        acc_arr.append(input_id)
        if len(map.get(input_id, [])) == 0:
            return acc_arr

        for input_id in map.get(input_id):
            self.connected_input_ids(input_id, acc_arr)

        return acc_arr
