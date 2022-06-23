from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

from writers.txt import TXTWriter
from writers.csv_writer import CSVWriter
from writers.json_writer import JSONWriter

writers = [
    TXTWriter('cars.txt'),
    CSVWriter('cars.csv'),
    JSONWriter('cars.json'),
]

def random_sleep():
    import random
    import time

    time.sleep(random.randint(1, 3))



page = 0
ua = UserAgent()

while True:
    page += 1

    print(f'Page: {page}')
    base_url = f'https://auto.ria.com/uk/search/'

    random_sleep()

    headers = {
        'User-Agent': ua.random,
    }
    params = {
        'page': page,
        'size': 50,
    }
    response = requests.get(base_url, params=params, headers=headers)
    response.raise_for_status()  # if status_code is not ok raise an error

    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')

    items = soup.find('div', id="searchResults").find_all('section', class_='ticket-item')

    if not items:
        break

    for car_item in items:
        car_details_url = car_item.find('a', class_='address')['href']
        car_id = car_item.find_all('a')[-1]['data-autoid']
        details = {
            'car_id': car_id,
            'car_details_url': car_details_url,
        }
        for writer in writers:
            writer.write(details)
