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
