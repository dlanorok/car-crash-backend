# INPUTS ID FROM 80-90
from enum import Enum

from django.utils.translation import ugettext_lazy as _


class DrivingStraightStep(str, Enum):
    CIRCUMSTANCES_STEP_2_STRAIGHT_ROAD = "circumstances_step_2_straight_road"

    CIRCUMSTANCES_STEP_3_STRAIGHT_ROAD_SAME_DIRECTION_ANOTHER_LANE = "circumstances_step_3_straight_road_same_direction_another_lane"

    CIRCUMSTANCES_STEP_4_STRAIGHT_ROAD_COLLIDED_SAME_DIRECTION_DIFFERENT_LANE = "circumstances_step_4_straight_road_collided_same_direction_different_lane"
    CIRCUMSTANCES_STEP_4_STRAIGHT_ROAD_CHANGING_LANES = "circumstances_step_4_straight_road_changing_lanes"



class DrivingStraightLabel(str, Enum):
    VEHICLE_DRIVING_STRAIGHT = _('I was driving on a straight road outside of an intersection or roundabout')

    # Second tank
    DRIVING_STRAIGHT_CORRECTLY_DRIVING_IN_MY_LANE = _('I drove correctly in my lane')
    DRIVING_STRAIGHT_CRASHED_WITH_VEHICLE_IN_FRONT = _("Crashed with vehicle driving in front of me")
    DRIVING_STRAIGHT_CRASHED_FROM_BEHIND = _("Another vehicle crashed into me from behind")
    DRIVING_STRAIGHT_CRASHED_TO_VEHICLE_DRIVING_IN_SAME_DIRECTION = _('I collided with a vehicle driving in the same direction')
    DRIVING_STRAIGHT_OVERTAKING_ANOTHER_VEHICLE = _("Overtaking another vehicle")
    DRIVING_STRAIGHT_REVERSE = _("Driving reverse")

    # Third rank
    DRIVING_STRAIGHT_CRASHED_TO_VEHICLE_IN_ANOTHER_LANE = _("Crashed with vehicle driving in the same direction, but another lane")
    DRIVING_STRAIGHT_CHANGING_LANE = _("Changing lanes")

    VEHICLE_ON_RIGHT = _("Other vehicle was on my right")
    VEHICLE_ON_LEFT = _("Other vehicle was on my left")

    CHANGING_DRIVING_LANE_RIGHT = _("Changed lane to right")
    CHANGING_DRIVING_LANE_LEFT = _("Changed lane to left")

section = {
    "value": "driving_straight",
    "label": DrivingStraightLabel.VEHICLE_DRIVING_STRAIGHT,
    "action_property": {
        "step": DrivingStraightStep.CIRCUMSTANCES_STEP_2_STRAIGHT_ROAD
    }
}

steps = [
    {
        "step_type": DrivingStraightStep.CIRCUMSTANCES_STEP_2_STRAIGHT_ROAD,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('6')),
        "updated_inputs": ["37"],
        "inputs": ["80"]
    },
    {
        "step_type": DrivingStraightStep.CIRCUMSTANCES_STEP_3_STRAIGHT_ROAD_SAME_DIRECTION_ANOTHER_LANE,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('18')),
        "updated_inputs": ["37"],
        "inputs": ["81"]
    },
    {
        "step_type": DrivingStraightStep.CIRCUMSTANCES_STEP_4_STRAIGHT_ROAD_COLLIDED_SAME_DIRECTION_DIFFERENT_LANE,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('18')),
        "updated_inputs": ["37"],
        "inputs": ["82"]
    },
    {
        "step_type": DrivingStraightStep.CIRCUMSTANCES_STEP_4_STRAIGHT_ROAD_CHANGING_LANES,
        "question": str(_('Choose option that suits you the best')),
        "help_text": str(_('18')),
        "updated_inputs": ["37"],
        "inputs": ["83"]
    },
]

