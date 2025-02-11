
# 🚀 Fetching and Analyzing Top 50 Live Cryptocurrency Data

✨ Author
👤 Aamir Lone
📧 Email: aamirlone004@gmail.com
💼 LinkedIn: linkedin.com/in/aamir-lone/
🐙 GitHub: github.com/Aamir-Lone



This project fetches live cryptocurrency data, analyzes it, and updates an Excel sheet automatically every 5 minutes.

## 📌 Features
✅ Fetches real-time cryptocurrency data (Top 50 by market cap)  
✅ Performs data analysis:  
   - Top 5 cryptocurrencies by market cap  
   - Average price of the top 50  
   - Highest & lowest 24h price change  
✅ Saves and updates data in an Excel sheet (`data/live_crypto_data.xlsx`)  
✅ Runs continuously, updating every **5 minutes**  

---

## 🛠️ Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/crypto-analysis.git
cd crypto-analysis



### 2️⃣ Install Required Libraries
pip install -r requirements.txt

### 3️⃣ Run this project
python run.py




Project Structure

crypto-analysis/
│── config/                     # Configuration files
│   ├── settings.py              # API settings
│   ├── __init__.py              # Makes config a package
│
│── data/                        # Stores live Excel data
│   ├── live_crypto_data.xlsx     # Updated every 5 minutes
│
│── reports/                     # Stores analysis reports
│   ├── analysis_report.txt       # Updated with latest insights
│
│── scripts/                      # Python scripts
│   ├── fetch_crypto.py           # Fetches and processes data
│   ├── analyze_data.py           # Performs data analysis
│   ├── update_excel.py           # Auto-updates Excel file
│   ├── __init__.py               # Makes scripts a package
│
│── .gitignore                    # Ignores unnecessary files
│── requirements.txt               # Required Python dependencies
│── README.md                      # Documentation
│── run.py                         # Main script to run everything


✨ Author
👤 Aamir Lone
📧 Email: aamirlone004@gmail.com
💼 LinkedIn: linkedin.com/in/aamir-lone/
🐙 GitHub: github.com/Aamir-Lone