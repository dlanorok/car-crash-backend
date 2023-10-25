# INPUTS ID FROM 70-80
from enum import Enum

from django.utils.translation import ugettext_lazy as _


class CrossingStep(str, Enum):
    CIRCUMSTANCES_STEP_2_CROSSING = "circumstances_step_2_crossing"

    CIRCUMSTANCES_STEP_3_CROSSING_DRIVING_STRAIGHT = "circumstances_step_3_crossing_driving_straight"
    CIRCUMSTANCES_STEP_3_CROSSING_TURNING_RIGHT = "circumstances_step_3_crossing_turning_right"
    CIRCUMSTANCES_STEP_3_CROSSING_TURNING_LEFT = "circumstances_step_3_crossing_turning_left"


class CrossingLabel(str, Enum):
    VEHICLE_CROSSING = _('I was at a crossing')

    # Second rank
    CROSSING_STANDING_IN_FRONT_OF_CROSSING_OR_TRAFFIC_LIGHT = _(
        "I was standing in front of merging into traffic or in front of a traffic light")
    CROSSING_CRASHED_TO_VEHICLE_IN_FRONT = _('Crashed with vehicle in front')
    CROSSING_ANOTHER_VEHICLE_CRASHED_FROM_BEHIND = _('Another vehicle crashed from behind')
    CROSSING_DRIVING_STRAIGHT = _("I was driving straight through the crossing")
    CROSSING_TURNING_RIGHT = _("I was turning right")
    CROSSING_TURNING_LEFT = _("I was turning left")

    # third rank
    CROSSING_OBEY_RIGHT_OF_WAY_SIGNS_OR_GREEN_LIGHT = _('I took into account the right-of-way signs or green light')
    CROSSING_NOT_OBEY_RIGHT_OF_WAY_SIGNS_OR_GREEN_LIGHT = _(
        'I did not take into account the right-of-way signs or green light')
    CROSSING_EQUIVALENT_ROADS_CAME_FROM_RIGHT = _(
        'At the intersection of equivalent roads, I was coming from the right in relation to another vehicle')
    CROSSING_EQUIVALENT_ROADS_CAME_FROM_LEFT = _(
        'At the intersection of equivalent roads, I was coming from the left in relation to another vehicle')


section = {
    "value": "crossing",
    "label": CrossingLabel.VEHICLE_CROSSING,
    "action_property": {
        "step": CrossingStep.CIRCUMSTANCES_STEP_2_CROSSING
    }
}

steps = [
    {
        "step_type": CrossingStep.CIRCUMSTANCES_STEP_2_CROSSING,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('5')),
        "updated_inputs": ["37"],
        "inputs": ["70"]
    },
    # SECOND RANK
    {
        "step_type": CrossingStep.CIRCUMSTANCES_STEP_3_CROSSING_DRIVING_STRAIGHT,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('15')),
        "updated_inputs": ["37"],
        "inputs": ["71"]
    },
    {
        "step_type": CrossingStep.CIRCUMSTANCES_STEP_3_CROSSING_TURNING_RIGHT,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('16')),
        "updated_inputs": ["37"],
        "inputs": ["71"]
    },
    {
        "step_type": CrossingStep.CIRCUMSTANCES_STEP_3_CROSSING_TURNING_LEFT,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('17')),
        "updated_inputs": ["37"],
        "inputs": ["71"]
    },
]

inputs = {
    "70": {
        "id": 70,
        "type": "select",
        "value": None,
        "required": True,
        "options": [
            {
                "value": "crossing_standing_or_traffic_light",
                "label": CrossingLabel.CROSSING_STANDING_IN_FRONT_OF_CROSSING_OR_TRAFFIC_LIGHT,
            },
            {
                "value": "crossing_crashed_to_vehicle_in_front",
                "label": CrossingLabel.CROSSING_CRASHED_TO_VEHICLE_IN_FRONT,
            },
            {
                "value": "crossing_another_vehicle_crashed_from_behind",
                "label": CrossingLabel.CROSSING_ANOTHER_VEHICLE_CRASHED_FROM_BEHIND,
            },
            {
                "value": "crossing_driving_straight",
                "label": CrossingLabel.CROSSING_DRIVING_STRAIGHT,
                "action_property": {
                    "step": CrossingStep.CIRCUMSTANCES_STEP_3_CROSSING_DRIVING_STRAIGHT
                }
            },
            {
                "value": "crossing_turning_right",
                "label": CrossingLabel.CROSSING_TURNING_RIGHT,
                "action_property": {
                    "step": CrossingStep.CIRCUMSTANCES_STEP_3_CROSSING_TURNING_RIGHT
                }
            },
            {
                "value": "crossing_turning_left",
                "label": CrossingLabel.CROSSING_TURNING_LEFT,
                "action_property": {
                    "step": CrossingStep.CIRCUMSTANCES_STEP_3_CROSSING_TURNING_LEFT
                }
            },
        ]
    },
    "71": {
        "id": 71,
        "type": "select",
        "value": None,
        "required": True,
        "options": [
            {
                "value": "crossing_obey_right_of_way_signs_or_green_light",
                "label": CrossingLabel.CROSSING_OBEY_RIGHT_OF_WAY_SIGNS_OR_GREEN_LIGHT,
            },
            {
                "value": "crossing_not_obey_right_of_way_signs_or_green_light",
                "label": CrossingLabel.CROSSING_NOT_OBEY_RIGHT_OF_WAY_SIGNS_OR_GREEN_LIGHT,
            },
            {
                "value": "crossing_equivalent_roads_came_from_right",
                "label": CrossingLabel.CROSSING_EQUIVALENT_ROADS_CAME_FROM_RIGHT,
            },
            {
                "value": "crossing_equivalent_roads_came_from_left",
                "label": CrossingLabel.CROSSING_EQUIVALENT_ROADS_CAME_FROM_LEFT,
            },
        ]
    }
}

to_model_mapper = {
    "70": {
        "conditions": [
            {
                "property": "rear_same_direction",
                "value": "crossing_crashed_to_vehicle_in_front"
            },
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
    "71": {
        "conditions": [
            {
                "property": "disregarding_right_of_way_red_light",
                "value": "crossing_not_obey_right_of_way_signs_or_green_light"
            },
            {
                "property": "from_right_crossing",
                "value": "crossing_equivalent_roads_came_from_right"
            },
        ]
    }
}
