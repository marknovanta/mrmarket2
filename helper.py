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
    try:
        reports = data['annualReports']
    except:
        print('\n')
        print(data['Information'])
        print('\n')
        return None

    fcf_records = []
    for r in reports:

        operating_cf = r['operatingCashflow']
        cap_ex = r['capitalExpenditures']
        fcf = float(operating_cf) - float(cap_ex)

        fcf_records.append(fcf)
    fcf_records.reverse()



    # calculate CAGR in the past x years
    period = len(fcf_records)-1
    start_value = fcf_records[0]
    end_value = fcf_records[-1]

    # CAGR (evaluate if smooth it by x%, add the decimal percentage at the end)
    cagr = (((end_value/start_value)**(1/period))-1)*0.90
    print(f'\n{ticker} ---')
    print(f'CAGR: {round((cagr*100), 2)}%')

    current = fcf_records[-1]
    year1 = current * (1 + cagr)**1
    year2 = current * (1 + cagr)**2
    year3 = current * (1 + cagr)**3
    year4 = current * (1 + cagr)**4
    year5 = current * (1 + cagr)**5
    year6 = current * (1 + cagr)**6
    year7 = current * (1 + cagr)**7
    year8 = current * (1 + cagr)**8
    year9 = current * (1 + cagr)**9
    year10 = current * (1 + cagr)**10

    # DISCOUNT RATE
    discount_rate = 0.1

    year1_present = year1/(1 + discount_rate)**1
    year2_present = year2/(1 + discount_rate)**2
    year3_present = year3/(1 + discount_rate)**3
    year4_present = year4/(1 + discount_rate)**4
    year5_present = year5/(1 + discount_rate)**5
    year6_present = year6/(1 + discount_rate)**6
    year7_present = year7/(1 + discount_rate)**7
    year8_present = year8/(1 + discount_rate)**8
    year9_present = year9/(1 + discount_rate)**9
    year10_present = year10/(1 + discount_rate)**10

    # TERMINAL GROWTH
    terminal_growth = 0.02

    terminal_value = (year10 * (1 + terminal_growth))/(discount_rate - terminal_growth)
    terminal_value_present = terminal_value/(1 + discount_rate)**10

    # Calculate intrinsic value
    intrinsic_value = year1_present + year2_present + year3_present + year4_present + year5_present + year6_present + year7_present + year8_present + year9_present + year10_present + terminal_value_present

    return intrinsic_value





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