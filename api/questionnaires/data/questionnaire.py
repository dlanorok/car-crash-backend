from enum import Enum
from django.utils.translation import gettext_lazy as _

from api.questionnaires.data.insurances import supported_insurances


class Step(str, Enum):
  INJURIES = "injuries"
  CAR_DAMAGE = "car_damage"
  AT_ACCIDENT_PLACE = "at_accident_place"
  ACCIDENT_PLACE = "accident_place"
  ACCIDENT_PLACE_TEXT = "accident_place_text"
  ACCIDENT_TIME = "accident_time"
  PARTICIPANTS_NUMBER = "participants_number"
  CIRCUMSTANCES_STEP_1 = "circumstances_step_1"
  CIRCUMSTANCES_STEP_2_PARKED = "circumstances_step_2_parked"
  CIRCUMSTANCES_STEP_2_MOVING_PARKING_JOINING = "circumstances_step_2_moving_parking_joining"
  CIRCUMSTANCES_STEP_2_ROUNDABOUT = "circumstances_step_2_roundabout"
  CIRCUMSTANCES_STEP_2_CROSSING = "circumstances_step_2_crossing"
  CIRCUMSTANCES_STEP_2_STRAIGHT_ROAD = "circumstances_step_2_straight_road"

  CIRCUMSTANCES_STEP_3_PARKED_LEAVING_CAR = "circumstances_step_3_parked_leaving_car"
  CIRCUMSTANCES_STEP_3_PARKED_ENTERING_CAR = "circumstances_step_3_parked_entering_car"

  CIRCUMSTANCES_STEP_3_LEAVING_PARKING = "circumstances_step_3_leaving_parking"
  CIRCUMSTANCES_STEP_3_PARKING = "circumstances_step_3_parking"
  CIRCUMSTANCES_STEP_3_LEAVING_PRIVATE_PROPERTY = "circumstances_step_3_leaving_private_property"
  CIRCUMSTANCES_STEP_3_ENTERING_PRIVATE_PROPERTY = "circumstances_step_3_entering_private_property"

  CIRCUMSTANCES_STEP_3_ROUNDABOUT_CRASHED_ANOTHER_LANE = "circumstances_step_3_roundabout_crashed_another_lane"
  CIRCUMSTANCES_STEP_3_ROUNDABOUT_CHANGING_LANES = "circumstances_step_3_roundabout_changing_lanes"

  CIRCUMSTANCES_STEP_3_CROSSING_DRIVING_STRAIGHT = "circumstances_step_3_crossing_driving_straight"
  CIRCUMSTANCES_STEP_3_CROSSING_TURNING_RIGHT = "circumstances_step_3_crossing_turning_right"
  CIRCUMSTANCES_STEP_3_CROSSING_TURNING_LEFT = "circumstances_step_3_crossing_turning_left"

  CIRCUMSTANCES_STEP_3_STRAIGHT_ROAD_SAME_DIRECTION_ANOTHER_LANE = "circumstances_step_3_straight_road_same_direction_another_lane"
  CIRCUMSTANCES_STEP_3_STRAIGHT_ROAD_CHANGING_LANES = "circumstances_step_3_straight_road_changing_lanes"

  COLLISION_DIRECTION = 'collision_direction'
  DAMAGED_PARTS = 'damaged_parts'
  ACCIDENT_SKETCH = 'accident_sketch'

  REGISTRATION_NUMBER = "registration_number"
  REGISTRATION_COUNTRY = "registration_country"
  INSURANCE_NAME = "insurance_name"
  INSURANCE_NUMBER = 'insurance_number'

  DRIVER_PERSONAL_DATA = 'driver_personal_data'
  DRIVER_DATA = 'driver_data'

  WITNESSES = 'witnesses'


class Action(str, Enum):
  CALL = 'call',
  NEXT_STEP = 'next_step'


class Section(str, Enum):
  STARTING_QUESTIONS = _('Starting questions')
  CIRCUMSTANCES = _('Circumstances')
  VEHICLE_DAMAGES = _('Vehicle damages')
  ACCIDENT_SKETCH = _('Accident sketch')
  CAR_AND_INSURANCE = _('Car and Insurance data')
  DRIVER = _('Driver')
  ADDITIONAL = _('Additional')

class PlaceHolder(str, Enum):
  STREET = _('Miklošičeva 21')

