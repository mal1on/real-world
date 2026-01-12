"""
Python program that asks for a date and returns historical events for
that date.
"""

import requests


def event_getter(month, day):
    """Get events function"""

    url = f'http://history.muffinlabs.com/date/{month}/{day}'

    response = requests.get(url, timeout=10)
    if response.status_code != 200:
        raise Exception(f'API error: {response.status_code}')

    events = response.json()['data']['Events']

    return events


if __name__ == '__main__':

    month = input('Enter a month e.g., "7" for July: ')
    day = input('Enter a day e.g., "3" for 3rd: ')
    events = None

    try:
        events = event_getter(month, day)
    except Exception as e:
        print(f'Error occurred:\n{e}')

    if events:
        print(f'Historical Events on {month}/{day}:\n')
        for event in events:
            print(f'Year: {event['year']}')
            print(f'Description: {event['text']}')
            print(f'Link: {event['links'][0]['link']}\n')

