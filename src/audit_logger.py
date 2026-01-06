from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///audit_logs.db")

def log_audit(data):
    df = pd.DataFrame([data])
    df.to_sql("credit_ai_audit", engine, if_exists="append", index=False)
