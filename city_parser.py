import requests
from bs4 import BeautifulSoup
import re
import csv


def run():
    link = 'https://xn----7sbiew6aadnema7p.xn--p1ai'
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    categories = soup.find_all('ul')[1].find_all('li')

    for category in categories:
        name_category = category.find('a').text
        with open(f'{name_category}.csv', 'w', newline='') as f:
            fieldnames = ['City', 'Region', 'Population']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            link_category = link + category.find('a').get('href')
            response = requests.get(link_category)
            soup = BeautifulSoup(response.text, 'html.parser')
            cities = soup.find('ol').find_all('li')
            for city in cities:
                city_region, population = city.text.split('\n')
                if '(' in city_region:
                    city, region = re.split('\(', city_region, maxsplit=1)
                    city = city.strip()
                    region = region[0:-1]
                else:
                    city = city_region
                    region = 'no information'
                population = re.search('\d+\s?(\d+)?\s?(\d+)?', population).group(0)
                writer.writerow({'City': city, 'Region': region, 'Population': population})
