from google.adk.agents import Agent
import yfinance as yf
import numpy as np


# ============================================================
# TOOL 1 — Price Summary
# ============================================================
def get_price_summary(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info

    return {
        "ticker": ticker.upper(),
        "current_price": info.get("currentPrice"),
        "previous_close": info.get("previousClose"),
        "open_price": info.get("open"),
        "day_high": info.get("dayHigh"),
        "day_low": info.get("dayLow"),
        "volume": info.get("volume"),
        "currency": info.get("currency"),
    }


# ============================================================
# TOOL 2 — Fundamentals
# ============================================================
def get_fundamentals(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info

    return {
        "ticker": ticker.upper(),
        "company_name": info.get("shortName"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "eps": info.get("trailingEps"),
        "beta": info.get("beta"),
        "dividend_yield": info.get("dividendYield"),
    }


# ============================================================
# TOOL 3 — 30-Day Historical Trend
# ============================================================
def get_historical_trend(ticker: str):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")

    if hist.empty:
        return {"error": "No historical data available", "ticker": ticker.upper()}

    closes = hist["Close"].tolist()

    return {
        "ticker": ticker.upper(),
        "closing_prices": closes,
        "start_price": closes[0],
        "end_price": closes[-1],
        "trend": "upward" if closes[-1] > closes[0] else "downward",
        "change_percent": round(((closes[-1] - closes[0]) / closes[0]) * 100, 2),
        "days": len(closes),
    }


# ============================================================
# TOOL 4 — SMA Technical Indicators
# ============================================================
def get_technical_indicators(ticker: str):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="6mo")

    if hist.empty:
        return {"error": "No technical data available", "ticker": ticker.upper()}

    hist["SMA20"] = hist["Close"].rolling(20).mean()
    hist["SMA50"] = hist["Close"].rolling(50).mean()
    hist["SMA200"] = hist["Close"].rolling(200).mean()

    latest = hist.iloc[-1]

    return {
        "ticker": ticker.upper(),
        "latest_price": latest["Close"],
        "sma20": None if np.isnan(latest["SMA20"]) else latest["SMA20"],
        "sma50": None if np.isnan(latest["SMA50"]) else latest["SMA50"],
        "sma200": None if np.isnan(latest["SMA200"]) else latest["SMA200"],
        "trend_signal": "Bullish" if latest["Close"] > latest["SMA50"] else "Bearish"
    }


# ============================================================
# TOOL 5 — Risk Score Engine
# Uses volatility, technicals, fundamentals
# ============================================================
def get_risk_score(ticker: str):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="3mo")

    if hist.empty:
        return {"error": "Risk data unavailable", "ticker": ticker.upper()}

    daily_returns = hist["Close"].pct_change().dropna()
    volatility = float(np.std(daily_returns))

    # Risk classification
    if volatility > 0.03:
        level = "High Risk"
    elif volatility > 0.015:
        level = "Medium Risk"
    else:
        level = "Low Risk"

    return {
        "ticker": ticker.upper(),
        "volatility": round(volatility, 4),
        "risk_level": level
    }


# ============================================================
# TOOL 6 — Sentiment (Based on price action only)
# ============================================================
def get_sentiment(ticker: str):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="10d")

    if hist.empty:
        return {"error": "Sentiment data unavailable", "ticker": ticker.upper()}

    closes = hist["Close"].tolist()
    sentiment = "Bullish" if closes[-1] > closes[0] else "Bearish"

    return {
        "ticker": ticker.upper(),
        "10d_change": round(((closes[-1] - closes[0]) / closes[0]) * 100, 2),
        "sentiment": sentiment
    }


# ============================================================
# TOOL 7 — Master Overview Tool
# Calls everything internally
# ============================================================
def get_master_overview(ticker: str):
    return {
        "ticker": ticker.upper(),
        "price": get_price_summary(ticker),
        "fundamentals": get_fundamentals(ticker),
        "trend": get_historical_trend(ticker),
        "technicals": get_technical_indicators(ticker),
        "risk": get_risk_score(ticker),
        "sentiment": get_sentiment(ticker)
    }


# ============================================================
# ADVANCED STOCK AGENT
# ============================================================
stock_agent = Agent(
    name="advanced_stock_agent",
    model="gemini-2.5-pro",
    description="Advanced Multi-Tool Stock Analysis Agent with risk, sentiment, and master analysis capabilities.",

    instruction="""
You are an institutional-grade financial analysis AI.

You MUST:
- Decide the correct tool based on the query.
- Provide high-quality analysis like Goldman Sachs / JP Morgan reports.
- Present information in a clean, structured manner.

TOOL RULES:
-----------
1️⃣ Price → get_price_summary  
2️⃣ Fundamentals → get_fundamentals  
3️⃣ Trend / 30-day performance → get_historical_trend  
4️⃣ SMA / technical → get_technical_indicators  
5️⃣ Volatility / risk → get_risk_score  
6️⃣ Sentiment / short-term direction → get_sentiment  
7️⃣ Full analysis → get_master_overview  

STRUCTURE YOUR RESPONSE:
------------------------
📌 **1. Company Snapshot**  
📈 **2. Price & Market Action**  
📊 **3. Fundamentals**  
📉 **4. Trend Analysis**  
📐 **5. Technical Indicators (SMA)**  
⚠️ **6. Risk Assessment**  
🙂 **7. Market Sentiment**  
🎯 **8. Final Investment Insights**  

Your tone should be:
- Clear  
- Professional  
- Insightful  
- Action-oriented  
""",

    tools=[
        get_price_summary,
        get_fundamentals,
        get_historical_trend,
        get_technical_indicators,
        get_risk_score,
        get_sentiment,
        get_master_overview
    ],
)

root_agent = stock_agent
