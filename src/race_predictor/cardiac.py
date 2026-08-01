def calculate_efficiency_factor(
    gap_seconds_per_km: float,
    heart_rate_bpm: int,
) -> float:
    if gap_seconds_per_km <= 0:
        raise ValueError("gap_seconds_per_km must be positive")
    if heart_rate_bpm <= 0:
        raise ValueError("heart_rate_bpm must be positive")
    gap_speed_m_per_s = 1000 / gap_seconds_per_km

    return gap_speed_m_per_s / heart_rate_bpm


def calculate_cardiac_drift(
    first_half_efficiency: float,
    second_half_efficiency: float,
) -> float:
    if first_half_efficiency <= 0:
        raise ValueError("first_half_efficiency must be positive")
    return (first_half_efficiency - second_half_efficiency) / first_half_efficiency * 100
