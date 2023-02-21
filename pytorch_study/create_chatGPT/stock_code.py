import yfinance as yf
import time

while True:
    stock = yf.Ticker("005930.KS")  # Samsung Electronics stock symbol
    info = stock.info
    print(f"Samsung Electronics ({info['symbol']}): {info['regularMarketPrice']} {info['currency']}")  # Print current stock price and currency
    time.sleep(3)  # Wait for 3 seconds before fetching stock again
