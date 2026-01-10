"""Program that returns the exchange rate for any given currency for
any given date."""


import requests


API_KEY = 'SltNRbkTkzpsbLbnMEyAppTlErx8MQ5Q'


def converter(date, to_curr, from_curr):
    """Main function"""

    url = f"https://api.apilayer.com/currency_data/convert?date={date}&to={to_curr}&from={from_curr}&amount=1"
    headers = {
        "apikey": API_KEY}

    response = requests.request("GET", url, headers=headers, timeout=10)
    
    if response.status_code != 200:
        raise Exception(f"API error: {response.status_code}")

    result = response.json()['result']

    return result


if __name__ == '__main__':
    date = input('Enter date in the "YYYY-MM-DD" format: ')
    from_curr = input('Enter base currency: ')
    to_curr = input('Enter target currency: ')
    try:
        rate = converter(date, to_curr, from_curr)
        print(f'{from_curr} to {to_curr} exchange rate on {date} was {rate}.')
    except Exception as e:
        print(f"Couldn't fetch data, error '{e}' occurred.")
