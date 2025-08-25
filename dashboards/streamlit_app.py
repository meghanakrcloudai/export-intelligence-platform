# dashboards/streamlit_app.py
import streamlit as st
import pandas as pd
import os
import warnings

st.set_page_config(page_title="Export Intelligence Dashboard", layout="wide")
st.title("Export Intelligence Dashboard")

# Sidebar for tabs
tabs = ["Trade Stats", "Tariffs", "Freight", "Marketplace", "Recommendations"]
tab = st.sidebar.selectbox("Select Tab", tabs)

# Base directory for relative paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Map tab names to CSV files
file_map = {
    "Trade Stats": os.path.join(BASE_DIR, "../data/trade_stats.csv"),
    "Tariffs": os.path.join(BASE_DIR, "../data/tariffs.csv"),
    "Freight": os.path.join(BASE_DIR, "../data/freight.csv"),
    "Marketplace": os.path.join(BASE_DIR, "../data/marketplace.csv"),
    "Recommendations": os.path.join(BASE_DIR, "../data/recommendations.csv")
}

DATA_FILE = file_map[tab]

def read_csv_safe(file_path):
    """Read CSV safely, skipping malformed rows and logging warnings"""
    if not os.path.exists(file_path):
        st.warning(f"{file_path} not found. Run the corresponding scraping module first.")
        return pd.DataFrame()
    
    try:
        with warnings.catch_warnings(record=True) as w:
            df = pd.read_csv(
                file_path,
                engine='python',           # more tolerant parser
                on_bad_lines='skip',       # skip malformed rows
                quotechar='"',             # handle quoted fields
                skipinitialspace=True
            )
            if w:
                st.warning(f"Some rows in {file_path} were skipped due to parsing issues.")
            return df
    except pd.errors.ParserError as e:
        st.error(f"Failed to parse {file_path}: {e}")
        return pd.DataFrame()

# Load CSV for the selected tab
df = read_csv_safe(DATA_FILE)

# Display dataframe or warning if empty
if df.empty:
    st.info(f"No data available for '{tab}'.")
else:
    st.dataframe(df, use_container_width=True)
