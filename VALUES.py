
import requests
import pandas as pd
import yfinance as yf
import streamlit as st 

@st.cache_data(ttl=3600)
def fetch_info(ticker):
    return yf.Ticker(ticker).info


def get_data(company1,company2):
  
 
 try:
        info = fetch_info(f"{company1}.NS")
        info1 = fetch_info(f"{company2}.NS")
    except Exception:
        return "Yahoo Finance rate limit exceeded. Try again later."

  metrics= [
            "company",
            "sector",
            "price",
            "market_cap",
            "high_52w",
            "low_52w",
            "dividend_yield",
            "revenue",
            "pe",
            "pb",
            "roe",
            "ev_ebitda",
            "roa",
            "profit_margin",
            "debt",
            "debt_equity",
            "cash",
            "operating_cf",
            "free_cf",
            "revenue_growth",
            "earnings_growth"
   ]

  df1_values=[ info.get("longName"),
             info.get("sector"),
             info.get("currentPrice"),
             info.get("marketCap"),
             info.get("fiftyTwoWeekHigh"),
             info.get("fiftyTwoWeekLow"),
             info.get("dividendYield"),
             info.get("totalRevenue"),
             info.get("trailingPE"),
             info.get("priceToBook"),
             info.get("returnOnEquity"),
             info.get("enterpriseToEbitda"),
             info.get("returnOnAssets"),
             info.get("profitMargins"),
             info.get("totalDebt"),
             info.get("debtToEquity"),
             info.get("totalCash"),
             info.get("operatingCashflow"),
             info.get("freeCashflow"),
             info.get("revenueGrowth"),
             info.get("earningsGrowth")

    ]
  df2_values= [
    info1.get("longName"),
    info1.get("sector"),
    info1.get("currentPrice"),
    info1.get("marketCap"),
    info1.get("fiftyTwoWeekHigh"),
    info1.get("fiftyTwoWeekLow"),
    info1.get("dividendYield"),
    info1.get("totalRevenue"),
    info1.get("trailingPE"),
    info1.get("priceToBook"),
    info1.get("returnOnEquity"),
    info1.get("enterpriseToEbitda"),
    info1.get("returnOnAssets"),
    info1.get("profitMargins"),
    info1.get("totalDebt"),
    info1.get("debtToEquity"),
    info1.get("totalCash"),
    info1.get("operatingCashflow"),
    info1.get("freeCashflow"),
    info1.get("revenueGrowth"),
    info1.get("earningsGrowth")
    ]

  df= pd.DataFrame(
    {
        "METRICS" : metrics,
        "VALUES_COMPANY_1" : df1_values,
        "VALUES_COMPANY_2": df2_values }
     )


  return  df


