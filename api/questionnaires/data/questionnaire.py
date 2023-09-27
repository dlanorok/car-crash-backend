from dataclasses import dataclass
from enum import Enum

from django.utils.translation import ugettext_lazy as _
from geopy.geocoders import Nominatim

from api.questionnaires.data.helpers import generate_circumstance_map
from api.questionnaires.data.insurances import supported_insurances


@dataclass
class MarkerPosition:
  lat: float
  lng: float


@dataclass
class Place:
  marker_position: MarkerPosition
  at_place: bool

  def __post_init__(self):
    self.marker_position = MarkerPosition(**self.marker_position)

  def to_presentation(self):
    if self.marker_position.lng:
      geolocator = Nominatim(user_agent="car_crash_assist")
      return str(geolocator.reverse(f"{self.marker_position.lat}, {self.marker_position.lng}"))
    else:
      return self.written_position

@dataclass
class Country(Place):
  def to_presentation(self):
    if self.marker_position.lng:
      geolocator = Nominatim(user_agent="car_crash_assist")
      return geolocator.reverse(f"{self.marker_position.lat}, {self.marker_position.lng}").raw.get("address").get("country")
    else:
      return self.written_position

@dataclass(init=False)
class ConfirmedEditors:
  confirmed_editors: list

  def __init__(self, **kwargs):
    self.confirmed_editors = kwargs.get("confirmed_editors")

  def to_presentation(self):
    return ",".join(self.confirmed_editors)

@dataclass(init=False)
class PhoneNumber:
  number: str
  internationalNumber: str
  nationalNumber: str

  def __init__(self, **kwargs):
    self.number = kwargs.get("number")
    self.internationalNumber = kwargs.get("internationalNumber")
    self.nationalNumber = kwargs.get("nationalNumber")

  def to_presentation(self):
    return self.internationalNumber

class Step(str, Enum):
  INJURIES = "injuries"
  CAR_DAMAGE = "car_damage"
  PROPERTY_DAMAGE = "property_damage"
  ACCIDENT_PLACE = "accident_place"
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

  CAR_DATA = "car_data"
  INSURANCE_NAME = "insurance_name"
  INSURANCE_DATA = 'insurance_data'
  INSURANCE_HOLDER_DATA = 'insurance_holder_data'

  DRIVER_PERSONAL_DATA = 'driver_personal_data'
  DRIVER_DATA = 'driver_data'

  WITNESSES = 'witnesses'
  ADDITIONAL_ACCIDENT_DATA_TEXT = 'additional_accident_data_text'

  CASE_1_VEHICLES = 'case_1_vehicles'
  CASE_3_VEHICLES = 'case_3_vehicles'

  RESPONSIBILITY_CONFIRMATION = "responsibility_confirmation"
  SUMMARY_CONFIRMATION = "summary_confirmation"
  FINAL_CONFIRMATION = "final_confirmation"

  STARTING_STEP_INITIAL_PAGE = "starting_page_initial_page"
  CIRCUMSTANCES_INITIAL_PAGE = "circumstances_initial_page"
  VEHICLE_DAMAGES_INITIAL_PAGE = "vehicle_damages_initial_page"
  ACCIDENT_SKETCH_INITIAL_PAGE = "accident_sketch_initial_page"
  CAR_AND_INSURANCE_INITIAL_PAGE = "car_and_insurance_initial_page"
  DRIVER_INITIAL_PAGE = "driver_initial_page"
  ADDITIONAL_INITIAL_PAGE = "additional_initial_page"
  CONFIRMATION_STEP_INITIAL_PAGE = "confirmation_step_initial_page"

  INVITE = 'invite'


class Action(str, Enum):
  CALL = 'call',
  NEXT_STEP = 'next_step'


