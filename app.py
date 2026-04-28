import streamlit as st
import pandas as pd
from src.ml_model import train_model

st.title("AI Lead Optimizer Dashboard")

file = st.file_uploader("Upload leads CSV")

if file:
    df = pd.read_csv(file)

    # train model live
    model, features = train_model("data/simulated_leads_nova_lead.csv")

    X = pd.get_dummies(df[["source","intent"]])
    X["response_delay"] = df["response_delay_min"]
    X = X.reindex(columns=features, fill_value=0)

    df["ml_score"] = model.predict_proba(X)[:,1] * 100

    st.subheader("Top Leads")
    st.dataframe(df.sort_values("ml_score", ascending=False).head(10))

    st.bar_chart(df["ml_score"])