from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime

engine = create_engine("sqlite:///monitoring.db")

def store_metrics(metrics):
    metrics["timestamp"] = datetime.utcnow()
    df = pd.DataFrame([metrics])
    df.to_sql("credit_ai_metrics", engine, if_exists="append", index=False)
