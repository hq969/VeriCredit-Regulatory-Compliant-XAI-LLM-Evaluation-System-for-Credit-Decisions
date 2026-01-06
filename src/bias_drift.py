def bias_drift(current_bias, baseline_bias):
    return round(abs(current_bias - baseline_bias), 2)
