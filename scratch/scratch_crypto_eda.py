import json

import pandas as pd
import requests
from bs4 import BeautifulSoup

currency_price_unit = "USD"

cmc = requests.get("https://coinmarketcap.com")
soup = BeautifulSoup(cmc.content, "html.parser")

data = soup.find("script", id="__NEXT_DATA__", type="application/json")
coins = {}
coin_data = json.loads(data.contents[0])
listings = coin_data["props"]["initialState"]["cryptocurrency"]["listingLatest"]["data"]

attributes = listings[0]["keysArr"]
index_of_id = attributes.index("id")
index_of_slug = attributes.index("slug")

for i in listings[1:]:
    
    
    coins[str(i[index_of_id])] = i[index_of_slug]

coin_name = []
coin_symbol = []
market_cap = []
percent_change_1h = []
percent_change_24h = []
percent_change_7d = []
price = []
volume_24h = []

index_of_slug = attributes.index("slug")
index_of_symbol = attributes.index("symbol")
index_of_quote_usd_price = attributes.index("quote.USD.price")
index_of_quote_usd_percent_change_1h = attributes.index("quote.USD.percentChange1h")
index_of_quote_usd_percent_change_24h = attributes.index("quote.USD.percentChange24h")
index_of_quote_usd_percent_change_7d = attributes.index("quote.USD.percentChange7d")
index_of_quote_usd_market_cap = attributes.index("quote.USD.marketCap")
index_of_quote_usd_volume_24h = attributes.index("quote.USD.volume24h")

for i in listings[1:]:
    coin_name.append(i[index_of_slug])
    coin_symbol.append(i[index_of_symbol])
    price.append(i[index_of_quote_usd_price])
    percent_change_1h.append(i[index_of_quote_usd_percent_change_1h])
    percent_change_24h.append(i[index_of_quote_usd_percent_change_24h])
    percent_change_7d.append(i[index_of_quote_usd_percent_change_7d])
    market_cap.append(i[index_of_quote_usd_market_cap])
    volume_24h.append(i[index_of_quote_usd_volume_24h])

    # coin_name.append(i["slug"])
    # coin_symbol.append(i["symbol"])
    # price.append(i["quote"][currency_price_unit]["price"])
    # percent_change_1h.append(i["quote"][currency_price_unit]["percent_change_1h"])
    # percent_change_24h.append(i["quote"][currency_price_unit]["percent_change_24h"])
    # percent_change_7d.append(i["quote"][currency_price_unit]["percent_change_7d"])
    # market_cap.append(i["quote"][currency_price_unit]["market_cap"])
    # volume_24h.append(i["quote"][currency_price_unit]["volume_24h"])

df = pd.DataFrame(
    columns=[
        "coin_name",
        "coin_symbol",
        "market_cap",
        "percent_change_1h",
        "percent_change_24h",
        "percent_change_7d",
        "price",
        "volume_24h",
    ]
)
df["coin_name"] = coin_name
df["coin_symbol"] = coin_symbol
df["price"] = price
df["percent_change_1h"] = percent_change_1h
df["percent_change_24h"] = percent_change_24h
df["percent_change_7d"] = percent_change_7d
df["market_cap"] = market_cap
df["volume_24h"] = volume_24h
