import yfinance as yf
import streamlit as st

st.write(
    """
# Simple Stock Price Application

Shown are the stock ***closing price*** and ***volume*** of Goodyear!

"""
)

ticker_symbol = "GOOGL"
ticker_data = yf.Ticker(ticker_symbol)


ticker_df = ticker_data.history(period="1d", start="2010-5-31", end="2021-12-31")

# Plot the values
st.write(
    """
## Closing Price
"""
)
st.line_chart(ticker_df.Close)

st.write(
    """
## Volume
"""
)
st.line_chart(ticker_df.Volume)
