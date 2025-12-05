# 📈 Advanced Stock Analysis Agent (ADK + Gemini)

This repository contains an **institutional-grade Stock Market Analysis Agent** built using the **Google Agents Development Kit (ADK)** and **Gemini 2.5 Pro**.  
It performs multi-dimensional stock evaluation using several specialized analytical tools, providing outputs similar to professional financial research reports.

---

## 🚀 Features

### 🧠 Multi-Tool Architecture
The agent includes **seven analytical tools**:

- **Price Summary** – Current price, daily movement, volume  
- **Fundamentals** – Market cap, P/E, EPS, sector, dividend yield  
- **Historical Trend (30 Days)** – Trend direction & percent change  
- **Technical Indicators (SMA20/50/200)** – Momentum-based trend signals  
- **Risk Engine** – Volatility-based risk classification  
- **Sentiment Engine** – Short-term market sentiment  
- **Master Overview Tool** – Aggregates all tools into a comprehensive dataset  

### 🏦 Professional Output Format  
The agent returns structured financial insights:

- 📌 **Company Snapshot**  
- 📈 **Price & Market Action**  
- 📊 **Fundamentals**  
- 📉 **Trend Analysis**  
- 📐 **Technical Indicators**  
- ⚠️ **Risk Assessment**  
- 🙂 **Market Sentiment**  
- 🎯 **Final Investment Insights**

### 🤖 Intelligent Tool Selection
The agent automatically selects tools based on user queries:
- “Price of AAPL?” → Price Summary  
- “Is TSLA risky?” → Risk Engine  
- “Summarize fundamentals for NVDA” → Fundamentals  
- “Is META bullish?” → SMA + Trend  
- “Give full analysis” → Master Overview  

---

## 📚 Technologies Used

- **Python 3.10+**  
- **Google ADK (Agents Development Kit)**  
- **Gemini 2.5 Pro Model**  
- **yfinance** for market data  
- **NumPy** for technical calculation  

---

## 📂 Project Structure

```plaintext
project_root/
│
├── agents/
│   └── stock_agent.py        # Main agent implementation
│
├── requirements.txt          # Dependencies
└── README.md                 # Documentation (this file)
```

## 🛠️ Installation & Setup

### Clone this repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Install Dependencies

```bash
pip install google-adk yfinance
```

### Set your Google API key
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

### Run the ADK Web Dashboard
```bash
adk web
```

##Open the interface:
👉 http://localhost:3000

##Your agent advanced_stock_agent will appear in the dashboard.

##🧪 Usage Examples

###You can ask questions such as:

```
"Give full analysis for AAPL"
"Is TSLA risky?"
"Show 30-day performance for NVDA"
"What is the sentiment for META?"
"Give technical indicators for MSFT"
```

🛡️ Disclaimer

This agent is intended for educational and research purposes only.
It does not constitute financial or investment advice.
Market data may be delayed or incomplete.
