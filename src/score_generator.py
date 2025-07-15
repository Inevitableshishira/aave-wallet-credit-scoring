import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from src.feature_engineering import transform_data
from src.model import predict_scores
from src.utils import load_json_from_gdrive  # Uses function from utils.py

def main():
    # Load JSON data from Google Drive
    gdrive_url = "https://drive.google.com/file/d/1ISFbAXxadMrt7Zl96rmzzZmEKZnyW7FS/view?usp=sharing"
    data = load_json_from_gdrive(gdrive_url)

    df_features = transform_data(data)
    scores = predict_scores(df_features)
    os.makedirs("outputs", exist_ok=True)
    scores.to_csv("outputs/wallet_scores.csv", index=False)
    print("Scoring complete. Output saved to outputs/wallet_scores.csv")

if __name__ == "__main__":
    main()
