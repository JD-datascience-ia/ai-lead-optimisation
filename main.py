from src.preprocessing import load_data
from src.scoring import rule_score
import pandas as pd

df = load_data("data/simulated_leads_nova_lead.csv")

df = df.read_csv("data/simulated_leads_nova_lead.csv")

df["score"] = df.apply(rule_score, axis=1)

print(df.sort_values("score", ascending=False).head(10))