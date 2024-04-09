import os
import yfinance as yf
from dotenv import load_dotenv
from watchlist import tickers
from helper import get_intrinsic_value

def configure():
    load_dotenv()

def main():
    configure()
    api_key = os.getenv('api_key')

    print()
    for t in tickers:
        intrinsic_value = get_intrinsic_value(t, api_key)
        stock = yf.Ticker(t)
        mkt_cap = stock.info['marketCap']
        print(mkt_cap)



if __name__ == '__main__':
    main()