import pytest

from race_predictor.cardiac import calculate_cardiac_drift, calculate_efficiency_factor


def test_efficiency_factor_uses_grade_adjusted_speed_and_heart_rate() -> None:
    efficiency_factor = calculate_efficiency_factor(
        gap_seconds_per_km=300.0,
        heart_rate_bpm=150,
    )

    assert efficiency_factor == pytest.approx(0.022222, abs=0.000001)


def test_efficiency_factor_rejects_nonpositive_gap() -> None:
    with pytest.raises(ValueError, match="gap_seconds_per_km must be positive"):
        calculate_efficiency_factor(
            gap_seconds_per_km=0.0,
            heart_rate_bpm=150,
        )


def test_efficiency_factor_rejects_nonpositive_heart_rate() -> None:
    with pytest.raises(ValueError, match="heart_rate_bpm must be positive"):
        calculate_efficiency_factor(
            gap_seconds_per_km=300.0,
            heart_rate_bpm=0,
        )


def test_cardiac_drift_is_positive_when_efficiency_declines() -> None:
    drift_percent = calculate_cardiac_drift(
        first_half_efficiency=0.020,
        second_half_efficiency=0.019,
    )

    assert drift_percent == pytest.approx(5.0)


def test_cardiac_drift_rejects_nonpositive_first_half_efficiency() -> None:
    with pytest.raises(
        ValueError,
        match="first_half_efficiency must be positive",
    ):
        calculate_cardiac_drift(
            first_half_efficiency=0.0,
            second_half_efficiency=0.019,
        )
