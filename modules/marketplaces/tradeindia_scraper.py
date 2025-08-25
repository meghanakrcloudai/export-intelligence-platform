import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_tradeindia(product):
    url = f"https://www.tradeindia.com/SellerSearch/{product}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    sellers = soup.select(".seller-info")
    data = []
    for s in sellers:
        name = s.select_one(".company-name").get_text(strip=True)
        price = s.select_one(".price").get_text(strip=True)
        data.append({"name": name, "price": price})
    df = pd.DataFrame(data)
    df.to_csv("../../data/tradeindia.csv", index=False)
    return df

if __name__ == "__main__":
    df = scrape_tradeindia("basmati-rice")
    print(df.head())
