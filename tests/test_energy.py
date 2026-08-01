import pytest

from race_predictor.energy import running_energy_cost


def test_running_energy_cost_matches_flat_ground_baseline() -> None:
    assert running_energy_cost(0.0) == pytest.approx(3.6)


def test_running_energy_cost_increases_on_uphill_grade() -> None:
    assert running_energy_cost(0.10) == pytest.approx(5.968214)


def test_running_energy_cost_decreases_on_moderate_downhill_grade() -> None:
    assert running_energy_cost(-0.10) == pytest.approx(2.151706)


def test_running_energy_cost_rejects_grade_outside_model_range() -> None:
    with pytest.raises(ValueError, match="grade must be between -0.45 and 0.45"):
        running_energy_cost(0.46)
