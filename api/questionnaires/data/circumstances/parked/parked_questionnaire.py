# INPUTS ID FROM 100-110
from enum import Enum

from django.utils.translation import ugettext_lazy as _


class ParkedStep(str, Enum):
    VEHICLE_PARKED_1 = 'vehicle_parked'
    CIRCUMSTANCES_STEP_2_PARKED = "circumstances_step_2_parked"
    CIRCUMSTANCES_STEP_3_PARKED_LEAVING_CAR = "circumstances_step_3_parked_leaving_car"
    CIRCUMSTANCES_STEP_3_PARKED_ENTERING_CAR = "circumstances_step_3_parked_entering_car"


class ParkedLabel(str, Enum):
    PARKED_LEAVING_CAR = _('I was leaving car')
    PARKED_ENTERING_CAR = _('I was entering car')
    PARKED_NOT_BY_THE_CAR = _('I was not by the car')
    DOORS_CLOSED = _("Doors were closed")
    DOORS_OPENED = _("Doors were opened")


section = {
    "value": "parked",
    "label": ParkedStep.VEHICLE_PARKED_1,
    "action_property": {
        "step": ParkedStep.CIRCUMSTANCES_STEP_2_PARKED
    }
}

steps = [
    {
        "step_type": ParkedStep.CIRCUMSTANCES_STEP_2_PARKED,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('2')),
        "updated_inputs": ["37"],
        "inputs": ["100"]
    },
    {
        "step_type": ParkedStep.CIRCUMSTANCES_STEP_3_PARKED_LEAVING_CAR,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('7')),
        "updated_inputs": ["37"],
        "inputs": ["101"]
    },
    {
        "step_type": ParkedStep.CIRCUMSTANCES_STEP_3_PARKED_ENTERING_CAR,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('8')),
        "updated_inputs": ["37"],
        "inputs": ["102"]
    },
]

inputs = {
    "100": {
        "id": 100,
        "type": "select",
        "value": None,
        "required": True,
        "options": [
            {
                "value": "leaving_car",
                "label": ParkedLabel.PARKED_LEAVING_CAR,
                "action_property": {
                    "step": ParkedStep.CIRCUMSTANCES_STEP_3_PARKED_LEAVING_CAR
                }
            },
            {
                "value": "entering_parked_car",
                "label": ParkedLabel.PARKED_ENTERING_CAR,
                "action_property": {
                    "step": ParkedStep.CIRCUMSTANCES_STEP_3_PARKED_ENTERING_CAR
                }
            },
            {
                "value": "not_in_car",
                "label": ParkedLabel.PARKED_NOT_BY_THE_CAR,
            }
        ]
    },
"101": {
      "id": 101,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "parked_leaving_car_doors_closed",
          "label": ParkedLabel.DOORS_CLOSED,
        },
        {
          "value": "parked_leaving_car_doors_opened",
          "label": ParkedLabel.DOORS_OPENED,
        },
      ]
    },
    "102": {
      "id": 102,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "parked_entering_car_doors_closed",
          "label": ParkedLabel.DOORS_CLOSED,
        },
        {
          "value": "parked_entering_car_doors_opened",
          "label": ParkedLabel.DOORS_OPENED,
        },
      ]
    },
}


to_model_mapper = {
    "101": {
        "conditions": [
            {
                "property": "leaving_parking_opening_door",
                "value": "parked_leaving_car_doors_opened"
            }
        ]
    },
    "102": {
        "conditions": [
            {
                "property": "leaving_parking_opening_door",
                "value": "parked_entering_car_doors_opened"
            }
        ]
    },
}
