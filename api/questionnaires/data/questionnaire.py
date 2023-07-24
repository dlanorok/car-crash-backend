from enum import Enum


class Step(str, Enum):
  INJURIES = "injuries"
  CAR_DAMAGE = "car_damage"
  PARTICIPANTS_NUMBER = "participants_number"
  CIRCUMSTANCES_STEP_1 = "circumstances_step_1"
  CIRCUMSTANCES_STEP_2_PARKED = "circumstances_step_2_parked"
  CIRCUMSTANCES_STEP_2_MOVING_PARKING_JOINING = "circumstances_step_2_moving_parking_joining"

class Action(str, Enum):
  CALL = 'call',
  NEXT_STEP = 'next_step'

QUESTIONNAIRE = {
  "sections": [
    {
      "id": "starting_questions",
      "name": "Uvodna vprašanja",
      "state": "empty",
      "starting_step": Step.INJURIES
    },
    {
      "id": "starting_questions",
      "name": "Okoliščene nesreče",
      "state": "empty",
      "starting_step": Step.CIRCUMSTANCES_STEP_1
    }
  ],
  "steps": [
    {
      "step_type": Step.INJURIES,
      "question": "Ali je med udeleženci nesreče kakšna oseba poškodovana in rabi medicinsko pomoč",
      "next_step": Step.CAR_DAMAGE,
      "input": 1,
    },
    {
      "step_type": Step.PARTICIPANTS_NUMBER,
      "question": "Koliko udeležencev",
      "input": 4
    },
    {
      "step_type": Step.CAR_DAMAGE,
      "question": "Any car damage?",
      "input": 2
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_1,
      "question": "Izberi",
      "input": 3
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_2_PARKED,
      "question": "Izberi",
      "input": 5
    },
    {
      "step_type": Step.CIRCUMSTANCES_STEP_2_MOVING_PARKING_JOINING,
      "question": "Izberi",
      "input": 6
    }
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
          "label": "Da, kliče 112",
          "action": Action.CALL,
          "action_property": {
            "number": 112
          }
        },
        {
          "value": False,
          "label": "Ne hvala, smo ok",
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.CAR_DAMAGE
          }
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
          "label": "Da",
          "action": Action.NEXT_STEP,
        },
        {
          "value": False,
          "label": "Ne",
          "action": Action.NEXT_STEP,
        }
      ]
    },
    {
      "id": 3,
      "type": "select",
      "value": None,
      "required": True,
      "conditional_state": True,
      "options": [
        {
          "value": "parked",
          "label": "Moje vozilo je bilo prakirano",
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_2_PARKED
          }
        },
        {
          "value": "moving",
          "label": "Premikal sem vozilo pri prakiranju ali vključevanju v promet",
          "action": Action.NEXT_STEP,
          "action_property": {
            "step": Step.CIRCUMSTANCES_STEP_2_MOVING_PARKING_JOINING
          }
        },
        {
          "value": "roundabout",
          "label": "Vozil sem v krožišču"
        },
        {
          "value": "crossing",
          "label": "Vozil sem v križišču"
        },
        {
          "value": "driving_straight",
          "label": "Vozil sem po ravni cesti"
        }
      ]
    },
    {
      "id": 4,
      "type": "number",
      "required": True,
      "value": None
    },
    {
      "id": 5,
      "type": "select",
      "value": None,
      "required": True,
      "options": [
        {
          "value": "leaving_car",
          "label": "Zapuščal sem vozilo"
        },
        {
          "value": "entering_parked_car",
          "label": "Vstopal sem v parkirano vozilo",
        },
        {
          "value": "not_in_car",
          "label": "Ni me bilo v vozilu"
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
          "label": "Zapuščal sem parkirni prostor"
        },
        {
          "value": "parking",
          "label": "Parkiral sem na parkirni prostor"
        },
        {
          "value": "leaving_parking_slot_private_property",
          "label": "Z vozilom sem zapuščal parkirišče, zasebno zemljišče ali poljsko pot"
        },
        {
          "value": "entering_parking_slot_private_property",
          "label": "Z vozilom sem se zavijal na parkirišče, zasebno zemljišče ali poljsko pot"
        }
      ]
    }
  ]
}
