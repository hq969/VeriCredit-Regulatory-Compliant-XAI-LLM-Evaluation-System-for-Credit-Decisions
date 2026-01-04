import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

def train_model():
    df = pd.read_csv("data/credit_data.csv")
    X = df.drop(columns=["approved"])
    y = df["approved"]

    X = pd.get_dummies(X, drop_first=True)

    model = XGBClassifier(eval_metric="logloss")
    model.fit(X, y)

    return model, X
