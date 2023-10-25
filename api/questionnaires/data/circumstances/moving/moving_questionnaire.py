# INPUTS ID FROM 90-100
from enum import Enum

from django.utils.translation import ugettext_lazy as _


class MovingStep(str, Enum):
    CIRCUMSTANCES_STEP_2_MOVING_PARKING_JOINING = "circumstances_step_2_moving_parking_joining"

    CIRCUMSTANCES_STEP_3_LEAVING_PARKING = "circumstances_step_3_leaving_parking"
    CIRCUMSTANCES_STEP_3_PARKING = "circumstances_step_3_parking"
    CIRCUMSTANCES_STEP_3_LEAVING_PRIVATE_PROPERTY = "circumstances_step_3_leaving_private_property"
    CIRCUMSTANCES_STEP_3_ENTERING_PRIVATE_PROPERTY = "circumstances_step_3_entering_private_property"


class MovingLabel(str, Enum):
    VEHICLE_MOVING = _('I was parking or entering into traffic')
    MOVING_LEAVING_PARKING = _('I was leaving parking slot')
    MOVING_PARKING_CAR = _('I was parking my car')
    MOVING_LEAVING_PRIVATE_PROPERTY = _('I was merging into traffic from private property')
    MOVING_ENTERING_PRIVATE_PROPERTY = _('I was turning to private property')
    DRIVING_STRAIGHT = _('Driving straight')
    DRIVING_REVERSE = _('Driving reverse')
    TURNING_RIGHT = _('Turning right')
    TURNING_LEFT = _('Turning left')


section = {
    "value": "moving",
    "label": MovingLabel.VEHICLE_MOVING,
    "action_property": {
        "step": MovingStep.CIRCUMSTANCES_STEP_2_MOVING_PARKING_JOINING
    }
}

steps = [
    {
        "step_type": MovingStep.CIRCUMSTANCES_STEP_2_MOVING_PARKING_JOINING,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('3')),
        "updated_inputs": ["37"],
        "inputs": ["90"]
    },
    {
        "step_type": MovingStep.CIRCUMSTANCES_STEP_3_LEAVING_PARKING,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('9')),
        "updated_inputs": ["37"],
        "inputs": ["91"]
    },
    {
        "step_type": MovingStep.CIRCUMSTANCES_STEP_3_PARKING,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('10')),
        "updated_inputs": ["37"],
        "inputs": ["92"]
    },

    {
        "step_type": MovingStep.CIRCUMSTANCES_STEP_3_LEAVING_PRIVATE_PROPERTY,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('11')),
        "updated_inputs": ["37"],
        "inputs": ["93"]
    },
    {
        "step_type": MovingStep.CIRCUMSTANCES_STEP_3_ENTERING_PRIVATE_PROPERTY,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('12')),
        "updated_inputs": ["37"],
        "inputs": ["94"]
    },
]

inputs = {
    "90": {
        "id": 90,
        "type": "select",
        "value": None,
        "required": True,
        "options": [
            {
                "value": "leaving_parking_slot",
                "label": MovingLabel.MOVING_LEAVING_PARKING,
                "action_property": {
                    "step": MovingStep.CIRCUMSTANCES_STEP_3_LEAVING_PARKING
                }
            },
            {
                "value": "parking",
                "label": MovingLabel.MOVING_PARKING_CAR,
                "action_property": {
                    "step": MovingStep.CIRCUMSTANCES_STEP_3_PARKING
                }
            },
            {
                "value": "leaving_parking_slot_private_property",
                "label": MovingLabel.MOVING_LEAVING_PRIVATE_PROPERTY,
                "action_property": {
                    "step": MovingStep.CIRCUMSTANCES_STEP_3_LEAVING_PRIVATE_PROPERTY
                }
            },
            {
                "value": "entering_parking_slot_private_property",
                "label": MovingLabel.MOVING_ENTERING_PRIVATE_PROPERTY,
                "action_property": {
                    "step": MovingStep.CIRCUMSTANCES_STEP_3_ENTERING_PRIVATE_PROPERTY
                }
            }
        ]
    },
    "91": {
        "id": 91,
        "type": "select",
        "value": None,
        "required": True,
        "options": [
            {
                "value": "driving_straight",
                "label": MovingLabel.DRIVING_STRAIGHT,
            },
            {
                "value": "driving_reverse",
                "label": MovingLabel.DRIVING_REVERSE,
            },
        ]
    },
    "92": {
        "id": 92,
        "type": "select",
        "value": None,
        "required": True,
        "options": [
            {
                "value": "driving_straight",
                "label": MovingLabel.DRIVING_STRAIGHT,
            },
            {
                "value": "driving_reverse",
                "label": MovingLabel.DRIVING_REVERSE,
            },
        ]
    },
    "93": {
        "id": 93,
        "type": "select",
        "value": None,
        "required": True,
        "options": [
            {
                "value": "driving_straight",
                "label": MovingLabel.DRIVING_STRAIGHT,
            },
            {
                "value": "driving_reverse",
                "label": MovingLabel.DRIVING_REVERSE,
            },
            {
                "value": "turning_left",
                "label": MovingLabel.TURNING_LEFT,
            },
            {
                "value": "turning_right",
                "label": MovingLabel.TURNING_RIGHT,
            },
        ]
    },
    "94": {
        "id": 94,
        "type": "select",
        "value": None,
        "required": True,
        "options": [
            {
                "value": "driving_straight",
                "label": MovingLabel.DRIVING_STRAIGHT,
            },
            {
                "value": "driving_reverse",
                "label": MovingLabel.DRIVING_REVERSE,
            },
            {
                "value": "turning_left",
                "label": MovingLabel.TURNING_LEFT,
            },
            {
                "value": "turning_right",
                "label": MovingLabel.TURNING_RIGHT,
            },
        ]
    },
}


to_model_mapper = {
    "90": {
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
    "91": {
        "conditions": [
            {
                "property": "reversing",
                "value": "driving_reverse"
            }
        ]
    },
    "92": {
        "conditions": [
            {
                "property": "reversing",
                "value": "driving_reverse"
            }
        ]
    },
    "93": {
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
    "94": {
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
}
