import pandas as pd

trade = pd.read_csv("../../data/trade_stats.csv")
tariff = pd.read_csv("../../data/tariffs.csv")
freight = pd.read_csv("../../data/freight.csv")
marketplace = pd.read_csv("../../data/marketplace.csv")

# Merge datasets
df = trade.merge(tariff, on=["HS Code","Country"], how="left") \
          .merge(freight, on=["Country"], how="left") \
          .merge(marketplace, left_on=["Product"], right_on=["name"], how="left")

# Calculate margin
df["Margin_USD"] = df["Price"].astype(float) - (df["Value"].astype(float) + df["Tariff"].astype(float) + df["Cost"].astype(float))
df.to_csv("../../data/recommendations.csv", index=False)
