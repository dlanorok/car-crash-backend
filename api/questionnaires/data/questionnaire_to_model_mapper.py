from api.cars.models import Car
from api.crashes.models import Crash
from api.drivers.models import Driver
from api.files.models import File
from api.insurances.models import Insurance
from api.policy_holders.models import PolicyHolder
from api.questionnaires.data.questionnaire import Place, PhoneNumber, Country
from api.sketches.models import Sketch

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
        "property": "registration_country",
    },
    "40": {
        "model": Car,
        "property": "car_type",
    },
    "31": {
        "model": Insurance,
        "property": "name",
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
    "43": {
        "model": PolicyHolder,
        "property": "name",
    },
    "44": {
        "model": PolicyHolder,
        "property": "address",
    },
    "45": {
        "model": PolicyHolder,
        "property": "email_phone_number",
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
            "address": {"fe_property": "address"},
            "driving_licence_number": {"fe_property": "driving_licence_number"},
            "driving_licence_valid_to": {"fe_property": "driving_licence_valid_to"}
        }
    },
    "37": {
        "model": Sketch,
        "mapper": {
            "file": {"fe_property": "file_id", "model": File},
        }
    },
    "38": {
        "model": Car,
        "property": "responsibility_type"
    },
    "35": {
        "model": Crash,
        "property": "witnesses"
    },
    "39": {
        "model": Crash,
        "property": "additional_crash_data"
    }
}


circumstance_to_model_mapper = {
    "3": {
        "conditions": [
            {
                "property": "parked_stopped",
                "value": "parked"
            }
        ]
    },
    "6": {
        "conditions": [
            {
                "property": "leaving_parking_opening_door",
                "value": "leaving_parking_slot"
            },
            {
                "property": "entering_parking",
                "value": "parking"
            },
            {
                "property": "emerging_from_car_park",
                "value": "leaving_parking_slot_private_property"
            },
            {
                "property": "entering_car_park",
                "value": "entering_parking_slot_private_property"
            }
        ]
    },
    "11": {
        "conditions": [
            {
                "property": "entering_roundabout",
                "value": "roundabout_entering"
            },
            {
                "property": "circulating_roundabout",
                "value": "roundabout_run_into_vehicle"
            },
            {
                "property": "rear_same_direction",
                "value": "roundabout_run_into_vehicle"
            },
            {
                "property": "circulating_roundabout",
                "value": "roundabout_another_vehicle_crashed_from_behind"
            },
            {
                "property": "circulating_roundabout",
                "value": "roundabout_crashed_with_vehicle_from_another_traffic_lane"
            },
            {
                "property": "same_direction_different_lane",
                "value": "roundabout_crashed_with_vehicle_from_another_traffic_lane"
            },
            {
                "property": "circulating_roundabout",
                "value": "roundabout_changing_traffic_lane"
            },
            {
                "property": "changing_lanes",
                "value": "roundabout_changing_traffic_lane"
            }
        ]
    },
    "12": {
        "conditions": [
            {
                "property": "turning_right",
                "value": "crossing_turning_right"
            },
            {
                "property": "turning_left",
                "value": "crossing_turning_left"
            }
        ]
    },
    "13": {
        "conditions": [
            {
                "property": "rear_same_direction",
                "value": "driving_straight_crashed_with_vehicle_in_front"
            },
            {
                "property": "same_direction_different_lane",
                "value": "driving_straight_crashed_to_vehicle_in_another_lane"
            },
            {
                "property": "changing_lanes",
                "value": "driving_straight_changing_lane"
            },
            {
                "property": "overtaking",
                "value": "driving_straight_overtaking_another_vehicle"
            },
            {
                "property": "reversing",
                "value": "driving_reverse"
            },
            {
                "property": "driving_on_opposite_lane",
                "value": "driving_straight_in_opposite_lane"
            }
        ]
    },
    "14": {
        "conditions": [
            {
                "property": "leaving_parking_opening_door",
                "value": "parked_leaving_car_doors_opened"
            }
        ]
    },
    "15": {
        "conditions": [
            {
                "property": "leaving_parking_opening_door",
                "value": "parked_entering_car_doors_opened"
            }
        ]
    },
    "16": {
        "conditions": [
            {
                "property": "reversing",
                "value": "driving_reverse"
            }
        ]
    },
    "17": {
        "conditions": [
            {
                "property": "reversing",
                "value": "driving_reverse"
            }
        ]
    },
    "18": {
        "conditions": [
            {
                "property": "reversing",
                "value": "driving_reverse"
            },
            {
                "property": "turning_left",
                "value": "turning_left"
            },
            {
                "property": "turning_right",
                "value": "turning_right"
            }
        ]
    },
    "19": {
        "conditions": [
            {
                "property": "reversing",
                "value": "driving_reverse"
            },
            {
                "property": "turning_left",
                "value": "turning_left"
            },
            {
                "property": "turning_right",
                "value": "turning_right"
            }
        ]
    },
    "21": {
        "conditions": [
            {
                "property": "turning_right",
                "value": "changing_driving_lane_right"
            },
            {
                "property": "turning_left",
                "value": "changing_driving_lane_left"
            },
        ]
    },
    "22": {
        "conditions": [
            {
                "property": "from_right_crossing",
                "value": "crossing_entering_from_right"
            },
            {
                "property": "disregarding_right_of_way_red_light",
                "value": "crossing_not_obeying_rules"
            },
        ]
    },
    "23": {
        "conditions": [
            {
                "property": "from_right_crossing",
                "value": "crossing_entering_from_right"
            },
            {
                "property": "disregarding_right_of_way_red_light",
                "value": "crossing_not_obeying_rules"
            },
        ]
    },
    "24": {
        "conditions": [
            {
                "property": "from_right_crossing",
                "value": "crossing_entering_from_right"
            },
            {
                "property": "disregarding_right_of_way_red_light",
                "value": "crossing_not_obeying_rules"
            },
        ]
    },
    "26": {
        "conditions": [
            {
                "property": "turning_right",
                "value": "changing_driving_lane_right"
            },
            {
                "property": "turning_left",
                "value": "changing_driving_lane_left"
            },
        ]
    }
}
