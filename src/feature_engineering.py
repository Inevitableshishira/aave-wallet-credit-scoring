import pandas as pd
from collections import defaultdict

def scale_amount(raw_amount, decimals=6):
    return float(raw_amount) / (10 ** decimals)

def transform_data(transactions):
    wallet_data = defaultdict(lambda: defaultdict(float))
    wallet_dates = defaultdict(list)

    for tx in transactions:
        wallet = tx["userWallet"]
        action = tx["action"].lower()
        timestamp = tx["timestamp"]
        price = float(tx["actionData"]["assetPriceUSD"])
        amount = float(tx["actionData"]["amount"])

        decimals = 6 if tx["actionData"]["assetSymbol"] == "USDC" else 18
        usd_value = scale_amount(amount, decimals) * price

        wallet_data[wallet][f"total_{action}s_usd"] += usd_value
        wallet_data[wallet][f"num_{action}s"] += 1
        wallet_dates[wallet].append(timestamp)

    features = []
    for wallet, data in wallet_data.items():
        dates = wallet_dates[wallet]
        active_days = (max(dates) - min(dates)) / (60 * 60 * 24)
        total_txs = sum(data[k] for k in data if k.startswith("num_"))
        avg_tx_per_day = total_txs / active_days if active_days > 0 else total_txs

        data["wallet"] = wallet
        data["active_days"] = active_days
        data["avg_tx_per_day"] = avg_tx_per_day
        data["borrow_to_deposit_ratio"] = data["total_borrows_usd"] / data["total_deposits_usd"] if data["total_deposits_usd"] else 0
        data["repay_to_borrow_ratio"] = data["total_repays_usd"] / data["total_borrows_usd"] if data["total_borrows_usd"] else 0
        features.append(data)

    return pd.DataFrame(features)