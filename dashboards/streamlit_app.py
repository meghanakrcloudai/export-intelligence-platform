import os
import pandas as pd
import streamlit as st

st.title("Export Intelligence Dashboard")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "../data/trade_stats.csv")

df = pd.read_csv(DATA_FILE)

st.subheader("Recent Export Data")
st.dataframe(df)

st.subheader("Top Products")
top_products = df.groupby("Product")["Value"].sum().sort_values(ascending=False)
st.bar_chart(top_products)

