def faithfulness_score(shap_values, llm_text):
    matched = 0
    for feature in shap_values:
        if feature.lower() in llm_text.lower():
            matched += 1

    return round(matched / len(shap_values), 2)
