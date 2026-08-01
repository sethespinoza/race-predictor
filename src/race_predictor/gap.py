from race_predictor.energy import running_energy_cost
from race_predictor.models import ActivityPoint
from race_predictor.segments import calculate_grade


def calculate_grade_adjusted_pace(start: ActivityPoint, end: ActivityPoint) -> float:
    elapsed_time = end.elapsed_seconds - start.elapsed_seconds
    if elapsed_time <= 0:
        raise ValueError("segment elapsed time must be positive")
    grade = calculate_grade(start, end)
    distance = end.distance_m - start.distance_m
    actual_pace = elapsed_time / distance * 1000

    flat_cost = running_energy_cost(0.0)
    grade_cost = running_energy_cost(grade)

    return actual_pace * flat_cost / grade_cost
