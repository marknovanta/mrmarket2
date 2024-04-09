import os
from dotenv import load_dotenv
from watchlist import tickers
from helper import fetch_cash_flow_data, hist_cagr

def configure():
    load_dotenv()

def main():
    configure()
    api_key = os.getenv('api_key')

    print()
    for t in tickers:
        records = fetch_cash_flow_data(t, api_key)
        cagr = hist_cagr(records)



if __name__ == '__main__':
    main()