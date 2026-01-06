## SOC-2 AI Governance Controls

### CC6.1 – Logical Access
- API secured via API keys
- Kubernetes Secrets
- Role-based access for auditors vs operators

### CC7.2 – System Monitoring
- Real-time bias drift alerts
- Explanation stability monitoring
- Audit log persistence (SQL)

### PI1.1 – Processing Integrity
- ML model version locking
- LLM prompt versioning
- Faithfulness scoring vs SHAP

### AI-EXT-01 – Explainability Validation
- SHAP/LIME used as ground truth
- LLM explanations evaluated against model features
- Human override workflow enforced

### AI-EXT-02 – Fairness Enforcement
- AIF360 disparate impact checks
- Protected attribute masking
- Bias deviation index logged