class Section(str, Enum):
  STARTING_QUESTIONS = _('Starting questions')
  INVITE = _('Invite')
  CIRCUMSTANCES = _('Circumstances')
  VEHICLE_DAMAGES = _('Vehicle damages')
  ACCIDENT_SKETCH = _('Accident sketch')
  CAR_AND_INSURANCE = _('Car and Insurance data')
  DRIVER = _('Driver')
  ADDITIONAL = _('Additional')
  CONFIRMATION_STEP = _('Confirm')

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

  VEHICLE_ON_RIGHT = _("Other vehicle was on my right")
  VEHICLE_ON_LEFT = _("Other vehicle was on my left")

  CHANGING_DRIVING_LANE_RIGHT = _("Changed lane to right")
  CHANGING_DRIVING_LANE_LEFT = _("Changed lane to left")
  CROSSING_ENTERING_FROM_RIGHT = _("I entered crossing from right relative to the other vehicle")
  CROSSING_NOT_OBEYING_RULES = _("I did (not) follow the right-of-way signs or the red light")

  CASCO_INSURANCE_OR_PARKED_VEHICLE = _('Casco insurance/parked vehicle')
  TWO_VEHICLES = _('2 vehicles')
  THREE_OR_MORE_VEHICLES = _('3 or more')

  ME = _("Me")
  ANOTHER_VEHICLE = _("Other vehicle")
  UNKNOWN = _("I don't know")

class ResponsibilityTypeEnum:
  ME = "ME"
  ANOTHER = "ANOTHER"
  UNKNOWN = "UNKNOWN"
  RESPONSIBILITY_TYPE = [
    (ME, "me"),
    (ANOTHER, "another"),
    (UNKNOWN, "unknown"),
  ]

