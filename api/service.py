from src.compliance import compliance_check
from src.faithfulness import faithfulness_score
from src.bias_drift import bias_drift

def evaluate_credit_api(payload):
    faith = payload["faithfulness_score"]
    bias = payload["bias_deviation_index"]
    compliance = payload["compliance_violation"]

    final_score = round(
        (faith * 0.5) +
        ((1 - bias) * 0.3) +
        ((1 - compliance) * 0.2), 2
    )

    status = "APPROVED"
    if final_score < 0.7:
        status = "REVIEW_REQUIRED"

    return final_score, status
