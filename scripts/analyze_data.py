import pandas as pd
import os

def analyze_data(file_path, save_report=True):
    """Performs analysis on the cryptocurrency data and saves results if needed."""
    try:
        # Load data from the Excel file
        df = pd.read_excel(file_path)

        # Top 5 Cryptos by Market Cap
        top_5 = df.nlargest(5, "Market Capitalization")

        # Average Price of Top 50 Cryptos
        avg_price = df["Current Price (USD)"].mean()

        # Highest & Lowest 24h Price Change
        highest_change = df.loc[df["24h Price Change (%)"].idxmax()]
        lowest_change = df.loc[df["24h Price Change (%)"].idxmin()]

        # Print results
        print("\n🔹 **Top 5 Cryptocurrencies by Market Cap**")
        print(top_5[["Cryptocurrency Name", "Market Capitalization"]])

        print(f"\n🔹 **Average Price of Top 50 Cryptos:** ${avg_price:.2f}")

        print("\n🔹 **Highest 24h Price Change:**")
        print(f"{highest_change['Cryptocurrency Name']} ({highest_change['24h Price Change (%)']:.2f}%)")

        print("\n🔹 **Lowest 24h Price Change:**")
        print(f"{lowest_change['Cryptocurrency Name']} ({lowest_change['24h Price Change (%)']:.2f}%)")

        # Save analysis report if enabled
        if save_report:
            save_analysis_report(top_5, avg_price, highest_change, lowest_change)
        
        return top_5, avg_price, highest_change, lowest_change

    except Exception as e:
        print(f"❌ Error analyzing data: {e}")

# def save_analysis_report(top_5, avg_price, highest_change, lowest_change):
#     """Saves the analysis report as a text file."""
#     # report_path = "../reports/analysis_report.txt"
#     # Ensure the reports directory exists
#     reports_dir = os.path.join(os.path.dirname(__file__), "../reports")
#     os.makedirs(reports_dir, exist_ok=True)

#     # Define the report file path
#     report_path = os.path.join(reports_dir, "analysis_report.txt")
    
#     with open(report_path, "w") as file:
#         file.write("📊 Cryptocurrency Analysis Report\n")
#         file.write("="*40 + "\n")
        
#         file.write("\n🔹 **Top 5 Cryptocurrencies by Market Cap**\n")
#         file.write(top_5[["Cryptocurrency Name", "Market Capitalization"]].to_string(index=False))
        
#         file.write(f"\n\n🔹 **Average Price of Top 50 Cryptos:** ${avg_price:.2f}")
        
#         file.write(f"\n\n🔹 **Highest 24h Price Change:** {highest_change['Cryptocurrency Name']} ({highest_change['24h Price Change (%)']:.2f}%)")
        
#         file.write(f"\n\n🔹 **Lowest 24h Price Change:** {lowest_change['Cryptocurrency Name']} ({lowest_change['24h Price Change (%)']:.2f}%)")

#     print(f"✅ Analysis report saved at: {report_path}")
def save_analysis_report(top_5, avg_price, highest_change, lowest_change):
    """Saves the analysis report as a text file with UTF-8 encoding."""
    import os

    # Ensure the reports directory exists
    reports_dir = os.path.join(os.path.dirname(__file__), "../reports")
    os.makedirs(reports_dir, exist_ok=True)

    # Define the report file path
    report_path = os.path.join(reports_dir, "analysis_report.txt")

    # Write the report using UTF-8 encoding
    with open(report_path, "w", encoding="utf-8") as file:
        file.write("📊 Cryptocurrency Analysis Report\n")
        file.write("=" * 40 + "\n")

        file.write("\n🔹 **Top 5 Cryptocurrencies by Market Cap**\n")
        file.write(top_5[["Cryptocurrency Name", "Market Capitalization"]].to_string(index=False))

        file.write(f"\n\n🔹 **Average Price of Top 50 Cryptos:** ${avg_price:.2f}")

        file.write(f"\n\n🔹 **Highest 24h Price Change:** {highest_change['Cryptocurrency Name']} ({highest_change['24h Price Change (%)']:.2f}%)")

        file.write(f"\n\n🔹 **Lowest 24h Price Change:** {lowest_change['Cryptocurrency Name']} ({lowest_change['24h Price Change (%)']:.2f}%)")

    print(f"✅ Analysis report saved at: {report_path}")


if __name__ == "__main__":
    # file_path = "../data/live_crypto_data.xlsx"
    

    # Get the absolute path of the project root
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Construct the correct file path
    file_path = os.path.join(BASE_DIR, "data", "live_crypto_data.xlsx")
    analyze_data(file_path)
