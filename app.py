import os
from dotenv import load_dotenv
from watchlist import tickers
from helper import fetch_cash_flow_data, fetch_valuation

def configure():
    load_dotenv()

def main():
    configure()
    api_key = os.getenv('api_key')

    data = fetch_valuation(tickers[0], api_key)
    ticker = data[0]['symbol']
    value = round(float(data[0]['dcf']), 2)
    price = float(data[0]['Stock Price'])
    if price > value:
        valuation = 'Overvalued'
    elif price < value:
        valuation = 'Undervalued'
    else:
        valuation = 'Fair Price'

    value_offset = (price-value)/value

    print(f'Ticke: {ticker}')
    print(f'Price: ${price}')
    print(f'Value: ${value}')
    print(f'Stock is {valuation} of {round(value_offset*100,2)}%')



if __name__ == '__main__':
    main()