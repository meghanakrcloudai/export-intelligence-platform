import requests
import pandas as pd

API_KEY = "YOUR_AIR_FREIGHT_KEY"
BASE_URL = "https://api.freightos.com/v1/airrates"

def get_air_freight(origin, destination, weight_kg=100):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {"origin": origin, "destination": destination, "weight": weight_kg}
    response = requests.get(BASE_URL, headers=headers, params=params)
    data = response.json()
    df = pd.DataFrame(data.get("rates", []))
    df.to_csv("../../data/air_freight.csv", index=False)
    return df

if __name__ == "__main__":
    df = get_air_freight("INDEL", "AEJEA")
    print(df.head())
