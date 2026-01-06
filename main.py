import pandas as pd
from src.train_model import train_model
from src.explain_model import shap_explanation
from src.llm_explainer import generate_llm_explanation
from src.faithfulness import faithfulness_score
from src.bias import bias_deviation
from src.compliance import compliance_check
from src.stability import stability_score
from src.evaluator import evaluate
from src.audit_logger import log_audit

model, X = train_model()
df = pd.read_csv("data/credit_data.csv")

index = 0
decision = df.loc[index, "approved"]
features = X.iloc[index].to_dict()

shap_vals = shap_explanation(model, X, index)

llm_explanations = [
    generate_llm_explanation(features, decision)
    for _ in range(3)
]

faith = faithfulness_score(shap_vals, llm_explanations[0])
bias = bias_deviation(df)
compliance = compliance_check(llm_explanations[0])
stability = stability_score(llm_explanations)

results = evaluate(
    shap_vals,
    llm_explanations,
    faith,
    bias,
    compliance,
    stability
)

log_audit(results)

pd.DataFrame([results]).to_csv(
    "reports/compliance_report.csv", index=False
)

print("Credit AI Evaluation Completed.")
