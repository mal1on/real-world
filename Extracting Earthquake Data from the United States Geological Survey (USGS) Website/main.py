"""
Аccess the United States Geological Survey free API and download
real-time earthquake events.
"""

import requests


URL = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson'


def data_getter():
    """Get data from the API"""

    response = requests.get(URL, timeout=10)
    if response.status_code != 200:
        raise Exception(f'API error: {response.status_code}')

    data = response.json()

    return data

print(data_getter())
