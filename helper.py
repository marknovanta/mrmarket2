import requests



def get_intrinsic_value(ticker, key):
    url = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={ticker}&apikey={key}'
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
    except requests.exceptions.RequestException as e:
        print('Error fetching data:', e)
        return None

    # get last year free cash flow data
    reports = data['annualReports']

    fcf_records = []
    for r in reports:

        operating_cf = r['operatingCashflow']
        cap_ex = r['capitalExpenditures']
        fcf = float(operating_cf) - float(cap_ex)
        print(fcf)
        fcf_records.append(fcf)
    fcf_records.reverse()
    print(fcf_records)


    # calculate CAGR in the past x years
    period = len(fcf_records)-1
    start_value = fcf_records[0]
    end_value = fcf_records[-1]
    cagr = ((end_value/start_value)**(1/period))-1
    print(cagr)

    # caluclate projected growth
    # calculate terminal value
    # calculate intrinsic value






'''
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

        try:
            ticker = data[0]['symbol']
        except:
            print(f'{ticker}: no data\n')
            return
        value = round(float(data[0]['dcf']), 2)
        price = float(data[0]['Stock Price'])
        if price > value:
            valuation = 'Overvalued'
        elif price < value:
            valuation = 'Undervalued'
        else:
            valuation = 'Fair Price'

        value_offset = (price-value)/value

        if valuation == 'Undervalued' and value_offset < -0.3:
            print(f'Ticke: {ticker}')
            print(f'Price: ${price}')
            print(f'Value: ${value}')
            print(f'Stock is {valuation} of {round(value_offset*100,2)}%\n')

    except requests.exceptions.RequestException as e:
        print(f'{ticker}: error fetching data:', e, '\n')
        return None
'''