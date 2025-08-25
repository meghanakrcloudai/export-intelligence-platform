import requests
import pandas as pd

API_KEY = "YOUR_FREIGHTOS_KEY"
BASE_URL = "https://api.freightos.com/v1/rates"

def get_sea_freight(origin, destination, container_type="20ft"):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {"origin": origin, "destination": destination, "container_type": container_type}
    response = requests.get(BASE_URL, headers=headers, params=params)
    data = response.json()
    df = pd.DataFrame(data.get("rates", []))
    df.to_csv("../../data/freight.csv", index=False)
    return df

if __name__ == "__main__":
    df = get_sea_freight("INNSA", "AEJEA")
    print(df.head())
