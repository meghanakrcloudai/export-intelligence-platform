import streamlit as st
import pandas as pd

st.title("Export Intelligence Dashboard")

tabs = ["Trade Stats", "Tariffs", "Freight", "Marketplace", "Recommendations"]
tab = st.sidebar.selectbox("Select Tab", tabs)

file_map = {
    "Trade Stats": "../data/trade_stats.csv",
    "Tariffs": "../data/tariffs.csv",
    "Freight": "../data/freight.csv",
    "Marketplace": "../data/marketplace.csv",
    "Recommendations": "../data/recommendations.csv"
}

try:
    df = pd.read_csv(file_map[tab])
    st.dataframe(df)
except FileNotFoundError:
    st.warning(f"{file_map[tab]} not found. Run the corresponding module first.")
