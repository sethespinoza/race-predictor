import pytest

from race_predictor.models import ActivityPoint
from race_predictor.segments import calculate_grade


def test_calculate_grade_for_an_uphill_segment() -> None:
    start = ActivityPoint(
        elapsed_seconds=0.0,
        distance_m=0.0,
        elevation_m=181.5,
    )
    end = ActivityPoint(
        elapsed_seconds=60.0,
        distance_m=250.0,
        elevation_m=185.0,
    )

    assert calculate_grade(start, end) == pytest.approx(0.014)


def test_calculate_grade_rejects_zero_distance_segment() -> None:
    start = ActivityPoint(
        elapsed_seconds=0.0,
        distance_m=0.0,
        elevation_m=181.5,
    )
    end = ActivityPoint(
        elapsed_seconds=60.0,
        distance_m=0.0,
        elevation_m=185.0,
    )

    with pytest.raises(ValueError, match="segment distance must be positive"):
        calculate_grade(start, end)
