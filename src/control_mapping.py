def control_mapping(results):
    return {
        "SR_11_7_Model_Explainability": results["faithfulness_score"] > 0.7,
        "Fair_Lending_Compliance": results["bias_deviation_index"] < 0.1,
        "Consumer_Protection": results["compliance_violation"] == 0,
        "Model_Stability": results["stability_score"] > 0.8
    }
