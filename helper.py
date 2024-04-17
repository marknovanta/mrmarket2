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
        try:
            fcf = float(operating_cf) - float(cap_ex)
        except:
            return None

        fcf_records.append(fcf)
    fcf_records.reverse()



    # calculate CAGR in the past x years
    period = len(fcf_records)-1
    start_value = fcf_records[0]
    end_value = fcf_records[-1]

    # CAGR
    cagr = (((end_value/start_value)**(1/period))-1)


    print(f'\n{ticker} ---')

    try:
        print(f'CAGR: {round((cagr*100), 2)}%')
    except:
        print('Problem with CAGR. Set default')
        cagr = 0.02
        print(f'CAGR: {round((cagr*100), 2)}%')

    # smooth down difficult to sustain CAGRs
    if cagr > 0.1:
        cagr = cagr*0.9

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
