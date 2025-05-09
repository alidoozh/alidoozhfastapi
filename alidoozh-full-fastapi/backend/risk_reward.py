def calculate_risk_reward(entry, target, stop):
    return round((target - entry) / (entry - stop), 2)