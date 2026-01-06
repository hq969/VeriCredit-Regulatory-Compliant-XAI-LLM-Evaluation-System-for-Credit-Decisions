from fastapi import FastAPI, Header, HTTPException
from api.schemas import CreditRequest, EvaluationResponse
from api.service import evaluate_credit_api

app = FastAPI(
    title="Credit AI Governance API",
    version="1.0"
)

API_KEY = "secure-bank-key"

@app.post("/evaluate", response_model=EvaluationResponse)
def evaluate(
    payload: CreditRequest,
    x_api_key: str = Header(...)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    final_score, status = evaluate_credit_api(payload.dict())

    return {
        **payload.dict(),
        "final_risk_score": final_score,
        "regulatory_status": status
    }
