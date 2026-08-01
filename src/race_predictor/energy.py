def running_energy_cost(grade: float) -> float:
    if not -0.45 <= grade <= 0.45:
        raise ValueError("grade must be between -0.45 and 0.45")
    return (
        155.4 * grade**5 - 30.4 * grade**4 - 43.3 * grade**3 + 46.3 * grade**2 + 19.5 * grade + 3.6
    )
