from api.crashes.helpers.create_pdf import create_pdf_from_crash
from api.questionnaires.data.constants import circumstances_input_ids
from api.questionnaires.data.questionnaire_to_model_mapper import questionnaire_to_model_mapper, \
    circumstance_to_model_mapper
from api.questionnaires.helpers import set_is_questionnaire_completed
from api.questionnaires.models import Questionnaire
from config import celery_app


def save_attribute_to_model(model, mapper, value):
    if "mapper" in mapper:
        for model_property, mapper_value in mapper.get("mapper").items():
            if mapper_value.get("dataclass"):
                setattr(model, model_property, mapper_value.get("dataclass")(**value).to_presentation())
            else:
                _value = value.get(mapper_value.get("fe_property"))
                if mapper_value.get("model") and _value:
                    _value = mapper_value.get("model").objects.get(id=_value)
                setattr(model, model_property, _value)
    else:
        if "dataclass" in mapper:
            value = mapper.get("dataclass")(**value).to_presentation()
        setattr(model, mapper.get("property"), value)

    model.save()

@celery_app.task
def map_questionnaire_to_models(request_dict, questionnaire_id):
    questionnaire = Questionnaire.objects.get(id=questionnaire_id)
    for input_id, value in request_dict.items():
        if input_id in questionnaire_to_model_mapper:
            mapper = questionnaire_to_model_mapper[input_id]
            model = mapper.get("model")
            if model.__name__ == 'Crash':
                save_attribute_to_model(questionnaire.crash, mapper, value)
            elif model.__name__ == 'Insurance':
                save_attribute_to_model(questionnaire.car.insurance, mapper, value)
            elif model.__name__ == 'Driver':
                save_attribute_to_model(questionnaire.car.driver, mapper, value)
            elif model.__name__ == 'PolicyHolder':
                save_attribute_to_model(questionnaire.car.policy_holder, mapper, value)
            elif model.__name__ == 'Sketch':
                save_attribute_to_model(questionnaire.crash.sketch, mapper, value)
            elif model.__name__ == 'Car':
                save_attribute_to_model(questionnaire.car, mapper, value)

        if input_id in circumstances_input_ids:
            for circumstance_input_id in circumstances_input_ids:
                if circumstance_input_id not in circumstance_to_model_mapper:
                    continue

                for condition in circumstance_to_model_mapper.get(circumstance_input_id).get("conditions", []):
                    if questionnaire.data.get("inputs").get(circumstance_input_id).get("value") is None:
                        continue

                    circumstance_value = questionnaire.data.get("inputs").get(circumstance_input_id).get("value") == condition.get("value")
                    if circumstance_value:
                        setattr(questionnaire.car.circumstances, condition.get("property"), circumstance_value)

            questionnaire.car.circumstances.save()

    set_is_questionnaire_completed(questionnaire)
    questionnaire.save()

    # create_pdf_from_crash(questionnaire.crash)
