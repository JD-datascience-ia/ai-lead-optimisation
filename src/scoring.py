def rule_score(row):
    score = 0

    if row["intent"] == "high":
        score += 50
    elif row["intent"] == "medium":
        score += 25
    else:
        score += 10

    if row["response_delay_min"] < 10:
        score += 30
    elif row["response_delay_min"] < 60:
        score += 15
    else:
        score -=10

    if row["source"] == "referral":
        score += 20
    elif row["source"] == "google_ads":
        score += 15
    elif row["source"] == "facebook_ads":
        score += 10
    elif row["source"] == "instagram":
        score += 5
    else:
        score += 10

    return score