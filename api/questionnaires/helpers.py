def set_is_questionnaire_completed(questionnaire):
    is_completed = questionnaire.car.driver.is_valid() and questionnaire.car.is_valid() and \
           questionnaire.crash.sketch.is_valid() and \
           questionnaire.car.policy_holder.is_valid() and \
           questionnaire.car.insurance.is_valid() and \
           questionnaire.car.circumstances.is_valid()

    if is_completed:
        questionnaire.completed = True
