import pytest

from race_predictor.prediction import predict_race_time


def test_riegel_predicts_10k_from_5k_performance() -> None:
    predicted_seconds = predict_race_time(
        known_distance_m=5000.0,
        known_time_seconds=1200.0,
        target_distance_m=10000.0,
    )

    assert predicted_seconds == pytest.approx(2501.92, abs=0.01)


def test_riegel_rejects_nonpositive_known_distance() -> None:
    with pytest.raises(ValueError, match="known_distance_m must be positive"):
        predict_race_time(
            known_distance_m=0.0,
            known_time_seconds=1200.0,
            target_distance_m=10000.0,
        )


def test_riegel_supports_custom_fatigue_exponent() -> None:
    predicted_seconds = predict_race_time(
        known_distance_m=5000.0,
        known_time_seconds=1200.0,
        target_distance_m=10000.0,
        fatigue_exponent=1.0,
    )

    assert predicted_seconds == pytest.approx(2400.0)


@pytest.mark.parametrize(
    ("known_time_seconds", "target_distance_m", "fatigue_exponent", "message"),
    [
        (0.0, 10000.0, 1.06, "known_time_seconds must be positive"),
        (1200.0, 0.0, 1.06, "target_distance_m must be positive"),
        (1200.0, 10000.0, 0.0, "fatigue_exponent must be positive"),
    ],
)
def test_riegel_rejects_nonpositive_inputs(
    known_time_seconds: float,
    target_distance_m: float,
    fatigue_exponent: float,
    message: str,
) -> None:
    with pytest.raises(ValueError, match=message):
        predict_race_time(
            known_distance_m=5000.0,
            known_time_seconds=known_time_seconds,
            target_distance_m=target_distance_m,
            fatigue_exponent=fatigue_exponent,
        )
