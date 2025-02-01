"""
Script that scrapes the temperature from the following page every
minute:
https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071
"""

import time
import schedule
import requests
from bs4 import BeautifulSoup

URL = "https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071"


def scraper():
    """Scraper function"""
    response = requests.get(URL, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        temp = soup.find("p", class_="myforecast-current-sm").text
        return True, temp
    else:
        return False, "Failed to load the webpage\n"


def reporter():
    """Main function"""
    print("Scraping the current temperature...")
    result, output = scraper()
    if result:
        print(f"Current temperature: {output}\n")
    else:
        print(output)


if __name__ == "__main__":
    reporter()
    schedule.every(1).minutes.do(reporter)

    while True:
        schedule.run_pending()
        time.sleep(1)
