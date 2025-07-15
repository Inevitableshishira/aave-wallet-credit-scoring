# Aave Wallet Credit Scoring

## 📌 Overview

This project assigns a credit score (0-1000) to wallets interacting with Aave V2 on Polygon using DeFi transaction data.

## 💡 Features Extracted

- Total Deposits / Borrows / Repays in USD
- Number of each transaction type
- Active days and transaction frequency
- Borrow-to-Deposit and Repay-to-Borrow ratios
- Liquidation presence

## 🧠 Scoring Logic

- Repay-to-Borrow Ratio > 90% → +300
- No Liquidations → +200
- Active > 30 days → +100
- Frequent activity → +100
- High deposits/borrows → +100 each
- Safe borrow ratios → +100

## ⚙️ How to Run

```bash
python src/score_generator.py
```

## 📁 Output

- `outputs/wallet_scores.csv`: Final wallet scores