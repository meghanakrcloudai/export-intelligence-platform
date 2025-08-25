import streamlit as st
import pandas as pd
import os

st.title("Export Intelligence Dashboard")

tabs = ["Trade Stats", "Tariffs", "Freight", "Marketplace", "Recommendations"]
tab = st.sidebar.selectbox("Select Tab", tabs)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_map = {
    "Trade Stats": os.path.join(BASE_DIR, "../data/trade_stats.csv"),
    "Tariffs": os.path.join(BASE_DIR, "../data/tariffs.csv"),
    "Freight": os.path.join(BASE_DIR, "../data/freight.csv"),
    "Marketplace": os.path.join(BASE_DIR, "../data/marketplace.csv"),
    "Recommendations": os.path.join(BASE_DIR, "../data/recommendations.csv")
}

DATA_FILE = file_map[tab]

try:
    # Use Python engine and skip bad lines
    df = pd.read_csv(
        DATA_FILE,
        on_bad_lines='skip',       # skip malformed rows
        quotechar='"',             # handle quoted fields with commas
        skipinitialspace=True,
        engine='python'            # more tolerant parser
    )
    
    if df.empty:
        st.warning(f"{DATA_FILE} is empty or has malformed rows. Please check the source module.")
    else:
        st.dataframe(df)
except FileNotFoundError:
    st.warning(f"{DATA_FILE} not found. Run the corresponding module first.")
except pd.errors.ParserError as e:
    st.error(f"Failed to parse {DATA_FILE}: {e}")
