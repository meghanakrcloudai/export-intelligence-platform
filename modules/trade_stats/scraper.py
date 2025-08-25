import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.commerce.gov.in/trade-statistics/"

def get_trade_data():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    # TODO: Inspect commerce.gov.in HTML and select table or CSV links
    table = soup.find("table")  # Placeholder
    df = pd.read_html(str(table))[0]
    return df

if __name__ == "__main__":
    df = get_trade_data()
    print(df.head())
    df.to_csv("../../data/trade_stats.csv", index=False)

