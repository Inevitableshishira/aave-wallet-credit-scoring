def simple_credit_score(row):
    score = 0
    if row['borrow_to_deposit_ratio'] < 0.8:
        score += 100
    if row['repay_to_borrow_ratio'] > 0.9:
        score += 300
    if row.get('num_liquidationcalls', 0) == 0:
        score += 200
    if row['avg_tx_per_day'] > 1.0:
        score += 100
    if row['active_days'] > 30:
        score += 100
    if row['total_deposits_usd'] > 1000:
        score += 100
    if row['total_borrows_usd'] > 500:
        score += 100
    return min(score, 1000)

def predict_scores(df):
    df["credit_score"] = df.apply(simple_credit_score, axis=1)
    return df[["wallet", "credit_score"]]