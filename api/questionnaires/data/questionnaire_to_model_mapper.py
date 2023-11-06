from api.cars.models import Car
from api.crashes.models import Crash
from api.drivers.models import Driver
from api.files.models import File
from api.insurances.models import Insurance
from api.policy_holders.models import PolicyHolder
from api.questionnaires.data.circumstances.crossing import crossing_questionnaire
from api.questionnaires.data.circumstances.driving_straight import driving_straight_questionnaire
from api.questionnaires.data.circumstances.moving import moving_questionnaire
from api.questionnaires.data.circumstances.parked import parked_questionnaire
from api.questionnaires.data.circumstances.roundabout import roundabout_questionnaire
from api.questionnaires.data.insurances import supported_insurances
from api.questionnaires.data.questionnaire import Place, PhoneNumber, Country, ConfirmedEditors
from api.sketches.models import Sketch

def insuranceDataModfFun(key):
    insurances_values = list(map(lambda insurance: insurance.get("value"),supported_insurances))
    if key in insurances_values:
        index = insurances_values.index(key)
        return supported_insurances[index].get("label")

    return ''

def replaceNewLineWithComma(value):
    return value.replace("\n", ",")

questionnaire_to_model_mapper = {
    "1": {
        "model": Crash,
        "property": "injuries"
    },
    "2": {
        "model": Crash,
        "property": "vehicle_material_damage"
    },
    "4": {
        "model": Crash,
        "property": "participants"
    },
    "7": {
        "model": Crash,
        "property": "date_of_accident"
    },
    "9": {
        "model": Crash,
        "mapper": {
            "place": {"dataclass": Place},
            "country": {"dataclass": Country},
        }
    },
    "27": {
        "model": Car,
        "mapper": {
            "initial_impact": {"fe_property": "selectedParts"},
            "initial_impact_svg_file": {"fe_property": "file_id", "model": File},
        }
    },
    "28": {
        "model": Car,
        "mapper": {
            "damaged_parts": {"fe_property": "selectedParts"},
            "damaged_parts_svg_file": {"fe_property": "file_id", "model": File},
        }
    },
    "29": {
        "model": Car,
        "property": "registration_plate"
    },
    "30": {
        "model": Car,
        "property": "registration_country"
    },
    "40": {
        "model": Car,
        "property": "car_type",
    },
    "31": {
        "model": Insurance,
        "property": "name",
        "dataModFun": insuranceDataModfFun
    },
    "32": {
        "model": Insurance,
        "property": "policy_number",
    },
    "41": {
        "model": Insurance,
        "property": "green_card",
    },
    "42": {
        "model": Insurance,
        "property": "valid_until",
    },
    "53": {
        "model": Insurance,
        "property": "valid_from",
    },
    "50": {
        "model": Insurance,
        "property": "damage_insured",
    },
    "43": {
        "model": PolicyHolder,
        "property": "name",
    },
    "54": {
        "model": PolicyHolder,
        "property": "surname",
    },
    "44": {
        "model": PolicyHolder,
        "property": "address",
    },
    "45": {
        "model": PolicyHolder,
        "property": "email_phone_number",
        "dataclass": PhoneNumber
    },
    "46": {
        "model": PolicyHolder,
        "property": "country_code",
    },
    "33": {
        "model": Driver,
        "property": "email",
    },
    "34": {
        "model": Driver,
        "property": "phone_number",
        "dataclass": PhoneNumber
    },
    "36": {
        "model": Driver,
        "mapper": {
            "name": {"fe_property": "name"},
            "surname": {"fe_property": "surname"},
            "address": {"fe_property": "address", "dataModFun": replaceNewLineWithComma},
            "country": {"fe_property": "country"},
            "driving_licence_number": {"fe_property": "driving_licence_number"},
            "driving_licence_valid_to": {"fe_property": "driving_licence_valid_to"},
            "driving_licence_category": {"fe_property": "driving_licence_category"},
            "date_of_birth": {"fe_property": "date_of_birth"}
        }
    },
    "37": {
        "model": Sketch,
        "mapper": {
            "file": {"fe_property": "file_id", "model": File},
            "confirmed_editors": {"dataclass": ConfirmedEditors},
        }
    },
    "38": {
        "model": Car,
        "property": "responsibility_type"
    },
    "35": {
        "model": Car,
        "property": "witnesses"
    },
    "39": {
        "model": Car,
        "property": "additional_data"
    }
}


circumstance_to_model_mapper = {
    "3": {
        "conditions": [
            {
                "property": "parked_stopped",
                "value": "parked"
            },
            {
                "property": "driving_on_opposite_lane",
                "value": "driving_straight_another_lane"
            }
        ]
    },
}
circumstance_to_model_mapper.update(moving_questionnaire.to_model_mapper)
circumstance_to_model_mapper.update(parked_questionnaire.to_model_mapper)
circumstance_to_model_mapper.update(roundabout_questionnaire.to_model_mapper)
circumstance_to_model_mapper.update(crossing_questionnaire.to_model_mapper)
circumstance_to_model_mapper.update(driving_straight_questionnaire.to_model_mapper)

