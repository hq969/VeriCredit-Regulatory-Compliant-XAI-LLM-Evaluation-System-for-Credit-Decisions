import shap

def shap_explanation(model, X, index=0):
    explainer = shap.Explainer(model, X)
    shap_values = explainer(X)

    explanation = dict(
        zip(X.columns, shap_values[index].values)
    )

    return explanation
