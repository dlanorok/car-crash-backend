from enum import Enum

from django.utils.translation import ugettext_lazy as _


class DrivingStraightAnotherLaneLabel(str, Enum):
    DRIVING_STRAIGHT_ANOTHER_LANE = _('I was driving in the oncoming traffic lane')


section = {
    "value": "driving_straight_another_lane",
    "label": DrivingStraightAnotherLaneLabel.DRIVING_STRAIGHT_ANOTHER_LANE
}

steps = [
]

inputs = {
}
