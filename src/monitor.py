from src.metrics_store import store_metrics
from src.data_drift import psi
from src.explanation_drift import explanation_drift
from src.bias_drift import bias_drift
from src.compliance_thresholds import check_thresholds
from src.alerts import send_alert

def monitor(
    baseline,
    current,
    baseline_expl,
    current_expl,
    baseline_bias,
    current_bias
):
    drift_metrics = {
        "psi": psi(baseline, current),
        "explanation_drift": explanation_drift(
            baseline_expl, current_expl
        ),
        "bias_drift": bias_drift(current_bias, baseline_bias)
    }

    store_metrics(drift_metrics)

    alerts = check_thresholds(drift_metrics)
    send_alert(alerts)

    return drift_metrics
