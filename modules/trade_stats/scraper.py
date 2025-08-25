import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

URL = "https://tradestat.commerce.gov.in/eidb/country_wise_ttrade"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../../data")
os.makedirs(DATA_DIR, exist_ok=True)

def get_trade_data():
    response = requests.get(URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    # Find first table
    table = soup.find("table")
    if not table:
        raise ValueError("No tables found on the page")

    # Clean text
    for cell in table.find_all(["td", "th"]):
        cell.string = cell.get_text(strip=True)

    # Convert to pandas dataframe
    df = pd.read_html(StringIO(str(table)))[0]
    df.columns = [col.strip() for col in df.columns]

    return df

def save_trade_data():
    df = get_trade_data()
    csv_path = os.path.join(DATA_DIR, "trade_stats.csv")
    df.to_csv(csv_path, index=False)
    print(f"✅ Data saved to {csv_path}")
    return df

if __name__ == "__main__":
    save_trade_data()
