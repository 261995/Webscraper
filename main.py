import sqlite3
# biblioteka dla baz danych
from sys import argv
import requests
from bs4 import BeautifulSoup

address = 'https://www.zalando-lounge.pl/campaigns/ZZO1L0Z/3'

db = sqlite3.connect('baza1.db')
cursor=db.cursor()
# stworzenie obiektu cursor

def parse_price(price):
    return float(price.replace(' ', '').replace('zł','').replace(',', '.'))
# funkcja do sformatowania ceny do floata

def parse_from_page():
    page = requests.get(address)  # zapytanie pobrania zawartości strony
    bs = BeautifulSoup(page.content, 'html.parser')  # pobranie zawartości zapytania
    for div in bs.find_all('span', class_='styles__StyledText-cia9rt-0 zUiGX'):
        title = div.find_all('h3',class_='articleName___uppercase___byJM8').get_text().strip().split(',')[0]
        cursor.execute('INSERT INTO article VALUES (?)', (title))
        # wpisanie zmiennych do wartości
    db.commit()

if len(argv) > 1 and argv[1] == 'setup':
    cursor.execute('''CREATE TABLE article (Item TEXT)''')
    # tworzenie tabeli zawierającej informacje o produktach
    quit()

# for page in range (1,10):
#     parse_from_page(number)

db.close()