from race_predictor.models import ActivityPoint


def calculate_grade(start: ActivityPoint, end: ActivityPoint) -> float:
    distance_change = end.distance_m - start.distance_m
    if distance_change <= 0:
        raise ValueError("segment distance must be positive")
    elevation_change = end.elevation_m - start.elevation_m

    return elevation_change / distance_change
