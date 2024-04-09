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

        # check if intrinsic value is not None
        if intrinsic_value is None:
            print(f'{t}: Not able to calculate')
            continue

        print(f'INTRINSIC VALUE: ${intrinsic_value:,}')
        print(f'MARKET CAP: ${mkt_cap:,}')

        # evaluate
        if mkt_cap > intrinsic_value:
            valuation = 'Overvalued'
        elif mkt_cap < intrinsic_value:
            valuation = 'Undervalued'
        else:
            valuation = 'Fair Value'

        margin_of_safety = (mkt_cap - intrinsic_value)/intrinsic_value
        print(f'{t} is {valuation} of {round((margin_of_safety*100), 2)}%')



if __name__ == '__main__':
    main()