QUESTIONNAIRE = {
  "car_arrow": "",
  "sections": [
    {
      "id": "starting_questions",
      "name": Section.STARTING_QUESTIONS,
      "state": "empty",
      "starting_step": Step.STARTING_STEP_INITIAL_PAGE
    },
    {
      "id": "invite",
      "name": Section.INVITE,
      "state": "empty",
      "starting_step": Step.INVITE
    },
    {
      "id": "circumstances",
      "name": Section.CIRCUMSTANCES,
      "state": "empty",
      "starting_step": Step.CIRCUMSTANCES_INITIAL_PAGE
    },
    {
      "id": "vehicle_damage",
      "name": Section.VEHICLE_DAMAGES,
      "state": "empty",
      "starting_step": Step.VEHICLE_DAMAGES_INITIAL_PAGE
    },
    {
      "id": "accident_sketch",
      "name": Section.ACCIDENT_SKETCH,
      "state": "empty",
      "starting_step": Step.ACCIDENT_SKETCH_INITIAL_PAGE
    },
    {
      "id": "car_and_insurance",
      "name": Section.CAR_AND_INSURANCE,
      "state": "empty",
      "starting_step": Step.CAR_AND_INSURANCE_INITIAL_PAGE
    },
    {
      "id": "driver",
      "name": Section.DRIVER,
      "state": "empty",
      "starting_step": Step.DRIVER_INITIAL_PAGE
    },
    {
      "id": "additional",
      "name": Section.ADDITIONAL,
      "state": "empty",
      "starting_step": Step.ADDITIONAL_INITIAL_PAGE
    },
    {
      "id": "confirmation",
      "name": Section.CONFIRMATION_STEP,
      "state": "empty",
      "starting_step": Step.CONFIRMATION_STEP_INITIAL_PAGE
    }
  ],
  "steps": [
    {
      "step_type": Step.INVITE,
      "main_screen": True,
      "question": str(_('Let the other participant scan this code to connect with your accident statement form')),
      "help_text": str(_('This is random help text on invite section')),
      "inputs": ["49"],
    },
    {
      "step_type": Step.STARTING_STEP_INITIAL_PAGE,
      "main_screen": True,
      "chapter": True,
      "question": str(_("Let's start")),
      "help_text": str(_('Initial questions right after the accident')),
      "next_step": Step.INJURIES,
      "inputs": [],
    },
    {
      "step_type": Step.CIRCUMSTANCES_INITIAL_PAGE,
      "main_screen": True,
      "chapter": True,
      "question": str(_('Circumstances page chapter')),
      "next_step": Step.CIRCUMSTANCES_STEP_1,
      "inputs": [],
    },
    {
      "step_type": Step.VEHICLE_DAMAGES_INITIAL_PAGE,
      "main_screen": True,
      "chapter": True,
      "question": str(_('Vehicle damage chapter')),
      "next_step": Step.COLLISION_DIRECTION,
      "inputs": [],
    },
    {
      "step_type": Step.ACCIDENT_SKETCH_INITIAL_PAGE,
      "main_screen": True,
      "chapter": True,
      "question": str(_('Sketch page chapter')),
      "next_step": Step.ACCIDENT_SKETCH,
      "inputs": [],
    },
    {
      "step_type": Step.CAR_AND_INSURANCE_INITIAL_PAGE,
      "main_screen": True,
      "chapter": True,
      "question": str(_('Car and Insurance page chapter')),
      "next_step": Step.CAR_DATA,
      "inputs": [],
    },
    {
      "step_type": Step.DRIVER_INITIAL_PAGE,
      "main_screen": True,
      "chapter": True,
      "question": str(_('Driver page chapter')),
      "next_step": Step.DRIVER_DATA,
      "inputs": [],
    },
    {
      "step_type": Step.ADDITIONAL_INITIAL_PAGE,
      "main_screen": True,
      "chapter": True,
      "question": str(_('Additional page chapter')),
      "next_step": Step.WITNESSES,
      "inputs": [],
    },
    {
      "step_type": Step.CONFIRMATION_STEP_INITIAL_PAGE,
      "main_screen": True,
      "chapter": True,
      "question": str(_('Confirmation step chapter')),
      "next_step": Step.RESPONSIBILITY_CONFIRMATION,
      "inputs": [],
    },


    {
      "step_type": Step.INJURIES,
      "question": str(_('Is there anyone injured and needs medical attention?')),
      "help_text": str(_('This is random help text that needs to be changed')),
      "next_step": Step.CAR_DAMAGE,
      "inputs": ["1"],
    },
    {
      "step_type": Step.CAR_DAMAGE,
      "question": str(_('Damage on other vehicles')),
      "help_text": str(_('This is random help text on page Damage on other vehicles section')),
      "next_step": Step.PROPERTY_DAMAGE,
      "inputs": ["2"]
    },
    {
      "step_type": Step.PROPERTY_DAMAGE,
      "question": str(_('Is there any damage on nearby property?')),
      "help_text": str(_('This is random help text on page Is there any damage on nearby property')),
      "next_step": Step.ACCIDENT_PLACE,
      "inputs": ["47"]
    },
    {
      "step_type": Step.ACCIDENT_PLACE,
      "main_screen": True,
      "question": str(_('Choose location')),
      "help_text": str(_('This is random help text on Accident place picker')),
      "next_step": Step.ACCIDENT_TIME,
      "inputs": ["9"],
    },
    {
      "step_type": Step.ACCIDENT_TIME,
      "question": str(_('Time of the accident')),
      "help_text": str(_('This is random help text on Time of accident')),
      "next_step": Step.PARTICIPANTS_NUMBER,
      "inputs": ["7"],
    },
    {
      "step_type": Step.PARTICIPANTS_NUMBER,
      "question": str(_('Number of participants')),
      "help_text": str(_('This is random help text on participant number')),
      "inputs": ["4"]
    },
    {
      "step_type": Step.RESPONSIBILITY_CONFIRMATION,
      "question": str(_('Who is responsible for the accident')),
      "help_text": str(_('Help text about responsibility')),
      "next_step": Step.SUMMARY_CONFIRMATION,
      "inputs": ["38"]
    },
    {
      "step_type": Step.SUMMARY_CONFIRMATION,
      "question": str(_('Povzetek')),
      "next_step": Step.FINAL_CONFIRMATION,
      "main_screen": True,
      "inputs": ["51"]
    },
    {
      "step_type": Step.FINAL_CONFIRMATION,
      "question": str(_('Smo na CILJU')),
      "help_text": str(_('Click on button and complete the flow')),
      "main_screen": True,
      "inputs": ["52"]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_1,
      "question": str(_('Choose option that suits you the best')),
      "help_text": str(_('1')),
      "updated_inputs": ["37"],
      "inputs": ["3"]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_2_PARKED,
      "question": str(_('Choose option that suits you the best')),
      "help_text": str(_('2')),
      "updated_inputs": ["37"],
      "inputs": ["5"]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_2_MOVING_PARKING_JOINING,
      "question": str(_('Choose option that suits you the best')),
      "help_text": str(_('3')),
      "updated_inputs": ["37"],
      "inputs": ["6"]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_2_ROUNDABOUT,
      "question": str(_('Choose option that suits you the best')),
      "help_text": str(_('4')),
      "updated_inputs": ["37"],
      "inputs": ["11"]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_2_CROSSING,
      "question": str(_('Choose option that suits you the best')),
      "help_text": str(_('5')),
      "updated_inputs": ["37"],
      "inputs": ["12"]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_2_STRAIGHT_ROAD,
      "question": str(_('Choose option that suits you the best')),
      "help_text": str(_('6')),
      "updated_inputs": ["37"],
      "inputs": ["13"]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_PARKED_LEAVING_CAR,
      "question": str(_('Choose option that suits you the best')),
      "help_text": str(_('7')),
      "updated_inputs": ["37"],
      "inputs": ["14"]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_PARKED_ENTERING_CAR,
      "question": str(_('Choose option that suits you the best')),
      "help_text": str(_('8')),
      "updated_inputs": ["37"],
      "inputs": ["15"]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_LEAVING_PARKING,
      "question": str(_('Choose option that suits you the best')),
      "help_text": str(_('9')),
      "updated_inputs": ["37"],
      "inputs": ["16"]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_PARKING,
      "question": str(_('Choose option that suits you the best')),
      "help_text": str(_('10')),
      "updated_inputs": ["37"],
      "inputs": ["17"]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_LEAVING_PRIVATE_PROPERTY,
      "question": str(_('Choose option that suits you the best')),
      "help_text": str(_('11')),
      "updated_inputs": ["37"],
      "inputs": ["18"]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_ENTERING_PRIVATE_PROPERTY,
      "question": str(_('Choose option that suits you the best')),
      "help_text": str(_('12')),
      "updated_inputs": ["37"],
      "inputs": ["19"]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_ROUNDABOUT_CRASHED_ANOTHER_LANE,
      "question": str(_('Choose option that suits you the best')),
      "help_text": str(_('13')),
      "updated_inputs": ["37"],
      "inputs": ["20"]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_ROUNDABOUT_CHANGING_LANES,
      "question": str(_('Choose option that suits you the best')),
      "help_text": str(_('14')),
      "updated_inputs": ["37"],
      "inputs": ["21"]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_CROSSING_DRIVING_STRAIGHT,
      "question": str(_('Choose option that suits you the best')),
      "help_text": str(_('15')),
      "updated_inputs": ["37"],
      "inputs": ["22"]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_CROSSING_TURNING_RIGHT,
      "question": str(_('Choose option that suits you the best')),
      "help_text": str(_('16')),
      "updated_inputs": ["37"],
      "inputs": ["23"]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_CROSSING_TURNING_LEFT,
      "question": str(_('Choose option that suits you the best')),
      "help_text": str(_('17')),
      "updated_inputs": ["37"],
      "inputs": ["24"]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_STRAIGHT_ROAD_SAME_DIRECTION_ANOTHER_LANE,
      "question": str(_('Choose option that suits you the best')),
      "help_text": str(_('18')),
      "updated_inputs": ["37"],
      "inputs": ["25"]
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_3_STRAIGHT_ROAD_CHANGING_LANES,
      "question": str(_('Choose option that suits you the best')),
      "help_text": str(_('19')),
      "updated_inputs": ["37"],
      "inputs": ["26"]
    },
    {
      "step_type": Step.COLLISION_DIRECTION,
      "main_screen": True,
      "question": str(_('Choose Collision direction')),
      "next_step": Step.DAMAGED_PARTS,
      "inputs": ["27"]
    },
    {
      "step_type": Step.DAMAGED_PARTS,
      "main_screen": True,
      "question": str(_('Choose damaged parts')),
      "inputs": ["28"]
    },
    {
      "step_type": Step.CAR_DATA,
      "question": str(_('Write down your registration number')),
      "help_text": str(_('Help ext about registration number')),
      "next_step": Step.INSURANCE_NAME,
      "inputs": ["29", "30", "40"],
    },
    {
      "step_type": Step.INSURANCE_NAME,
      "question": str(_('Select your insurance')),
      "help_text": str(_('Help ext about insurance')),
      "next_step": Step.INSURANCE_DATA,
      "inputs": ["31"],
    },
    {
      "step_type": Step.INSURANCE_DATA,
      "question": str(_('Write down insurance data')),
      "help_text": str(_('Help text about insurance data')),
      "next_step": Step.INSURANCE_HOLDER_DATA,
      "inputs": ["32", "41", "42", "50", "46"],
    },
    {
      "step_type": Step.INSURANCE_HOLDER_DATA,
      "question": str(_('Write down insurance holder data')),
      "help_text": str(_('Help text about insurance holder data')),
      "inputs": ["43", "44", "48", "45"],
    },
    {
      "step_type": Step.DRIVER_PERSONAL_DATA,
      "question": str(_('For data exchange purposes and contact with your insurance company we need your email and telephone number.')),
      "help_text": str(_('Information about data exchange step')),
      "inputs": ["33", "34"],
    },
    {
      "step_type": Step.WITNESSES,
      "question": str(_('Write down data of anyone who saw the accident?')),
      "help_text": str(_('Information about witnesses')),
      "next_step": Step.ADDITIONAL_ACCIDENT_DATA_TEXT,
      "inputs": ["35"],
    },
    {
      "step_type": Step.DRIVER_DATA,
      "question": str(_('Please scan you driving license or choose to input by hand')),
      "help_text": str(_('Help text about scan')),
      "next_step": Step.DRIVER_PERSONAL_DATA,
      "inputs": ["36"],
    },
    {
      "step_type": Step.ACCIDENT_SKETCH,
      "main_screen": True,
      "question": str(_('Sketch you accident')),
      "data_from_input": 9,
      "inputs": ["37"],
    },
    {
      "step_type": Step.ADDITIONAL_ACCIDENT_DATA_TEXT,
      "question": str(_('Write down additional data of the accident')),
      "help_text": str(_('Information about additional data of accident')),
      "inputs": ["39"],
    },
    {
      "step_type": Step.CASE_3_VEHICLES,
      "question": str(_('3 vehicles not supported')),
      "help_text": str(_('This is random help text that needs to be changed 3 vehicles')),
      "inputs": [],
    },
    {
      "step_type": Step.CASE_1_VEHICLES,
      "inputs": [],
      "question": str(_('CASCO test')),
      "help_text": str(_('This is random help text that needs to be changed')),
    }
  ],
  "inputs": {
    "1": {
      "id": 1,
      "type": "select",
      "value": None,
      "required": True,
      "shared_input": True,
      "options": [
        {
          "value": True,
          "label": Label.CALL_112,
          "action": Action.CALL,
          "icon": 'car',
          "action_property": {
            "number": 112
          },
        },
        {
          "value": False,
          "label": Label.WE_ARE_OK,
          "icon": 'thumbs-up',
        }
      ]
    },
    "37": {
      "id": 37,
      "shared_input": True,
      "type": "sketch",
      "value": {"cars": [], "confirmed_editors": [], "editing": False},
      "required": True
    },
    "2": {
      "id": 2,
      "type": "select",
      "value": None,
      "required": True,
      "shared_input": True,
      "options": [
        {
          "value": True,
          "label": Label.YES,
          "icon": 'car-broken',
        },
        {
          "value": False,
          "icon": 'car-ok',
          "label": Label.NO,
        }
      ]
    },
    "3": {
      "id": 3,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "parked",
          "label": Label.VEHICLE_PARKED,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_2_PARKED
          }
        },
        {
          "value": "moving",
          "label": Label.VEHICLE_MOVING,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_2_MOVING_PARKING_JOINING
          }
        },
        {
          "value": "roundabout",
          "label": Label.VEHICLE_ROUNDABOUT,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_2_ROUNDABOUT
          }
        },
        {
          "value": "crossing",
          "label": Label.VEHICLE_CROSSING,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_2_CROSSING
          }
        },
        {
          "value": "driving_straight",
          "label": Label.VEHICLE_DRIVING_STRAIGHT,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_2_STRAIGHT_ROAD
          }
        }
      ]
    },
    "4": {
      "id": 4,
      "type": "select",
      "required": True,
      "value": None,
      "shared_input": True,
      "options": [
        {
          "value": 1,
          "label": Label.CASCO_INSURANCE_OR_PARKED_VEHICLE,
          "action_property": {
            "step": Step.CASE_1_VEHICLES
          }
        },
        {
          "value": 2,
          "label": Label.TWO_VEHICLES,
        },
        {
          "value": 3,
          "label": Label.THREE_OR_MORE_VEHICLES,
          "action_property": {
            "step": Step.CASE_3_VEHICLES
          }
        },
      ]
    },
    "5": {
      "id": 5,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "leaving_car",
          "label": Label.PARKED_LEAVING_CAR,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_PARKED_LEAVING_CAR
          }
        },
        {
          "value": "entering_parked_car",
          "label": Label.PARKED_ENTERING_CAR,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_PARKED_ENTERING_CAR
          }
        },
        {
          "value": "not_in_car",
          "label": Label.PARKED_NOT_BY_THE_CAR,
        }
      ]
    },
    "6": {
      "id": 6,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "leaving_parking_slot",
          "label": Label.MOVING_LEAVING_PARKING,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_LEAVING_PARKING
          }
        },
        {
          "value": "parking",
          "label": Label.MOVING_PARKING_CAR,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_PARKING
          }
        },
        {
          "value": "leaving_parking_slot_private_property",
          "label": Label.MOVING_LEAVING_PRIVATE_PROPERTY,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_LEAVING_PRIVATE_PROPERTY
          }
        },
        {
          "value": "entering_parking_slot_private_property",
          "label": Label.MOVING_ENTERING_PRIVATE_PROPERTY,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_ENTERING_PRIVATE_PROPERTY
          }
        }
      ]
    },
    "7": {
      "id": 7,
      "type": "datetime",
      "value": None,
      "required": True,
      "shared_input": True
    },
    "9": {
      "id": 9,
      "type": "place",
      "value": None,
      "required": True,
      "shared_input": True
    },
    "11": {
      "id": 11,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "roundabout_entering",
          "label": Label.ROUNDABOUT_ENTERING,
        },
        {
          "value": "roundabout_run_into_vehicle",
          "label": Label.ROUNDABOUT_RUN_INTO_VEHICLE,
        },
        {
          "value": "roundabout_another_vehicle_crashed_from_behind",
          "label": Label.ROUNDABOUT_ANOTHER_VEHICLE_FROM_BEHIND,
        },
        {
          "value": "roundabout_crashed_with_vehicle_from_another_traffic_lane",
          "label": Label.ROUNDABOUT_CRASHED_WITH_VEHICLE_FROM_ANOTHER_TRAFFIC_LANE,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_ROUNDABOUT_CRASHED_ANOTHER_LANE
          }
        },
        {
          "value": "roundabout_changing_traffic_lane",
          "label": Label.ROUNDABOUT_CHANGING_TRAFFIC_LANE,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_ROUNDABOUT_CHANGING_LANES
          }
        }
      ]
    },
    "12": {
      "id": 12,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "crossing_standing_or_traffic_light",
          "label": Label.CROSSING_STANDING_IN_FRONT_OF_CROSSING_OR_TRAFFIC_LIGHT,
        },
        {
          "value": "crossing_driving_straight",
          "label": Label.CROSSING_DRIVING_STRAIGHT,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_CROSSING_DRIVING_STRAIGHT
          }
        },
        {
          "value": "crossing_turning_right",
          "label": Label.CROSSING_TURNING_RIGHT,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_CROSSING_TURNING_RIGHT
          }
        },
        {
          "value": "crossing_turning_left",
          "label": Label.CROSSING_TURNING_LEFT,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_CROSSING_TURNING_LEFT
          }
        },
      ]
    },
    "13": {
      "id": 13,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "driving_straight_crashed_with_vehicle_in_front",
          "label": Label.DRIVING_STRAIGHT_CRASHED_WITH_VEHICLE_IN_FRONT,
        },
        {
          "value": "driving_straight_crashed_from_behind",
          "label": Label.DRIVING_STRAIGHT_CRASHED_FROM_BEHIND,
        },
        {
          "value": "driving_straight_crashed_to_vehicle_in_another_lane",
          "label": Label.DRIVING_STRAIGHT_CRASHED_TO_VEHICLE_IN_ANOTHER_LANE,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_STRAIGHT_ROAD_SAME_DIRECTION_ANOTHER_LANE
          }
        },
        {
          "value": "driving_straight_changing_lane",
          "label": Label.DRIVING_STRAIGHT_CHANGING_LANE,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_3_STRAIGHT_ROAD_CHANGING_LANES
          }
        },
        {
          "value": "driving_straight_overtaking_another_vehicle",
          "label": Label.DRIVING_STRAIGHT_OVERTAKING_ANOTHER_VEHICLE,
        },
        {
          "value": "driving_reverse",
          "label": Label.DRIVING_STRAIGHT_REVERSE,
        },
        {
          "value": "driving_straight_in_opposite_lane",
          "label": Label.DRIVING_STRAIGHT_IN_OPPOSITE_LANE,
        },
      ]
    },
    "14": {
      "id": 14,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "parked_leaving_car_doors_closed",
          "label": Label.DOORS_CLOSED,
        },
        {
          "value": "parked_leaving_car_doors_opened",
          "label": Label.DOORS_OPENED,
        },
      ]
    },
    "15": {
      "id": 15,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "parked_entering_car_doors_closed",
          "label": Label.DOORS_CLOSED,
        },
        {
          "value": "parked_entering_car_doors_opened",
          "label": Label.DOORS_OPENED,
        },
      ]
    },
    "16": {
      "id": 16,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "driving_straight",
          "label": Label.DRIVING_STRAIGHT,
        },
        {
          "value": "driving_reverse",
          "label": Label.DRIVING_REVERSE,
        },
      ]
    },
    "17": {
      "id": 17,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "driving_straight",
          "label": Label.DRIVING_STRAIGHT,
        },
        {
          "value": "driving_reverse",
          "label": Label.DRIVING_REVERSE,
        },
      ]
    },
    "18": {
      "id": 18,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "driving_straight",
          "label": Label.DRIVING_STRAIGHT,
        },
        {
          "value": "driving_reverse",
          "label": Label.DRIVING_REVERSE,
        },
        {
          "value": "turning_left",
          "label": Label.TURNING_LEFT,
        },
        {
          "value": "turning_right",
          "label": Label.TURNING_RIGHT,
        },
      ]
    },
    "19": {
      "id": 19,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "driving_straight",
          "label": Label.DRIVING_STRAIGHT,
        },
        {
          "value": "driving_reverse",
          "label": Label.DRIVING_REVERSE,
        },
        {
          "value": "turning_left",
          "label": Label.TURNING_LEFT,
        },
        {
          "value": "turning_right",
          "label": Label.TURNING_RIGHT,
        },
      ]
    },
    "20": {
      "id": 20,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "vehicle_on_right",
          "label": Label.VEHICLE_ON_RIGHT,
        },
        {
          "value": "vehicle_on_left",
          "label": Label.VEHICLE_ON_LEFT,
        },
      ]
    },
    "21": {
      "id": 21,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "changing_driving_lane_right",
          "label": Label.CHANGING_DRIVING_LANE_RIGHT,
        },
        {
          "value": "changing_driving_lane_left",
          "label": Label.CHANGING_DRIVING_LANE_LEFT,
        },
      ]
    },
    "22": {
      "id": 22,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "crossing_entering_from_right",
          "label": Label.CROSSING_ENTERING_FROM_RIGHT,
        },
        {
          "value": "crossing_not_obeying_rules",
          "label": Label.CROSSING_NOT_OBEYING_RULES,
        },
      ]
    },
    "23": {
      "id": 23,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "crossing_entering_from_right",
          "label": Label.CROSSING_ENTERING_FROM_RIGHT,
        },
        {
          "value": "crossing_not_obeying_rules",
          "label": Label.CROSSING_NOT_OBEYING_RULES,
        },
      ]
    },
    "24": {
      "id": 24,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "crossing_entering_from_right",
          "label": Label.CROSSING_ENTERING_FROM_RIGHT,
        },
        {
          "value": "crossing_not_obeying_rules",
          "label": Label.CROSSING_NOT_OBEYING_RULES,
        },
      ]
    },
    "25": {
      "id": 25,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "vehicle_on_right",
          "label": Label.VEHICLE_ON_RIGHT,
        },
        {
          "value": "vehicle_on_left",
          "label": Label.VEHICLE_ON_LEFT,
        },
      ]
    },
    "26": {
      "id": 26,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "changing_driving_lane_right",
          "label": Label.CHANGING_DRIVING_LANE_RIGHT,
        },
        {
          "value": "changing_driving_lane_left",
          "label": Label.CHANGING_DRIVING_LANE_LEFT,
        },
      ]
    },
    "27": {
      "id": 27,
      "type": "collision_direction",
      "value": None,
      "required": True
    },
    "28": {
      "id": 28,
      "type": "damaged_parts",
      "value": None,
      "required": True
    },
    "29": {
      "id": 29,
      "type": "text",
      "on_change_action": "capitalize",
      "label": str(_("Registration number")),
      "value": None,
      "required": True
    },
    "30": {
      "id": 30,
      "label": str(_("Country")),
      "type": "country_picker",
      "value": None,
      "required": True
    },
    "31": {
      "id": 31,
      "type": "select",
      "options": sorted(map(lambda insurance: insurance, supported_insurances), key=lambda d: d['label']),
      "value": None,
      "required": True
    },
    "32": {
      "id": 32,
      "type": "text",
      "label": str(_("Insurance number")),
      "value": None,
      "required": True
    },
    "33": {
      "id": 33,
      "type": "text",
      "label": str(_("Email address")),
      "input_type": "email",
      "value": None,
      "required": True
    },
    "34": {
      "id": 34,
      "type": "phone_picker",
      "label": str(_("Phone number")),
      "value": None,
      "required": True
    },
    "35": {
      "id": 35,
      "type": "textarea",
      "label": str(_("Witnesses")),
      "value": None,
    },
    "36": {
      "id": 36,
      "type": "driving_license",
      "value": None,
      "required": True
    },
    "38": {
      "id": 38,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": ResponsibilityTypeEnum.ME,
          "label": Label.ME,
        },
        {
          "value": ResponsibilityTypeEnum.ANOTHER,
          "label": Label.ANOTHER_VEHICLE,
        },
        {
          "value": ResponsibilityTypeEnum.UNKNOWN,
          "label": Label.UNKNOWN,
        },
      ]
    },
    "39": {
      "id": 39,
      "type": "textarea",
      "label": str(_("Additional Data")),
      "value": None,
    },
    "40": {
      "id": 40,
      "type": "text",
      "label": str(_("Vehicle type")),
      "value": None,
      "required": True
    },
    "41": {
      "id": 41,
      "type": "text",
      "label": str(_("Green card number")),
      "value": None,
    },
    "42": {
      "id": 42,
      "type": "date",
      "label": str(_("Validity")),
      "value": None,
      "required": True
    },
    "43": {
      "id": 43,
      "type": "text",
      "label": str(_("Insurance holder Name")),
      "value": None,
      "required": True
    },
    "44": {
      "id": 44,
      "type": "text",
      "label": str(_("Insurance holder Address")),
      "value": None,
      "required": True
    },
    "45": {
      "id": 45,
      "label": str(_("Insurance holder phone")),
      "type": "phone_picker",
      "value": None,
      "required": True
    },
    "46": {
      "id": 46,
      "type": "country_picker",
      "label": str(_("Insurance holder country")),
      "value": None,
      "required": True
    },
    "47": {
      "id": 47,
      "type": "select",
      "value": None,
      "required": True,
      "shared_input": True,
      "options": [
        {
          "value": True,
          "icon": 'crash',
          "label": Label.YES,
        },
        {
          "value": False,
          "icon": 'fill-rect',
          "label": Label.NO,
        }
      ]
    },
    "48": {
      "id": 48,
      "type": "text",
      "input_type": "email",
      "label": str(_("Insurance holder email")),
      "value": None,
      "required": True
    },
    "49": {
      "id": 49,
      "type": "invite",
      "value": None,
    },
    "50": {
      "id": 50,
      "type": "boolean",
      "label": str(_("Damage insured")),
      "required": True,
      "value": None,
    },
    "51": {
      "id": 51,
      "type": "confirmation",
      "required": True,
      "value": None,
    },
    "52": {
      "id": 52,
      "type": "final_step",
      "required": True,
      "value": None,
    },
  }
}

QUESTIONNAIRE_MAP = generate_circumstance_map(QUESTIONNAIRE)
