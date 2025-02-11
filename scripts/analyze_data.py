import pandas as pd
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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

def save_analysis_report(top_5, avg_price, highest_change, lowest_change):
    """Saves the analysis report as a PDF file."""
    # Ensure the reports directory exists
    reports_dir = os.path.join(os.path.dirname(__file__), "../reports")
    os.makedirs(reports_dir, exist_ok=True)

    # Define the PDF report file path
    report_path = os.path.join(reports_dir, "analysis_report.pdf")

    # Create the PDF report
    c = canvas.Canvas(report_path, pagesize=letter)
    c.setFont("Helvetica", 12)

    c.drawString(100, 750, "📊 Cryptocurrency Analysis Report")
    c.drawString(100, 730, "=" * 40)

    c.drawString(100, 710, "🔹 Top 5 Cryptocurrencies by Market Cap:")
    
    y_pos = 690
    for index, row in top_5.iterrows():
        c.drawString(120, y_pos, f"{row['Cryptocurrency Name']}: ${row['Market Capitalization']:,}")
        y_pos -= 20

    c.drawString(100, y_pos - 10, f"🔹 Average Price of Top 50 Cryptos: ${avg_price:,.2f}")
    
    c.drawString(100, y_pos - 40, f"🔹 Highest 24h Price Change: {highest_change['Cryptocurrency Name']} ({highest_change['24h Price Change (%)']}%)")
    c.drawString(100, y_pos - 60, f"🔹 Lowest 24h Price Change: {lowest_change['Cryptocurrency Name']} ({lowest_change['24h Price Change (%)']}%)")

    c.save()
    print(f"✅ Analysis report saved as: {report_path}")

if __name__ == "__main__":
    # Get the absolute path of the project root
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Construct the correct file path
    file_path = os.path.join(BASE_DIR, "data", "live_crypto_data.xlsx")
    analyze_data(file_path)
