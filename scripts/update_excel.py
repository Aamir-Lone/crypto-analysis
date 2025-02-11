import time
import os
import requests
import pandas as pd
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import API_URL, PARAMS

def fetch_crypto_data():
    """Fetches the latest cryptocurrency data from the CoinGecko API."""
    try:
        response = requests.get(API_URL, params=PARAMS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")
        return []

def process_data(data):
    """Processes the fetched cryptocurrency data into a DataFrame."""
    df = pd.DataFrame(data)[["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]]
    
    df.rename(columns={
        "name": "Cryptocurrency Name",
        "symbol": "Symbol",
        "current_price": "Current Price (USD)",
        "market_cap": "Market Capitalization",
        "total_volume": "24h Trading Volume",
        "price_change_percentage_24h": "24h Price Change (%)"
    }, inplace=True)

    return df

def save_to_excel(df):
    """Saves the updated cryptocurrency data to an Excel file."""
    # Ensure the data directory exists
    data_dir = os.path.join(os.path.dirname(__file__), "../data")
    os.makedirs(data_dir, exist_ok=True)

    # Save file path
    file_path = os.path.join(data_dir, "live_crypto_data.xlsx")

    # Save DataFrame to Excel
    df.to_excel(file_path, index=False)
    print(f"✅ Data updated in {file_path}")

def update_data(interval=300):
    """Continuously updates the Excel file every `interval` seconds."""
    while True:
        print("\n🔄 Fetching latest cryptocurrency data...")
        crypto_data = fetch_crypto_data()
        if crypto_data:
            df = process_data(crypto_data)
            save_to_excel(df)
            print("📊 Excel updated successfully!")
        else:
            print("⚠️ Failed to update data. Retrying in 5 minutes...")

        print(f"⏳ Next update in {interval // 60} minutes...\n")
        time.sleep(interval)  # Wait before fetching again

if __name__ == "__main__":
    update_data()
