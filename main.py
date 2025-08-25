from modules.trade_stats.scraper import get_trade_data
from modules.tariffs.itc_api import get_tariff
from modules.freight.sea_freight import get_sea_freight
from modules.freight.air_freight import get_air_freight
from modules.marketplaces.indiamart_scraper import scrape_indiamart
from modules.analytics.engine import *

# Step 1: Trade Stats
trade_df = get_trade_data()

# Step 2: Tariffs
tariff_df = get_tariff("AE", "100630")

# Step 3: Freight
sea_df = get_sea_freight("INNSA", "AEJEA")
air_df = get_air_freight("INDEL", "AEJEA")

# Step 4: Marketplace
marketplace_df = scrape_indiamart("basmati-rice")

# Step 5: Analytics
# Already executed when engine.py is imported
