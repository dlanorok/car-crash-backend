from dataclasses import dataclass
from enum import Enum

from django.utils.translation import ugettext_lazy as _
from geopy.geocoders import Nominatim

from api.questionnaires.data.circumstances.crossing import crossing_questionnaire
from api.questionnaires.data.circumstances.driving_straight import driving_straight_questionnaire
from api.questionnaires.data.circumstances.driving_straight_another_lane import \
  driving_straight_another_lane_questionnaire
from api.questionnaires.data.circumstances.moving import moving_questionnaire
from api.questionnaires.data.circumstances.roundabout import roundabout_questionnaire
from api.questionnaires.data.helpers import generate_circumstance_map
from api.questionnaires.data.insurances import supported_insurances
from api.questionnaires.data.circumstances.parked import parked_questionnaire


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
      "question": '',
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
      "inputs": ["32", "41", "53", "42", "50", "46"],
    },
    {
      "step_type": Step.INSURANCE_HOLDER_DATA,
      "question": str(_('Write down insurance holder data')),
      "help_text": str(_('Help text about insurance holder data')),
      "inputs": ["43", "54", "44", "48", "45"],
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
        parked_questionnaire.section,
        moving_questionnaire.section,
        roundabout_questionnaire.section,
        crossing_questionnaire.section,
        driving_straight_questionnaire.section,
        driving_straight_another_lane_questionnaire.section,
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
      "after_months": 12,
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
    "54": {
      "id": 54,
      "type": "text",
      "label": str(_("Insurance holder Surname")),
      "value": None,
      "required": True
    },
    "44": {
      "id": 44,
      "type": "textarea",
      "rows": 3,
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
    "53": {
      "id": 53,
      "type": "date",
      "label": str(_("Validity from")),
      "value": None,
    },
  }
}

QUESTIONNAIRE['steps'] = QUESTIONNAIRE['steps'] \
                         + parked_questionnaire.steps \
                         + moving_questionnaire.steps \
                         + roundabout_questionnaire.steps \
                         + crossing_questionnaire.steps \
                         + driving_straight_questionnaire.steps
QUESTIONNAIRE.get('inputs', {}).update(parked_questionnaire.inputs)
QUESTIONNAIRE.get('inputs', {}).update(moving_questionnaire.inputs)
QUESTIONNAIRE.get('inputs', {}).update(roundabout_questionnaire.inputs)
QUESTIONNAIRE.get('inputs', {}).update(crossing_questionnaire.inputs)
QUESTIONNAIRE.get('inputs', {}).update(driving_straight_questionnaire.inputs)

QUESTIONNAIRE_MAP = generate_circumstance_map(QUESTIONNAIRE)
