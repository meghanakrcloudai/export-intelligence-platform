import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_alibaba(product):
    url = f"https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&SearchText={product}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.select(".organic-gallery-title")
    data = []
    for i in items:
        name = i.get_text(strip=True)
        data.append({"name": name})
    df = pd.DataFrame(data)
    df.to_csv("../../data/alibaba.csv", index=False)
    return df

if __name__ == "__main__":
    df = scrape_alibaba("basmati-rice")
    print(df.head())
