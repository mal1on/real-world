import os
import requests
from bs4 import BeautifulSoup


def scraper():
    '''
    Scrapes the first section of the Mathematics Wikipedia page along with
    the requests and the BeautifulSoup libraries, and save the results in a
    text file.
    '''
    url = 'https://en.wikipedia.org/wiki/Mathematics'
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.select('p')
        os.makedirs('tmp', exist_ok=True)
        with open('tmp/mathematics.txt', 'w', encoding='utf-8') as file:
            for paragraph in paragraphs[1:5]:
                file.write(paragraph.text)
        print('The first section of the Mathematics Wikipedia page has been scraped and saved in the file mathematics.txt.')
    else:
        print('Failed to retrieve the page.')


if __name__ == '__main__':
    scraper()
