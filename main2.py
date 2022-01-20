import sqlite3
# biblioteka dla baz danych
from sys import argv
import requests
from lxml import html
from bs4 import BeautifulSoup

EMAIL = 'zal.user@mytrashemail.com'
PASSWORD = 'zal.user.1234'
URL = 'https://www.zalando-lounge.pl/campaigns/ZZO1L0Z/3'

db = sqlite3.connect('baza.db')
cursor=db.cursor()
# stworzenie obiektu cursor


def parse_price(price):
    return float(price.replace(' ', '').replace('zł','').replace(',', '.'))
# funkcja do sformatowania ceny do floata

print ('1')

def main():

    URLL = 'https://www.zalando-lounge.pl/event'

    print('2')

    # Create payload
    payload = {
        "email": EMAIL,
        "password": PASSWORD,
    }

    print('3')


    with requests.Session()as s:
        p=s.post(URLL, data=payload)
        # Perform login

    print('4')

if __name__ == '__main__':
    main()

def parse_from_page():
     page = requests.get(URL)  # zapytanie pobrania zawartości strony
     bs = BeautifulSoup(page.content, 'html.parser')  # pobranie zawartości zapytania
     for div in bs.find_all('span', class_='styles__StyledText-cia9rt-0 zUiGX'):
         title = div.find_all('h3',class_='articleName___uppercase___byJM8').get_text().strip().split(',')[0]
         cursor.execute('INSERT INTO article VALUES (?, ?, ?)', (title))
         print (title)
         # wpisanie zmiennych do wartości
     print ('5')
     db.commit()

if len(argv) > 1 and argv[1] == 'setup':
    cursor.execute('''CREATE TABLE article (Item TEXT, Firm TEXT, Color TEXT, Price REAL)''')
    # tworzenie tabeli zawierającej informacje o produktach
    quit()

parse_from_page()

db.close()