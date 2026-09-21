from config import BASE_URL, RAW_PATH, HEADERS
from bs4 import BeautifulSoup
import requests
import os


def pobierz_dane():
    

    with open(RAW_PATH, 'w', encoding='UTF-8') as f:
        for i in range(1, 25):
            if i == 1:
                response = requests.get(BASE_URL, headers=HEADERS)            
                f.write(response.text)
            else:
                response = requests.get(f'https://www.olx.pl/muzyka-edukacja/ksiazki/podreczniki-szkolne/q-podreczniki-liceum-i-technikum/?page={i}', headers=HEADERS)                
                f.write(response.text)

def usun_dane():
    try:
        os.remove(RAW_PATH)
    except Exception as e:
        print(e)
    

