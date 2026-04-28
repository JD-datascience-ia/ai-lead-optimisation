from src.rule_scoring import rule_score
import pandas as pd

df = df.read_csv("data/simulated_leads_nova_lead.csv")

df["score"] = df.apply(rule_score, axis=1)