class Label(str, Enum):
  CALL_112 = _('Call 112')
  WE_ARE_OK = _('We are OK')
  YES = _('Yes')
  NO = _('No')

  # CIRCUMSTANCES STEP 1
  VEHICLE_PARKED = _('My vehicle was parked')
  VEHICLE_MOVING = _('I was parking or entering into traffic')
  VEHICLE_ROUNDABOUT = _('I was in a roundabout')
  VEHICLE_CROSSING = _('I was at a crossing')
  VEHICLE_DRIVING_STRAIGHT = _('I was driving straight')

  # CIRCUMSTANCES STEP 2
  PARKED_LEAVING_CAR = _('I was leaving car')
  PARKED_ENTERING_CAR = _('I was entering car')
  PARKED_NOT_BY_THE_CAR = _('I was not by the car')

  MOVING_LEAVING_PARKING = _('I was leaving parking slot')
  MOVING_PARKING_CAR = _('I was parking my car')
  MOVING_LEAVING_PRIVATE_PROPERTY = _('I was merging into traffic from private property')
  MOVING_ENTERING_PRIVATE_PROPERTY = _('I was turning to private property')

  ROUNDABOUT_ENTERING = _('I was entering roundabout')
  ROUNDABOUT_RUN_INTO_VEHICLE = _('I run into vehicle in front')
  ROUNDABOUT_ANOTHER_VEHICLE_FROM_BEHIND = _('Another vehicle crashed into me from behind')
  ROUNDABOUT_CRASHED_WITH_VEHICLE_FROM_ANOTHER_TRAFFIC_LANE = _('Crashed with another vehicle from another traffic lane')
  ROUNDABOUT_CHANGING_TRAFFIC_LANE = _('I was changing traffic lane')

  CROSSING_STANDING_IN_FRONT_OF_CROSSING_OR_TRAFFIC_LIGHT = _("I was standing in front of merging into traffic or in front of a traffic light")
  CROSSING_DRIVING_STRAIGHT = _("I was driving straight through the crossing")
  CROSSING_TURNING_RIGHT = _("I was turning right")
  CROSSING_TURNING_LEFT = _("I was turning left")

  DRIVING_STRAIGHT_CRASHED_WITH_VEHICLE_IN_FRONT = _("Crashed with vehicle driving in front of me")
  DRIVING_STRAIGHT_CRASHED_FROM_BEHIND = _("Another vehicle crashed into me from behind")
  DRIVING_STRAIGHT_CRASHED_TO_VEHICLE_IN_ANOTHER_LANE = _("Crashed with vehicle driving in the same direction, but another lane")
  DRIVING_STRAIGHT_CHANGING_LANE = _("Changing lanes")
  DRIVING_STRAIGHT_OVERTAKING_ANOTHER_VEHICLE = _("Overtaking another vehicle")
  DRIVING_STRAIGHT_REVERSE = _("Driving reverse")
  DRIVING_STRAIGHT_IN_OPPOSITE_LANE = _("Driving on a lane from opposite direction")

  #CIRCUMSTANCES STEP 3
  DOORS_CLOSED = _("Doors were closed")
  DOORS_OPENED = _("Doors were opened")

  DRIVING_STRAIGHT = _('Driving straight')
  DRIVING_REVERSE = _('Driving reverse')

  TURNING_RIGHT = _('Turning right')
  TURNING_LEFT = _('Turning left')

  VEHICLE_ON_RIGHT = _("On right")
  VEHICLE_ON_LEFT = _("On left")

  CHANGING_DRIVING_LANE_RIGHT = _("Changed lane to right")
  CHANGING_DRIVING_LANE_LEFT = _("Changed lane to left")
  CROSSING_ENTERING_FROM_RIGHT = _("I entered crossing from right relative to the other vehicle")
  CROSSING_NOT_OBEYING_RULES = _("Didn't follow the right-of-way signs or the red light")

  CASCO_INSURANCE_OR_PARKED_VEHICLE = _('Casco insurance/parked vehicle')
  TWO_VEHICLES = _('2 vehicles')
  THREE_OR_MORE_VEHICLES = _('3 or more')


