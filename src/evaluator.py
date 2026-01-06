def evaluate(
    shap_vals,
    llm_explanations,
    faithfulness,
    bias,
    compliance,
    stability
):
    return {
        "faithfulness_score": faithfulness,
        "bias_deviation_index": bias,
        "compliance_violation": compliance,
        "stability_score": stability,
        "final_risk_score": round(
            (faithfulness * 0.4) +
            ((1 - bias) * 0.3) +
            ((1 - compliance) * 0.2) +
            (stability * 0.1), 2
        )
    }
