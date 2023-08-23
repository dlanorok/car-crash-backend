from api.common.enums import Enum


class ArrowType(Enum):
    NULL = "null"
    STRAIGHT = "straight"
    REVERSE = "reverse"
    RIGHT = "right"
    LEFT = "left"
    STRAIGHT_RIGHT = "straight_right"
    STRAIGHT_LEFT = "straight_left"

def circumstance_input_to_arrow(input_value):
    if input_value in ["parked", "crossing_standing_or_traffic_light"]:
        return ArrowType.NULL

    if input_value in [
        "driving_straight"
        "roundabout_run_into_vehicle",
        "roundabout_another_vehicle_crashed_from_behind",
        "roundabout_crashed_with_vehicle_from_another_traffic_lane",
        "crossing_driving_straight",
        "driving_straight_crashed_with_vehicle_in_front",
        "driving_straight_crashed_from_behind"
        "driving_straight_crashed_to_vehicle_in_another_lane",
        "driving_straight_overtaking_another_vehicle",
        "driving_straight_in_opposite_lane"
    ]:
        return ArrowType.STRAIGHT

    if input_value in ["driving_reverse"]:
        return ArrowType.REVERSE

    if input_value in ["turning_left", "crossing_turning_left"]:
        return ArrowType.LEFT

    if input_value in ["turning_right", "roundabout_entering", "crossing_turning_right"]:
        return ArrowType.RIGHT

    if input_value == "changing_driving_lane_right":
        return ArrowType.STRAIGHT_RIGHT
    if input_value == "changing_driving_lane_left":
        return ArrowType.STRAIGHT_LEFT


def generate_circumstance_map(questionnaire):
    circumstance_dict_map = {}
    for input_id, value in questionnaire.get("inputs", {}).items():
        options = value.get("options", None)
        if not options:
            continue

        circumstance_dict_map[input_id] = []

        step_types = []
        for option in options:
            action_property = option.get("action_property", {}).get("step")
            if action_property:
                step_types.append(action_property)


        if not step_types:
            continue

        steps = list(filter(lambda step: step.get("step_type") in step_types, questionnaire.get("steps", [])))

        input_steps = []
        for step in steps:
            for _input in step.get("inputs"):
                input_steps.append(_input)

        circumstance_dict_map[input_id] = input_steps

    return circumstance_dict_map
