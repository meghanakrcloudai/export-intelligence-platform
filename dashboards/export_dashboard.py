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

DATA_FILE = file_map[tab]

try:
    df = pd.read_csv(DATA_FILE, on_bad_lines='skip', quotechar='"', skipinitialspace=True, engine='python')
    if df.empty:
        st.warning(f"{DATA_FILE} is empty or has malformed rows. Please check the source module.")
    else:
        st.dataframe(df)
except FileNotFoundError:
    st.warning(f"{DATA_FILE} not found. Run the corresponding module first.")
except pd.errors.ParserError as e:
    st.error(f"Failed to parse {DATA_FILE}: {e}")
