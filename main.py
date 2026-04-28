from src.preprocessing import load_data
from src.scoring import rule_score
from src.ml_model import train_model
from src.roi_simulation import simulate_roi
import pandas as pd

path = "data/simulated_leads_nova_lead.csv"

df = load_data(path)

#Scoring

df["rule_score"] = df.apply(rule_score, axis=1)

#Model

model, features = train_model(path)

X = pd.get_dummies(df[["source", "intent"]])
X["response_delay"] = df["response_delay_min"]

X = X.reindex(columns=features, fill_value=0)

df["ml_score"] = model.predict_proba(X)[:, 1] * 100

print(df[["rule_score", "ml_score", "converted"]].head(10))

df = simulate_roi(df)