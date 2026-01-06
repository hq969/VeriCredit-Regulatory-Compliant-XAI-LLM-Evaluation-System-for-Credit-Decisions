# VeriCredit

## Regulatory-Compliant XAI & LLM Evaluation System for Credit Decisions

---

## Overview

**VeriCredit** is a production-ready AI governance framework designed to **evaluate, validate, and audit AI-generated credit decision explanations**. It ensures that explanations produced by Large Language Models (LLMs) are **faithful to the underlying credit model**, **free from bias**, **legally compliant**, and **stable across prompts**.

The system addresses a critical gap in modern credit systems where LLMs are used to explain decisions made by traditional ML models (e.g., Logistic Regression, XGBoost), but lack verifiable guarantees of correctness and fairness.

VeriCredit is built to meet the expectations of **financial regulators, model risk teams, and internal audit functions**.

---

## Problem Statement

Financial institutions increasingly rely on AI-generated natural-language explanations for credit decisions such as:

> “Why was this loan application rejected?”

While LLMs improve customer transparency, they introduce **new regulatory risks**:

* Hallucinated or incorrect reasoning
* Misalignment with the actual credit model
* Hidden bias via protected attributes or proxies
* Inconsistent explanations across prompts
* Non-compliant or discriminatory language

Regulators now require **explainable, verifiable, and auditable AI**, not just human-readable text.

**VeriCredit solves this problem by acting as an independent evaluation and governance layer.**

---

## Key Features

### 1. Explanation Faithfulness Validation

* Compares LLM explanations against **SHAP / LIME ground-truth explanations**
* Produces a quantitative **Explanation Faithfulness Score**
* Ensures explanations reflect real model behavior, not fabricated logic

### 2. Bias & Fairness Detection

* Uses **AIF360** to detect bias across protected attributes (e.g., gender, location)
* Identifies proxy discrimination via correlated features
* Outputs a **Bias Deviation Index** for audit review

### 3. Legal & Language Compliance

* Flags discriminatory, misleading, or advisory language
* Enforces fair-lending and anti-discrimination principles
* Prevents legally risky phrasing in customer explanations

### 4. Explanation Stability Testing

* Evaluates consistency across multiple re-prompts
* Detects explanation drift under prompt variation
* Produces a **Consistency Across Re-Prompts score**

### 5. Human vs AI Agreement

* Compares AI explanations with expert-defined rationales
* Quantifies alignment between automated and human explanations

### 6. Full Audit Trail

* SQL-based audit logging
* Model, prompt, and explanation versioning
* Automated, regulator-ready compliance reports (PDF)

---

## System Architecture

```
Client / Auditor
      |
API Gateway
      |
FastAPI (Signed Requests)
      |
Credit ML Model (Logistic / XGBoost)
      |
SHAP / LIME (Ground Truth XAI)
      |
LLM Explanation Generator
      |
Evaluation Engine
  ├── Faithfulness Scoring
  ├── Bias Detection (AIF360)
  ├── Stability Analysis
  └── Compliance Rules
      |
Audit Database (SQL)
      |
Compliance Report (PDF)
```

---

## Evaluation Metrics

| Metric                         | Description                                   |
| ------------------------------ | --------------------------------------------- |
| Explanation Faithfulness Score | Alignment between SHAP/LIME and LLM output    |
| Bias Deviation Index           | Degree of bias across protected attributes    |
| Consistency Score              | Stability of explanations across re-prompts   |
| Human-AI Agreement             | Similarity between AI and expert explanations |
| Compliance Flags               | Legal and policy violations                   |

---

## Tech Stack

* **Programming:** Python
* **ML Models:** Logistic Regression, XGBoost
* **Explainability:** SHAP, LIME
* **LLMs:** OpenAI / Anthropic / Llama (model-agnostic)
* **Fairness:** AIF360
* **Backend:** FastAPI
* **Data & Audit Logs:** SQL
* **Reporting:** ReportLab (PDF)
* **Deployment:** Docker, Kubernetes, CI/CD

---


## Installation

```bash
git clone https://github.com/hq969/vericredit-Regulatory-Compliant-XAI-LLM-Evaluation-System-for-Credit-Decisions.git
cd vericredit-Regulatory-Compliant-XAI-LLM-Evaluation-System-for-Credit-Decisions
pip install -r requirements.txt
```

Set environment variables:

```bash
export OPENAI_API_KEY=your_key_here
```

---

## Running the Pipeline

```bash
python api/main.py
```

Generate audit report:

```bash
python reports/generate_report.py
```

---

## Compliance Alignment

VeriCredit is designed to align with:

* **SR 11-7 (Model Risk Management)**
* **RBI & ECB AI Governance Guidelines**
* **EU AI Act (High-Risk AI Systems)**
* **SOC-2 (AI-extended controls)**
* **Fair Lending & Anti-Discrimination Laws**

---

## Why This Project Matters

Regulators are moving from **“black-box explanations”** to **“provable AI accountability.”**
VeriCredit reflects this shift by ensuring that AI explanations are **measurable, defensible, and auditable**, not just readable.

This project is directly relevant to roles in:

* Responsible AI
* Model Risk Management
* Credit Risk Analytics
* AI Governance
* Regulatory AI Auditing

---
