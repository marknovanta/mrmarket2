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

    for t in tickers:
        intrinsic_value = get_intrinsic_value(t, api_key)
        stock = yf.Ticker(t)
        mkt_cap = stock.info['marketCap']
        print(f'\n{t} ---')
        print(f'INTRINSIC VALUE: ${intrinsic_value:,}')
        print(f'MARKET CAP: ${mkt_cap:,}')
        if intrinsic_value is None:
            print(f'{t}: Not able to calculate')
            continue




if __name__ == '__main__':
    main()