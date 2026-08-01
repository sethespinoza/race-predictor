import pytest

from race_predictor.gap import (
    calculate_activity_grade_adjusted_pace,
    calculate_grade_adjusted_pace,
)
from race_predictor.models import Activity, ActivityPoint


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


def test_activity_gap_matches_actual_pace_for_flat_activity() -> None:
    activity = Activity(
        points=(
            ActivityPoint(
                elapsed_seconds=0.0,
                distance_m=0.0,
                elevation_m=181.5,
            ),
            ActivityPoint(
                elapsed_seconds=150.0,
                distance_m=500.0,
                elevation_m=181.5,
            ),
            ActivityPoint(
                elapsed_seconds=300.0,
                distance_m=1000.0,
                elevation_m=181.5,
            ),
        )
    )

    assert calculate_activity_grade_adjusted_pace(activity) == pytest.approx(300.0)


def test_activity_gap_accounts_for_mixed_terrain() -> None:
    activity = Activity(
        points=(
            ActivityPoint(
                elapsed_seconds=0.0,
                distance_m=0.0,
                elevation_m=181.5,
            ),
            ActivityPoint(
                elapsed_seconds=150.0,
                distance_m=500.0,
                elevation_m=181.5,
            ),
            ActivityPoint(
                elapsed_seconds=300.0,
                distance_m=1000.0,
                elevation_m=231.5,
            ),
        )
    )

    assert calculate_activity_grade_adjusted_pace(activity) == pytest.approx(
        240.48,
        abs=0.01,
    )
