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