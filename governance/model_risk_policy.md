## Model Risk Policy – Credit AI

### Model Inventory
- Credit Decision Model (XGBoost / Logistic)
- Explanation Model (LLM – Non-decisioning)

### Risk Classification
- Tier 1 (High Impact – Credit Decisions)

### Validation Layers
1. Statistical performance (AUC, KS)
2. Explainability alignment (SHAP faithfulness)
3. Bias testing (AIF360)
4. Stability testing (re-prompt variance)
5. Human review checkpoints

### Model Change Control
- Git commit hash tracking
- Shadow deployment
- Rollback mechanism
