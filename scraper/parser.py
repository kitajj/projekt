from config import RAW_PATH, OUTPUT_PATH
from bs4 import BeautifulSoup
import json

def przetlumacz_dane():
    with open(RAW_PATH, "r", encoding="UTF-8") as f:
        data = f.read()
    soup = BeautifulSoup(data, "html.parser")
    prices = soup.find_all("p", class_="css-61fb99") 
    prices_final = [price.get_text(strip=True) for price in prices]

 #   print(prices_final)

    opis = soup.find_all("a", class_ = 'css-1tqlkj0')
    opis_final = [el.get('aria-label') for el in opis]
    opis_final = [i for i in opis_final if i != "None"]
    opis_final = [t for t in opis_final if t is not None]
#    print(opis_final)        

    czyste = ladniej(prices_final, opis_final)
#    print(czyste)

    with open(OUTPUT_PATH, "w", encoding="UTF-8") as f:
        json.dump(czyste, f, ensure_ascii=False, indent=4)


def ladniej(cena, opis):
    ladny_zapis = {opis[i] : cena[i] for i in range(len(cena))}
    return ladny_zapis

#   ceny_end = [i.text[1:] for i in prices]  
#    with open(OUTPUT_PATH, "w", encoding="UTF-8") as f:
#        json.dump(ceny_end, f, ensure_ascii=False, indent=4)
