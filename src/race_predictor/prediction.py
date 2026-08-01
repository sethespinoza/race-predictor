from math import pow

DEFAULT_FATIGUE_EXPONENT = 1.06


def predict_race_time(
    known_distance_m: float,
    known_time_seconds: float,
    target_distance_m: float,
    fatigue_exponent: float = DEFAULT_FATIGUE_EXPONENT,
) -> float:
    if known_distance_m <= 0:
        raise ValueError("known_distance_m must be positive")
    if known_time_seconds <= 0:
        raise ValueError("known_time_seconds must be positive")
    if target_distance_m <= 0:
        raise ValueError("target_distance_m must be positive")
    if fatigue_exponent <= 0:
        raise ValueError("fatigue_exponent must be positive")
    distance_ratio = target_distance_m / known_distance_m

    return known_time_seconds * pow(distance_ratio, fatigue_exponent)
