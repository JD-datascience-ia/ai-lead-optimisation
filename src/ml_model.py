import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model(path):
    df = pd.read_csv(path)

    #Features

    X = pd.get_dummies(df[["source", "intent"]])
    X["response_delay"] = df["response_delay_min"]

    y = df["converted"]


    #Split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #Model

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    #Predictions

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    print(f"Model accuracy : {acc:.2f}")

    return model, X.columns
