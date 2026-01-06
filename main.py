import pandas as pd
from src.train_model import train_model
from src.explain_model import shap_explanation
from src.llm_explainer import generate_llm_explanation
from src.faithfulness import faithfulness_score
from src.bias import bias_deviation
from src.compliance import compliance_check
from src.stability import stability_score
from src.human_agreement import human_ai_agreement
from src.rag_grounding import grounding_score
from src.control_mapping import control_mapping
from src.audit_logger import log_audit
from src.pdf_report import generate_pdf

df = pd.read_csv("data/credit_data.csv")
human_df = pd.read_csv("data/human_explanations.csv")
policy_text = open("data/credit_policy.txt").read()

model, X = train_model()
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

human_agree = human_ai_agreement(
    human_df.loc[0, "human_explanation"],
    llm_explanations[0]
)

grounding = grounding_score(llm_explanations[0], policy_text)

results = {
    "faithfulness_score": faith,
    "bias_deviation_index": bias,
    "compliance_violation": compliance,
    "stability_score": stability,
    "human_ai_agreement": human_agree,
    "policy_grounding_score": grounding
}

results.update(control_mapping(results))

log_audit(results)
generate_pdf(results)

print("Regulatory-Grade Credit AI Evaluation Completed.")
