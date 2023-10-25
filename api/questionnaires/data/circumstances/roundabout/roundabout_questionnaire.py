# INPUTS ID FROM 60-70
from enum import Enum

from django.utils.translation import ugettext_lazy as _


class RoundAboutStep(str, Enum):
    CIRCUMSTANCES_STEP_2_ROUNDABOUT = "circumstances_step_2_roundabout"

    CIRCUMSTANCES_STEP_3_ROUNDABOUT_CRASHED_ANOTHER_LANE = "circumstances_step_3_roundabout_crashed_another_lane"
    CIRCUMSTANCES_STEP_3_ROUNDABOUT_CHANGING_LANES = "circumstances_step_3_roundabout_changing_lanes"

    CIRCUMSTANCES_STEP_4_ROUNDABOUT_COLLIDED_SAME_LANE = "circumstances_step_4_roundabout_collided_same_lane"
    CIRCUMSTANCES_STEP_4_ROUNDABOUT_CHANGING_LANES = "circumstances_step_4_roundabout_changing_lanes"


class RoundAboutLabel(str, Enum):
    VEHICLE_ROUNDABOUT = _('I was in a roundabout')

    # SECOND RANK
    ROUNDABOUT_CORRECTLY_DRIVING_ON_MY_LANE = _('I was correctly driving on my lane')
    ROUNDABOUT_ENTERING = _('I was entering roundabout')
    ROUNDABOUT_DROVE_IN_WRONG_DIRECTION = _('Drove in the wrong direction at the roundabout')
    ROUNDABOUT_RUN_INTO_VEHICLE = _('I run into vehicle in front')
    ROUNDABOUT_ANOTHER_VEHICLE_FROM_BEHIND = _('Another vehicle crashed into me from behind')
    ROUNDABOUT_COLLIDED_WITH_VEHICLE_SAME_LANE = _('I collided with a vehicle traveling in the same direction')

    # THIRD RANK
    ROUNDABOUT_COLLIDED_WITH_VEHICLE_DRIVING_SAME_DIRECTION = _(
        'I collided with a vehicle traveling in the same direction but in the other lane')
    ROUNDABOUT_CHANGING_LANES = _('I was changing lanes')

    # FORTH RANK
    VEHICLE_ON_RIGHT = _("Other vehicle was on my right")
    VEHICLE_ON_LEFT = _("Other vehicle was on my left")
    CHANGING_DRIVING_LANE_RIGHT = _("Changed lane to right")
    CHANGING_DRIVING_LANE_LEFT = _("Changed lane to left")


section = {
    "value": "roundabout",
    "label": RoundAboutLabel.VEHICLE_ROUNDABOUT,
    "action_property": {
        "step": RoundAboutStep.CIRCUMSTANCES_STEP_2_ROUNDABOUT
    }
}

steps = [
    # FIRST
    {
        "step_type": RoundAboutStep.CIRCUMSTANCES_STEP_2_ROUNDABOUT,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('4')),
        "updated_inputs": ["37"],
        "inputs": ["60"]
    },

    # SECOND
    {
        "step_type": RoundAboutStep.CIRCUMSTANCES_STEP_3_ROUNDABOUT_CRASHED_ANOTHER_LANE,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('13')),
        "updated_inputs": ["37"],
        "inputs": ["61"]
    },

    # THIRD
    {
        "step_type": RoundAboutStep.CIRCUMSTANCES_STEP_4_ROUNDABOUT_COLLIDED_SAME_LANE,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('13')),
        "updated_inputs": ["37"],
        "inputs": ["62"]
    },
    {
        "step_type": RoundAboutStep.CIRCUMSTANCES_STEP_4_ROUNDABOUT_CHANGING_LANES,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('13')),
        "updated_inputs": ["37"],
        "inputs": ["63"]
    },
]

inputs = {
    "60": {
        "id": 60,
        "type": "select",
        "value": None,
        "required": True,
        "options": [
            {
                "value": "roundabout_correctly_driving_on_my_lane",
                "label": RoundAboutLabel.ROUNDABOUT_CORRECTLY_DRIVING_ON_MY_LANE,
            },
            {
                "value": "roundabout_entering",
                "label": RoundAboutLabel.ROUNDABOUT_ENTERING,
            },
            {
                "value": "roundabout_drove_in_wrong_direction",
                "label": RoundAboutLabel.ROUNDABOUT_DROVE_IN_WRONG_DIRECTION,
            },
            {
                "value": "roundabout_run_into_vehicle",
                "label": RoundAboutLabel.ROUNDABOUT_RUN_INTO_VEHICLE,
            },
            {
                "value": "roundabout_another_vehicle_crashed_from_behind",
                "label": RoundAboutLabel.ROUNDABOUT_ANOTHER_VEHICLE_FROM_BEHIND,
            },
            {
                "value": "roundabout_crashed_with_vehicle_from_another_traffic_lane",
                "label": RoundAboutLabel.ROUNDABOUT_COLLIDED_WITH_VEHICLE_SAME_LANE,
                "action_property": {
                    "step": RoundAboutStep.CIRCUMSTANCES_STEP_3_ROUNDABOUT_CRASHED_ANOTHER_LANE
                }
            },
        ]
    },

    "61": {
        "id": 61,
        "type": "select",
        "value": None,
        "required": True,
        "options": [
            {
                "value": "roundabout_collided_with_vehicle_driving_same_direction",
                "label": RoundAboutLabel.ROUNDABOUT_COLLIDED_WITH_VEHICLE_DRIVING_SAME_DIRECTION,
                "action_property": {
                    "step": RoundAboutStep.CIRCUMSTANCES_STEP_4_ROUNDABOUT_COLLIDED_SAME_LANE
                }
            },
            {
                "value": "roundabout_changing_lanes",
                "label": RoundAboutLabel.ROUNDABOUT_CHANGING_LANES,
                "action_property": {
                    "step": RoundAboutStep.CIRCUMSTANCES_STEP_4_ROUNDABOUT_CHANGING_LANES
                }
            },
        ]
    },
    # THIRD RANK
    "62": {
        "id": 62,
        "type": "select",
        "value": None,
        "required": True,
        "options": [
            {
                "value": "vehicle_on_right",
                "label": RoundAboutLabel.VEHICLE_ON_RIGHT,
            },
            {
                "value": "vehicle_on_left",
                "label": RoundAboutLabel.VEHICLE_ON_LEFT,
            },
        ]
    },
    "63": {
        "id": 63,
        "type": "select",
        "value": None,
        "required": True,
        "options": [
            {
                "value": "changing_driving_lane_right",
                "label": RoundAboutLabel.CHANGING_DRIVING_LANE_RIGHT,
            },
            {
                "value": "changing_driving_lane_left",
                "label": RoundAboutLabel.CHANGING_DRIVING_LANE_LEFT,
            },
        ]
    },
}

to_model_mapper = {
    "60": {
        "conditions": [
            {
                "property": "entering_roundabout",
                "value": "roundabout_entering"
            },
            {
              "property": "driving_on_opposite_lane",
              "value": "roundabout_drove_in_wrong_direction"
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
        ]
    },
    "61": {
        "conditions": [
            {
                "property": "same_direction_different_lane",
                "value": "roundabout_collided_with_vehicle_driving_same_direction"
            },
        ]
    },
    "63": {
        "conditions": [
            {
                "property": "turning_right",
                "value": "vehicle_on_right"
            },
            {
                "property": "turning_left",
                "value": "vehicle_on_left"
            },
        ]
    }
}
