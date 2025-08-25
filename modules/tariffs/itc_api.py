# modules/tariffs/itc_api.py
import requests
import pandas as pd

ITC_API_KEY = "YOUR_ITC_KEY"
BASE_URL = "https://api.trademap.org/api/v1/tariff"

def get_tariff(country_code, hs_code):
    params = {"country": country_code, "hs": hs_code, "api_key": ITC_API_KEY}
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    df = pd.DataFrame(response.json()['tariff_data'])
    df.to_csv("../../data/tariffs.csv", index=False)
    return df

if __name__ == "__main__":
    df = get_tariff("AE", "100630")
    print(df.head())
