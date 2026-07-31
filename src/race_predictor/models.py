from dataclasses import dataclass


@dataclass(frozen=True)
class ActivityPoint:
    elapsed_seconds: float
    distance_m: float
    elevation_m: float
    heart_rate_bpm: int | None = None

    def __post_init__(self) -> None:
        if self.elapsed_seconds < 0:
            raise ValueError("elapsed_seconds must be non-negative")
        if self.distance_m < 0:
            raise ValueError("distance_m must be non-negative")