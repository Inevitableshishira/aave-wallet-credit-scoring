import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import pandas as pd
from src.feature_engineering import transform_data
from src.model import predict_scores

def main():
    with open("data/user-wallet-transactions.json") as f:
        data = json.load(f)

    df_features = transform_data(data)
    scores = predict_scores(df_features)
    scores.to_csv("outputs/wallet_scores.csv", index=False)
    print("Scoring complete. Output saved to outputs/wallet_scores.csv")

if __name__ == "__main__":
    main()
