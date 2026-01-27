"""
Access the United States Geological Survey free API and download
real-time earthquake events.
"""

import os
import requests
import pandas as pd


URL = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson'


def data_getter():
    """Get data from the API"""

    response = requests.get(URL, timeout=10)
    if response.status_code != 200:
        raise Exception(f'API error: {response.status_code}')

    earthquakes = response.json()['features']

    data_list = []

    for earthquake in earthquakes:
        mag = earthquake['properties']['mag']
        place = earthquake['properties']['place']
        lon, lat, _ = earthquake['geometry']['coordinates']
        data_list.append({
            'Magnitude': mag,
            'Location': place,
            'Latitude': lat,
            'Longitude': lon
             })

    return data_list


def csv_maker(data):
    """Create csv file from the available data"""

    os.makedirs('tmp', exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv('tmp/output.csv', index=False)


if __name__ == '__main__':
    data = data_getter()
    csv_maker(data)
