THRESHOLDS = {
    "faithfulness_score": 0.7,
    "bias_deviation_index": 0.1,
    "compliance_violation": 0,
    "stability_score": 0.8,
    "psi": 0.25,
    "explanation_drift": 0.3
}

def check_thresholds(metrics):
    alerts = {}
    for k, v in THRESHOLDS.items():
        if k in metrics and metrics[k] < v:
            alerts[k] = metrics[k]
    return alerts
