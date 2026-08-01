import pytest

from race_predictor.gap import calculate_grade_adjusted_pace
from race_predictor.models import ActivityPoint


def test_grade_adjusted_pace_matches_actual_pace_on_flat_ground() -> None:
    start = ActivityPoint(
        elapsed_seconds=0.0,
        distance_m=0.0,
        elevation_m=181.5,
    )
    end = ActivityPoint(
        elapsed_seconds=300.0,
        distance_m=1000.0,
        elevation_m=181.5,
    )

    assert calculate_grade_adjusted_pace(start, end) == pytest.approx(300.0)


def test_grade_adjusted_pace_is_faster_than_actual_pace_on_uphill() -> None:
    start = ActivityPoint(
        elapsed_seconds=0.0,
        distance_m=0.0,
        elevation_m=181.5,
    )
    end = ActivityPoint(
        elapsed_seconds=300.0,
        distance_m=1000.0,
        elevation_m=281.5,
    )

    gap = calculate_grade_adjusted_pace(start, end)

    assert gap == pytest.approx(180.96, abs=0.01)


def test_grade_adjusted_pace_rejects_nonpositive_elapsed_time() -> None:
    start = ActivityPoint(
        elapsed_seconds=60.0,
        distance_m=0.0,
        elevation_m=181.5,
    )
    end = ActivityPoint(
        elapsed_seconds=60.0,
        distance_m=250.0,
        elevation_m=185.0,
    )

    with pytest.raises(ValueError, match="segment elapsed time must be positive"):
        calculate_grade_adjusted_pace(start, end)


def test_grade_adjusted_pace_rejects_zero_distance_segment() -> None:
    start = ActivityPoint(
        elapsed_seconds=0.0,
        distance_m=0.0,
        elevation_m=181.5,
    )
    end = ActivityPoint(
        elapsed_seconds=300.0,
        distance_m=0.0,
        elevation_m=181.5,
    )

    with pytest.raises(ValueError, match="segment distance must be positive"):
        calculate_grade_adjusted_pace(start, end)
