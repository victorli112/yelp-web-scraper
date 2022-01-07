
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
# see how many times the script failed
failed = 0
def vaccine_req():
    exec_reqs('&attrs=proof_of_vaccination_required')

def staff_vaccinated():
    exec_reqs('&attrs=staff_fully_vaccinated')

#find restaurants for all cities
def exec_reqs(stri):
    for i in range(len(cities)):
        print(cities[i][0] + " " + cities[i][1])
        req_city(cities[i][0], cities[i][1], 0, stri)
        print(' ')

#find all restaurants for each city
def req_city(city, state, num, stri):
        URL = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc=' + city + '%2C%20' + state + stri + '&start=' + str(num)

        try:
            client = ScraperAPIClient('TOKEN')
            page = client.get(URL)

        except Exception:
            print('URL request failed.')
            failed = failed + 1

        soup = BeautifulSoup(page.text, 'html.parser')
        find_res(soup)

        # for every page number do the same thing
        for itemText in soup.find_all('div', class_=' border-color--default__09f24__NPAKY text-align--center__09f24__fYBGO'):
            page_num_str = itemText.find('span',{'class':' css-1e4fdj9'}).get_text()
            array = page_num_str.split(' of ')
            page_num = int(array[len(array) - 1])
            if num+10 < page_num * 10:
                req_city(city, state, num+10, stri)
            elif num+10 == page_num * 10:
                print(page_num_str)

# find all restaurants given the soup object
def find_res(soup):
    restaurants = soup.find_all('a', class_='css-1422juy', href=True)
    for i in restaurants:
      if "/biz/" in i.get('href'):
        print(i.get('href')[5:])

staff_vaccinated()
vaccine_req()
print(failed)