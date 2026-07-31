from dataclasses import dataclass


@dataclass(frozen=True)
class ActivityPoint:
    elapsed_seconds: float
    distance_m: float
    elevation_m: float
    heart_rate_bpm: int | None = None