QUESTIONNAIRE = {
  "sections": [
    {
      "id": "starting_questions",
      "name": Section.STARTING_QUESTIONS,
      "state": "empty",
      "starting_step": Step.INJURIES
    },
    {
      "id": "circumstances",
      "name": Section.CIRCUMSTANCES,
      "state": "empty",
      "starting_step": Step.CIRCUMSTANCES_STEP_1
    },
    {
      "id": "vehicle_damage",
      "name": Section.VEHICLE_DAMAGES,
      "state": "empty",
      "starting_step": Step.COLLISION_DIRECTION
    },
    {
      "id": "accident_sketch",
      "name": Section.ACCIDENT_SKETCH,
      "state": "empty",
      "starting_step": Step.ACCIDENT_SKETCH
    },
    {
      "id": "car_and_insurance",
      "name": Section.CAR_AND_INSURANCE,
      "state": "empty",
      "starting_step": Step.REGISTRATION_NUMBER
    },
    {
      "id": "driver",
      "name": Section.DRIVER,
      "state": "empty",
      "starting_step": Step.DRIVER_PERSONAL_DATA
    },
    {
      "id": "additional",
      "name": Section.ADDITIONAL,
      "state": "empty",
      "starting_step": Step.WITNESSES
    }
  ],
  "steps": [
    {
      "step_type": Step.INJURIES,
      "question": str(_('Is there anyone injured and needs medical attention?')),
      "next_step": Step.CAR_DAMAGE,
      "inputs": [1],
    },
    {
      "step_type": Step.CAR_DAMAGE,
      "question": str(_('Major property damage')),
      "next_step": Step.AT_ACCIDENT_PLACE,
      "inputs": [2]
    },
    {
      "step_type": Step.AT_ACCIDENT_PLACE,
      "question": str(_('Are you at the place of the accident?')),
      "inputs": [8]
    },
    {
      "step_type": Step.ACCIDENT_PLACE,
      "question": str(_('The place of the accident')),
      "next_step": Step.ACCIDENT_TIME,
      "inputs": [9],
    },
    {
      "step_type": Step.ACCIDENT_PLACE_TEXT,
      "question": str(_('Write down where it happened')),
      "next_step": Step.ACCIDENT_TIME,
      "inputs": [10],
    },
    {
      "step_type": Step.ACCIDENT_TIME,
      "question": str(_('Time of the accident')),
      "next_step": Step.PARTICIPANTS_NUMBER,
      "inputs": [7],
    },
    {
      "step_type": Step.PARTICIPANTS_NUMBER,
      "question": str(_('Number of participants')),
      "inputs": [4]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_1,
      "question": str(_('Choose option that suits you the best')),
      "inputs": [3]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_2_PARKED,
      "question": str(_('Choose option that suits you the best')),
      "inputs": [5]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_2_MOVING_PARKING_JOINING,
      "question": str(_('Choose option that suits you the best')),
      "inputs": [6]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_2_ROUNDABOUT,
      "question": str(_('Choose option that suits you the best')),
      "inputs": [11]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_2_CROSSING,
      "question": str(_('Choose option that suits you the best')),
      "inputs": [12]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_2_STRAIGHT_ROAD,
      "question": str(_('Choose option that suits you the best')),
      "inputs": [13]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_PARKED_LEAVING_CAR,
      "question": str(_('Choose option that suits you the best')),
      "inputs": [14]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_PARKED_ENTERING_CAR,
      "question": str(_('Choose option that suits you the best')),
      "inputs": [15]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_LEAVING_PARKING,
      "question": str(_('Choose option that suits you the best')),
      "inputs": [16]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_PARKING,
      "question": str(_('Choose option that suits you the best')),
      "inputs": [17]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_LEAVING_PRIVATE_PROPERTY,
      "question": str(_('Choose option that suits you the best')),
      "inputs": [18]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_ENTERING_PRIVATE_PROPERTY,
      "question": str(_('Choose option that suits you the best')),
      "inputs": [19]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_ROUNDABOUT_CRASHED_ANOTHER_LANE,
      "question": str(_('Choose option that suits you the best')),
      "inputs": [20]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_ROUNDABOUT_CHANGING_LANES,
      "question": str(_('Choose option that suits you the best')),
      "inputs": [21]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_CROSSING_DRIVING_STRAIGHT,
      "question": str(_('Choose option that suits you the best')),
      "inputs": [22]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_CROSSING_TURNING_RIGHT,
      "question": str(_('Choose option that suits you the best')),
      "inputs": [23]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_CROSSING_TURNING_LEFT,
      "question": str(_('Choose option that suits you the best')),
      "inputs": [24]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_STRAIGHT_ROAD_SAME_DIRECTION_ANOTHER_LANE,
      "question": str(_('Choose option that suits you the best')),
      "inputs": [25]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_STRAIGHT_ROAD_CHANGING_LANES,
      "question": str(_('Choose option that suits you the best')),
      "inputs": [26]
    },
    {
      "step_type": Step.COLLISION_DIRECTION,
      "question": str(_('Collision direction')),
      "next_step": Step.DAMAGED_PARTS,
      "inputs": [27]
    },
    {
      "step_type": Step.DAMAGED_PARTS,
      "question": str(_('Damaged parts')),
      "inputs": [28]
    },
    {
      "step_type": Step.REGISTRATION_NUMBER,
      "question": str(_('Registration Number')),
      "next_step": Step.REGISTRATION_COUNTRY,
      "inputs": [29],
    },
    {
      "step_type": Step.REGISTRATION_COUNTRY,
      "question": str(_('Registration Country')),
      "next_step": Step.INSURANCE_NAME,
      "inputs": [30],
    },
    {
      "step_type": Step.INSURANCE_NAME,
      "question": str(_('Insurance name')),
      "next_step": Step.INSURANCE_NUMBER,
      "inputs": [31],
    },
    {
      "step_type": Step.INSURANCE_NUMBER,
      "question": str(_('Insurance number')),
      "inputs": [32],
    },
    {
      "step_type": Step.DRIVER_PERSONAL_DATA,
      "question": str(_('For data exchange purposes and contact with your insurance company we need your email and telephone number.')),
      "next_step": Step.DRIVER_DATA,
      "inputs": [33, 34],
    },
    {
      "step_type": Step.WITNESSES,
      "question": str(_('Write down data of anyone who saw the accident?')),
      "inputs": [35],
    },
    {
      "step_type": Step.DRIVER_DATA,
      "question": str(_('Please scan you driving license or choose to input by hand')),
      "inputs": [36],
    },
  ],
  "inputs": [
    {
      "id": 1,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": True,
          "label": Label.CALL_112,
          "action": Action.CALL,
          "action_property": {
            "number": 112
          },
        },
        {
          "value": False,
          "label": Label.WE_ARE_OK,
          "action": Action.NEXT_STEP,
        }
      ]
    },
    {
      "id": 2,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": True,
          "label": Label.YES,
          "action": Action.NEXT_STEP,
        },
        {
          "value": False,
          "label": Label.NO,
          "action": Action.NEXT_STEP,
        }
      ]
    },
    {
      "id": 3,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "parked",
          "label": Label.VEHICLE_PARKED,
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_2_PARKED
          }
        },
        {
          "value": "moving",
          "label": Label.VEHICLE_MOVING,
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_2_MOVING_PARKING_JOINING
          }
        },
        {
          "value": "roundabout",
          "label": Label.VEHICLE_ROUNDABOUT,
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_2_ROUNDABOUT
          }
        },
        {
          "value": "crossing",
          "label": Label.VEHICLE_CROSSING,
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_2_CROSSING
          }
        },
        {
          "value": "driving_straight",
          "label": Label.VEHICLE_DRIVING_STRAIGHT,
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_2_STRAIGHT_ROAD
          }
        }
      ]
    },
    {
      "id": 4,
      "type": "select",
      "required": True,
      "value": None,
      "options": [
        {
          "value": 1,
          "label": Label.CASCO_INSURANCE_OR_PARKED_VEHICLE,
          "action": Action.NEXT_STEP,
        },
        {
          "value": 2,
          "label": Label.TWO_VEHICLES,
          "action": Action.NEXT_STEP,
        },
        {
          "value": 3,
          "label": Label.THREE_OR_MORE_VEHICLES,
          "action": Action.NEXT_STEP,
        },
      ]
    },
    {
      "id": 5,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "leaving_car",
          "label": Label.PARKED_LEAVING_CAR,
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_PARKED_LEAVING_CAR
          }
        },
        {
          "value": "entering_parked_car",
          "label": Label.PARKED_ENTERING_CAR,
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_PARKED_ENTERING_CAR
          }
        },
        {
          "value": "not_in_car",
          "label": Label.PARKED_NOT_BY_THE_CAR,
          "action": Action.NEXT_STEP,
        }
      ]
    },
    {
      "id": 6,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "leaving_parking_slot",
          "label": Label.MOVING_LEAVING_PARKING,
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_PARKED_LEAVING_CAR
          }
        },
        {
          "value": "parking",
          "label": Label.MOVING_PARKING_CAR,
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_PARKED_ENTERING_CAR
          }
        },
        {
          "value": "leaving_parking_slot_private_property",
          "label": Label.MOVING_LEAVING_PRIVATE_PROPERTY,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "entering_parking_slot_private_property",
          "label": Label.MOVING_ENTERING_PRIVATE_PROPERTY,
          "action": Action.NEXT_STEP,
        }
      ]
    },
    {
      "id": 11,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "roundabout_entering",
          "label": Label.ROUNDABOUT_ENTERING,
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_ROUNDABOUT_CRASHED_ANOTHER_LANE
          }
        },
        {
          "value": "roundabout_run_into_vehicle",
          "label": Label.ROUNDABOUT_RUN_INTO_VEHICLE,
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_ROUNDABOUT_CHANGING_LANES
          }
        },
        {
          "value": "roundabout_another_vehicle_crashed_from_behind",
          "label": Label.ROUNDABOUT_ANOTHER_VEHICLE_FROM_BEHIND,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "roundabout_crashed_with_vehicle_from_another_traffic_lane",
          "label": Label.ROUNDABOUT_CRASHED_WITH_VEHICLE_FROM_ANOTHER_TRAFFIC_LANE,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "roundabout_changing_traffic_lane",
          "label": Label.ROUNDABOUT_CHANGING_TRAFFIC_LANE,
          "action": Action.NEXT_STEP,
        }
      ]
    },
    {
      "id": 12,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "crossing_standing_or_traffic_light",
          "label": Label.CROSSING_STANDING_IN_FRONT_OF_CROSSING_OR_TRAFFIC_LIGHT,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "crossing_driving_straight",
          "label": Label.CROSSING_DRIVING_STRAIGHT,
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_CROSSING_DRIVING_STRAIGHT
          }
        },
        {
          "value": "crossing_turning_right",
          "label": Label.CROSSING_TURNING_RIGHT,
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_CROSSING_TURNING_RIGHT
          }
        },
        {
          "value": "crossing_turning_left",
          "label": Label.CROSSING_TURNING_LEFT,
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_CROSSING_TURNING_LEFT
          }
        },
      ]
    },
    {
      "id": 13,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "driving_straight_crashed_with_vehicle_in_front",
          "label": Label.DRIVING_STRAIGHT_CRASHED_WITH_VEHICLE_IN_FRONT,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "driving_straight_crashed_from_behind",
          "label": Label.DRIVING_STRAIGHT_CRASHED_FROM_BEHIND,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "driving_straight_crashed_to_vehicle_in_another_lane",
          "label": Label.DRIVING_STRAIGHT_CRASHED_TO_VEHICLE_IN_ANOTHER_LANE,
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_STRAIGHT_ROAD_SAME_DIRECTION_ANOTHER_LANE
          }
        },
        {
          "value": "driving_straight_changing_lane",
          "label": Label.DRIVING_STRAIGHT_CHANGING_LANE,
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_STRAIGHT_ROAD_CHANGING_LANES
          }
        },
        {
          "value": "driving_straight_overtaking_another_vehicle",
          "label": Label.DRIVING_STRAIGHT_OVERTAKING_ANOTHER_VEHICLE,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "driving_straight_reverse",
          "label": Label.DRIVING_STRAIGHT_REVERSE,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "driving_straight_in_opposite_lane",
          "label": Label.DRIVING_STRAIGHT_IN_OPPOSITE_LANE,
          "action": Action.NEXT_STEP,
        },
      ]
    },
    {
      "id": 14,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "parked_leaving_car_doors_closed",
          "label": Label.DOORS_CLOSED,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "parked_leaving_car_doors_opened",
          "label": Label.DOORS_OPENED,
          "action": Action.NEXT_STEP,
        },
      ]
    },
    {
      "id": 15,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "parked_entering_car_doors_closed",
          "label": Label.DOORS_CLOSED,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "parked_entering_car_doors_opened",
          "label": Label.DOORS_OPENED,
          "action": Action.NEXT_STEP,
        },
      ]
    },
    {
      "id": 16,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "driving_straight",
          "label": Label.DRIVING_STRAIGHT,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "driving_reverse",
          "label": Label.DRIVING_REVERSE,
          "action": Action.NEXT_STEP,
        },
      ]
    },
    {
      "id": 17,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "driving_straight",
          "label": Label.DRIVING_STRAIGHT,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "driving_reverse",
          "label": Label.DRIVING_REVERSE,
          "action": Action.NEXT_STEP,
        },
      ]
    },
    {
      "id": 18,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "driving_straight",
          "label": Label.DRIVING_STRAIGHT,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "driving_reverse",
          "label": Label.DRIVING_REVERSE,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "turning_left",
          "label": Label.TURNING_LEFT,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "turning_right",
          "label": Label.TURNING_RIGHT,
          "action": Action.NEXT_STEP,
        },
      ]
    },
    {
      "id": 19,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "driving_straight",
          "label": Label.DRIVING_STRAIGHT,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "driving_reverse",
          "label": Label.DRIVING_REVERSE,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "turning_left",
          "label": Label.TURNING_LEFT,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "turning_right",
          "label": Label.TURNING_RIGHT,
          "action": Action.NEXT_STEP,
        },
      ]
    },
    {
      "id": 20,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "vehicle_on_right",
          "label": Label.VEHICLE_ON_RIGHT,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "vehicle_on_left",
          "label": Label.VEHICLE_ON_LEFT,
          "action": Action.NEXT_STEP,
        },
      ]
    },
    {
      "id": 21,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "changing_driving_lane_right",
          "label": Label.CHANGING_DRIVING_LANE_RIGHT,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "changing_driving_lane_left",
          "label": Label.CHANGING_DRIVING_LANE_LEFT,
          "action": Action.NEXT_STEP,
        },
      ]
    },
    {
      "id": 22,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "crossing_entering_from_right",
          "label": Label.CROSSING_ENTERING_FROM_RIGHT,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "crossing_not_obeying_rules",
          "label": Label.CROSSING_NOT_OBEYING_RULES,
          "action": Action.NEXT_STEP,
        },
      ]
    },
    {
      "id": 23,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "crossing_entering_from_right",
          "label": Label.CROSSING_ENTERING_FROM_RIGHT,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "crossing_not_obeying_rules",
          "label": Label.CROSSING_NOT_OBEYING_RULES,
          "action": Action.NEXT_STEP,
        },
      ]
    },
    {
      "id": 24,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "crossing_entering_from_right",
          "label": Label.CROSSING_ENTERING_FROM_RIGHT,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "crossing_not_obeying_rules",
          "label": Label.CROSSING_NOT_OBEYING_RULES,
          "action": Action.NEXT_STEP,
        },
      ]
    },

    {
      "id": 25,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "vehicle_on_right",
          "label": Label.VEHICLE_ON_RIGHT,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "vehicle_on_left",
          "label": Label.VEHICLE_ON_LEFT,
          "action": Action.NEXT_STEP,
        },
      ]
    },
    {
      "id": 26,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "changing_driving_lane_right",
          "label": Label.CHANGING_DRIVING_LANE_RIGHT,
          "action": Action.NEXT_STEP,
        },
        {
          "value": "changing_driving_lane_left",
          "label": Label.CHANGING_DRIVING_LANE_LEFT,
          "action": Action.NEXT_STEP,
        },
      ]
    },
    {
      "id": 7,
      "type": "datetime",
      "value": None,
      "required": True
    },
    {
      "id": 8,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": True,
          "label": Label.YES,
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.ACCIDENT_PLACE
          }
        },
        {
          "value": False,
          "label": Label.NO,
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.ACCIDENT_PLACE_TEXT
          }
        }
      ]
    },
    {
      "id": 9,
      "type": "place",
      "value": None,
      "required": True
    },
    {
      "id": 10,
      "type": "text",
      "placeholder": PlaceHolder.STREET,
      "value": None,
      "required": True
    },
    {
      "id": 27,
      "type": "collision_direction",
      "value": None,
      "required": True
    },
    {
      "id": 28,
      "type": "damaged_parts",
      "value": None,
      "required": True
    },
    {
      "id": 29,
      "type": "text",
      "label": _("Registration number"),
      "value": None,
      "required": True
    },
    {
      "id": 30,
      "type": "country_picker",
      "value": None,
      "required": True
    },
    {
      "id": 31,
      "type": "insurance_picker",
      "options": sorted(supported_insurances, key=lambda d: d['label']) ,
      "value": None,
      "required": True
    },
    {
      "id": 32,
      "type": "text",
      "label": _("Insurance number"),
      "value": None,
      "required": True
    },
    {
      "id": 33,
      "type": "text",
      "label": str(_("Email address")),
      "input_type": "email",
      "value": None,
      "required": True
    },
    {
      "id": 34,
      "type": "phone_picker",
      "label": str(_("Phone number")),
      "value": None,
      "required": True
    },
    {
      "id": 35,
      "type": "textarea",
      "label": str(_("Witnesses")),
      "value": None,
      "required": True
    },
    {
      "id": 36,
      "type": "driving_license",
      "value": None,
      "required": True
    },
  ]
}
