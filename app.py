import os
from dotenv import load_dotenv
from watchlist import tickers
from helper import fetch_cash_flow_data, fetch_valuation

def configure():
    load_dotenv()

def main():
    configure()
    api_key = os.getenv('api_key')

    print()
    for t in tickers:
        fetch_valuation(t, api_key)



if __name__ == '__main__':
    main()