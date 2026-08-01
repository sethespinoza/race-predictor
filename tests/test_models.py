import pytest

from race_predictor.models import Activity, ActivityPoint


def test_activity_point_stores_measurements() -> None:
    point = ActivityPoint(
        elapsed_seconds=60.0,
        distance_m=250.0,
        elevation_m=181.5,
        heart_rate_bpm=145,
    )

    assert point.elapsed_seconds == 60.0
    assert point.distance_m == 250.0
    assert point.elevation_m == 181.5
    assert point.heart_rate_bpm == 145


def test_activity_point_allows_missing_heart_rate() -> None:
    point = ActivityPoint(
        elapsed_seconds=60.0,
        distance_m=250.0,
        elevation_m=181.5,
    )

    assert point.heart_rate_bpm is None


def test_activity_point_rejects_negative_elapsed_time() -> None:
    with pytest.raises(ValueError, match="elapsed_seconds must be non-negative"):
        ActivityPoint(
            elapsed_seconds=-1.0,
            distance_m=250.0,
            elevation_m=181.5,
        )


def test_activity_point_rejects_negative_distance() -> None:
    with pytest.raises(ValueError, match="distance_m must be non-negative"):
        ActivityPoint(
            elapsed_seconds=60.0,
            distance_m=-1.0,
            elevation_m=181.5,
        )


def test_activity_requires_at_least_two_points() -> None:
    point = ActivityPoint(
        elapsed_seconds=0.0,
        distance_m=0.0,
        elevation_m=181.5,
    )

    with pytest.raises(ValueError, match="at least two points"):
        Activity(points=(point,))
