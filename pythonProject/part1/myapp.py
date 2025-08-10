import yfinance as yf
import streamlit as st
import pandas as pd
st.write("""
#simple stock price App
show are the stock closing price and volume of Google!
""")

#define the ticker symbol
tickerSymbol = 'GOOGL'

#get data on this ticker

tickerDate=yf.Ticker(tickerSymbol)

#get the historical prices for this ticker

tickerDf = tickerData.history(period='id',start='2010-5-31',end='2026-5-31')
#open High low Close Volume Dividends Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.volume)