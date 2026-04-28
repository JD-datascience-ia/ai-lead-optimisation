import pandas as pd

def simulate_roi(df):
    total = len(df)

    #Baseline

    baseline_conv = df["converted"].mean()

    #Simulation

    improved = df.copy()

    #ML

    threshold = improved["ml_score"].median()

    improved["converted_improved"] = improved.apply(
        lambda x: 1 if x["ml_score"] > threshold and x["intent"] != "low" else x["converted"], axis=1
    )

    improved_conv = improved["converted_improved"].mean()

    #Affichage

    print(" ROI SIMULATION ")
    print(f"COnversion actuelle : {baseline_conv:.2%}")
    print(f"Conversion optimisée : {improved_conv:.2%}")
    print(f"Gain relatif : +{(improved_conv - baseline_conv)*100:.2f}%")

    return improved