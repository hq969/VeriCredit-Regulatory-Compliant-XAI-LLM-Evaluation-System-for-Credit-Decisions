from pydantic import BaseModel
from typing import Dict

class CreditRequest(BaseModel):
    features: Dict[str, float]
    decision: int
    llm_explanation: str

class EvaluationResponse(BaseModel):
    faithfulness_score: float
    bias_deviation_index: float
    compliance_violation: int
    stability_score: float
    human_ai_agreement: float
    policy_grounding_score: float
    final_risk_score: float
    regulatory_status: str
