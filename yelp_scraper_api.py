
import requests
import time
import random
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from scraper_api import ScraperAPIClient

# List of Top 50 Cities
cities = [
    ['NewYorkCity', 'NY'],
    ['LosAngeles', 'CA'],
    ['Chicago', 'IL'],
    ['Houston', 'TX'],
    ['Phoenix', 'AZ'],
    ['Philadelphia', 'PA'],
    ['SanAntonio', 'TX'],
    ['SanDiego', 'CA'],
    ['Dallas', 'TX'],
    ['Austin', 'TX'],
    ['SanJose', 'CA'],
    ['FortWorth', 'TX'],
    ['Jacksonville', 'FL'],
    ['Columbus', 'OH'],
    ['Charlotte', 'NC'],
    ['Indianapolis', 'IN'], 
    ['SanFrancisco', 'CA'],
    ['Seattle', 'WA'],
    ['Denver', 'CO'],
    ['Washington', 'DC'],
    ['Boston', 'MA'],
    ['ElPaso', 'TX'],
    ['Nashville', 'TN'],
    ['OklahomaCity', 'OK'],
    ['LasVegas', 'NV'],
    ['Detroit', 'MI'],
    ['Portland', 'OR'],
    ['Memphis', 'TN'],
    ['Louisville', 'KY'],
    ['Milwaukee', 'WI'],
    ['Baltimore', 'MD'],
    ['Albuquerque', 'NM'],
    ['Tuscon', 'AZ'],
    ['Mesa', 'AZ'],
    ['Fresno', 'CA'],
    ['Sacramento', 'CA'],
    ['Atlanta', 'GA'],
    ['KansasCity', 'MO'],
    ['ColoradoSprings', 'CO'],
    ['Raleigh', 'NC'],
    ['Omaha', 'NE'],
    ['Miami', 'FL'],
    ['LongBeach', 'CA'],
    ['VirginiaBeach', 'VA'],
    ['Oakland', 'CA'],
    ['Minneapolis', 'MN'],
    ['Tampa', 'FL'],
    ['Tulsa', 'OK'],
    ['Arlington', 'TX'],
    ['Wichita', 'KS'],
    ]

businesses = ['nail+salon', 'tattoo+parlor', 'restaurant', 'spa', 'gym', 'hotel', 'plumbers', 'takeout', 'bar', 'lunch', 'motel', 'contractor', 'car+fixer', 'auto+repair', 'Aquariums', 'bowling', 'parks']
headers = {
            'referer' : 'https://www.google.com/',
            'authority': 'www.yelp.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-Control': 'max-age=0',
            'dnt' : '1',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

def vaccine_req():
    exec_reqs('&attrs=proof_of_vaccination_required')

def staff_vaccinated():
    exec_reqs('&attrs=staff_fully_vaccinated')

def exec_reqs(stri):
    for i in range(len(cities)):
        print(cities[i][0] + " " + cities[i][1])
        req_city(cities[i][0], cities[i][1], 0, stri)
        print(' ')

def req_city(city, state, num, stri):
        URL = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc=' + city + '%2C%20' + state + stri + '&start=' + str(num)

        try:
            client = ScraperAPIClient('TOKEN')
            page = client.get(URL)

        except Exception:
            print('URL request failed, please rerun this city.')

        soup = BeautifulSoup(page.text, 'html.parser')
        find_res(soup)

        for itemText in soup.find_all('div', class_=' border-color--default__09f24__NPAKY text-align--center__09f24__fYBGO'):
            page_num_str = itemText.find('span',{'class':' css-1e4fdj9'}).get_text()
            array = page_num_str.split(' of ')
            page_num = int(array[len(array) - 1])
            if num+10 < page_num * 10:
                req_city(city, state, num+10, stri)
            elif num+10 == page_num * 10:
                print(page_num_str)

def find_res(soup):
    restaurants = soup.find_all('a', class_='css-1422juy', href=True)
    for i in restaurants:
      if "/biz/" in i.get('href'):
        print(i.get('href')[5:])

vaccine_req()
staff_vaccinated()