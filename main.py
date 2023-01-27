import streamlit as st
import yfinance as yahooFinance
import pandas as pd


stock = st.text_input('stockname', 'AAPL')

df = pd.DataFrame(yahooFinance.Ticker(stock).history(period="max"))

st.write('HELLO')
st.line_chart(df.Close)
st.line_chart(df.Volume)