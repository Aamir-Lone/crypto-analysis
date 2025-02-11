import requests
import pandas as pd
from config.settings import API_URL, PARAMS
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def fetch_crypto_data():
    """Fetches top 50 cryptocurrency data from CoinGecko API"""
    try:
        response = requests.get(API_URL, params=PARAMS)
        response.raise_for_status()  # Raises error for bad response (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def process_data(data):
    """Processes raw API data into a structured Pandas DataFrame"""
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
    """Saves the processed cryptocurrency data to an Excel file."""
    data_dir = os.path.join(os.path.dirname(__file__), "../data")
    os.makedirs(data_dir, exist_ok=True)  # Ensure the directory exists
    file_path = os.path.join(data_dir, "live_crypto_data.xlsx")

    df.to_excel(file_path, index=False)
    print(f"✅ Data saved to {file_path}")


if __name__ == "__main__":
    crypto_data = fetch_crypto_data()
    if crypto_data:
        df = process_data(crypto_data)
        # df.to_excel("../data/live_crypto_data.xlsx", index=False)
        data_dir = os.path.join(os.path.dirname(__file__), "../data")
        os.makedirs(data_dir, exist_ok=True)

        # Save the Excel file
        file_path = os.path.join(data_dir, "live_crypto_data.xlsx")
        df.to_excel(file_path, index=False)
        print("Live cryptocurrency data saved to Excel successfully!")
