from race_predictor.models import ActivityPoint


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