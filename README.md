📈 Advanced Stock Analysis Agent (ADK + Gemini)

This repository contains an institutional-grade Stock Market Analysis Agent built using the Google Agents Development Kit (ADK) and Gemini 2.5 Pro.
The agent performs multi-dimensional stock evaluation using several specialized tools including price analysis, fundamentals, technical indicators, risk scoring, sentiment estimation, and a master aggregation engine.

Designed for developers, traders, and AI enthusiasts, this agent provides intelligent, automated financial insights similar to professional equity research systems.

🚀 Features

Multi-Tool Architecture

The agent includes seven analytical tools:

1. Price Summary – Current price, volume, intraday range

2. Fundamentals – Market cap, P/E, EPS, sector, dividend yield

3. Historical Trend – 30-day price movement & trend direction

4. Technical Indicators – SMA20, SMA50, SMA200, bullish/bearish signals

5. Risk Scoring – Volatility-based low/medium/high risk classification

6. Sentiment Analysis – Short-term directional momentum

7. Master Overview – Combines all tools into a full analytical dataset


🏦 Institutional-Grade Output

The agent produces structured, research-style reports with sections:

- Company Snapshot

- Price & Market Action

- Fundamentals

- Technical Indicators

- Trend Analysis

- Risk Assessment

- Sentiment

- Final Investment Insights


🤖 Smart Tool Selection

Using intent-based logic, the agent automatically calls the correct tool based on the user's query (e.g., “Is TSLA risky?”, “Show fundamentals for AAPL”, “Give full analysis of NVDA”).


📚 Tech Stack

Python 3.10+

Google ADK (Agents Development Kit)

Gemini 2.5 Pro Model

yfinance (for market data)

NumPy (technical calculations)


📂 Project Structure
project_root/
│
├── agents/
│   └── stock_agent.py      # Advanced stock agent implementation
│
├── README.md               # Documentation (this file)
└── requirements.txt        # Python dependencies

🛠️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Set Your GOOGLE_API_KEY
export GOOGLE_API_KEY="your-api-key-here"

4️⃣ Run ADK Dashboard
adk web


Then open:
👉 http://localhost:3000

Your advanced_stock_agent will be listed under the Agents section.

🧪 Usage Examples

Ask the agent:

“Give full analysis for AAPL”
“Is TSLA risky?”
“Show 30-day trend for NVDA”
“Provide technical signals for MSFT”
“What is the sentiment for META?”



🛡️ Disclaimer

This project is for educational and research purposes only.
It is not financial advice. Market data may be delayed or inaccurate.

🤝 Contributing

Contributions, improvements, and feature requests are welcome!
Feel free to open issues or submit pull requests.

⭐ Support the Project

If you find this helpful, consider giving the repository a star ⭐ on GitHub.