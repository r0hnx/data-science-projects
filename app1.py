#!/usr/bin/env python
# coding: utf-8

import yfinance as yf
import streamlit as st


st.write("""
# Simple Stock Price App

Shown below are the stock **closing price** and ***volume*** of Google!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symbol
tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period="1d", start="2001-01-01", end="2021-01-01")
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)