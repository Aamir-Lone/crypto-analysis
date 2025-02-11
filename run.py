import time
import os
import requests
import pandas as pd
from config.settings import API_URL, PARAMS
from scripts.analyze_data import analyze_data
from scripts.fetch_crypto import fetch_crypto_data, process_data, save_to_excel

def update_data(interval=300):
    """Fetches, analyzes, and updates cryptocurrency data every interval seconds."""
    while True:
        print("\n🔄 Fetching latest cryptocurrency data...")
        crypto_data = fetch_crypto_data()
        if crypto_data:
            df = process_data(crypto_data)
            save_to_excel(df)

            print("📊 Running analysis...")
            analyze_data(os.path.join(os.path.dirname(__file__), "data/live_crypto_data.xlsx"))

            print("✅ Excel updated successfully!")
        else:
            print("⚠️ Failed to update data. Retrying in 5 minutes...")

        print(f"⏳ Next update in {interval // 60} minutes...\n")
        time.sleep(interval)  # Wait before fetching again

if __name__ == "__main__":
    update_data()
