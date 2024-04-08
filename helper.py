import requests

def fetch_cash_flow_data(ticker, key):
    url = f'https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?period=annual&apikey={key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print('Error fetching data:', e)
        return None

def fetch_valuation(ticker, key):
    url = f'https://financialmodelingprep.com/api/v3/discounted-cash-flow/{ticker}?apikey={key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

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

        if valuation == 'Undervalued':
            print(f'Ticke: {ticker}', '<-----')
        else:
            print(f'Ticke: {ticker}')
        print(f'Price: ${price}')
        print(f'Value: ${value}')
        print(f'Stock is {valuation} of {round(value_offset*100,2)}%')

    except requests.exceptions.RequestException as e:
        print('Error fetching data:', e)
        return None