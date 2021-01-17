import yfinance as yf
import streamlit as st

 st.write("""
 # padhiyar 
# Stock Price App
Shown are the stock **closing price** and ***volume*** of Google!
 """)

 tickerSymbol='GOOGL'
 tickerData = yf.Ticker(tickerSymbol)
 tickerData = tickerData.history(period='1d', start='2007-1-1', end='2021-1-1')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)