inputs = {
    "80": {
        "id": 80,
        "type": "select",
        "value": None,
        "required": True,
        "options": [
            {
                "value": "driving_straight_correctly_driving_in_my_lane",
                "label": DrivingStraightLabel.DRIVING_STRAIGHT_CORRECTLY_DRIVING_IN_MY_LANE,
            },
            {
                "value": "driving_straight_crashed_with_vehicle_in_front",
                "label": DrivingStraightLabel.DRIVING_STRAIGHT_CRASHED_WITH_VEHICLE_IN_FRONT,
            },
            {
                "value": "driving_straight_crashed_from_behind",
                "label": DrivingStraightLabel.DRIVING_STRAIGHT_CRASHED_FROM_BEHIND,
            },
            {
                "value": "driving_straight_crashed_to_vehicle_driving_in_same_direction",
                "label": DrivingStraightLabel.DRIVING_STRAIGHT_CRASHED_TO_VEHICLE_DRIVING_IN_SAME_DIRECTION,
                "action_property": {
                    "step": DrivingStraightStep.CIRCUMSTANCES_STEP_3_STRAIGHT_ROAD_SAME_DIRECTION_ANOTHER_LANE
                }
            },
            {
                "value": "driving_straight_overtaking_another_vehicle",
                "label": DrivingStraightLabel.DRIVING_STRAIGHT_OVERTAKING_ANOTHER_VEHICLE,
            },
            {
                "value": "driving_reverse",
                "label": DrivingStraightLabel.DRIVING_STRAIGHT_REVERSE,
            }
        ]
    },
    "81": {
        "id": 81,
        "type": "select",
        "value": None,
        "required": True,
        "options": [
            {
                "value": "driving_straight_crashed_to_vehicle_driving_in_same_direction",
                "label": DrivingStraightLabel.DRIVING_STRAIGHT_CRASHED_TO_VEHICLE_IN_ANOTHER_LANE,
                "action_property": {
                    "step": DrivingStraightStep.CIRCUMSTANCES_STEP_4_STRAIGHT_ROAD_COLLIDED_SAME_DIRECTION_DIFFERENT_LANE
                }
            },
            {
                "value": "driving_straight_changing_lane",
                "label": DrivingStraightLabel.DRIVING_STRAIGHT_CHANGING_LANE,
                "action_property": {
                    "step": DrivingStraightStep.CIRCUMSTANCES_STEP_4_STRAIGHT_ROAD_CHANGING_LANES
                }
            },
        ]
    },
    "82": {
        "id": 82,
        "type": "select",
        "value": None,
        "required": True,
        "options": [
            {
                "value": "vehicle_on_right",
                "label": DrivingStraightLabel.VEHICLE_ON_RIGHT,
            },
            {
                "value": "vehicle_on_left",
                "label": DrivingStraightLabel.VEHICLE_ON_LEFT,
            },
        ]
    },
    "83": {
        "id": 83,
        "type": "select",
        "value": None,
        "required": True,
        "options": [
            {
                "value": "changing_driving_lane_right",
                "label": DrivingStraightLabel.CHANGING_DRIVING_LANE_RIGHT,
            },
            {
                "value": "changing_driving_lane_left",
                "label": DrivingStraightLabel.CHANGING_DRIVING_LANE_LEFT,
            },
        ]
    },
}

to_model_mapper = {
    "80": {
        "conditions": [
            {
                "property": "rear_same_direction",
                "value": "driving_straight_crashed_with_vehicle_in_front"
            },
            {
                "property": "overtaking",
                "value": "driving_straight_overtaking_another_vehicle"
            },
            {
                "property": "reversing",
                "value": "driving_reverse"
            }
        ]
    },
    "81": {
        "conditions": [
            {
                "property": "same_direction_different_lane",
                "value": "driving_straight_crashed_to_vehicle_driving_in_same_direction"
            },
            {
                "property": "changing_lanes",
                "value": "driving_straight_changing_lane"
            },
        ]
    },
    "83": {
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
}
