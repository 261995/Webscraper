from bs4 import BeautifulSoup
from requests import get
import sqlite3
# biblioteka dla baz danych
from sys import argv

address = 'https://www.zalando.pl/mezczyzni-promocja/?sale=true'
number = 1

db = sqlite3.connect('baza1.db')
cursor=db.cursor()
# stworzenie obiektu cursor

def parse_price(price):
    return float(price.replace(' ', '').replace('zł','').replace(',', '.'))
# funkcja do sformatowania ceny do floata

def parse_from_page(number):
    page = get(f'{address}&p={number}')  # zapytanie pobrania zawartości strony
    bs = BeautifulSoup(page.content, 'html.parser')  # pobranie zawartości zapytania
    for article in bs.find_all('div', class_='hPWzFB'):
        title = article.find_all('h3',class_='u-6V88 ka2E9k uMhVZi FxZV-M _6yVObe pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2').get_text().strip()
        firm = article.find('span',class_='u-6V88 ka2E9k uMhVZi FxZV-M Kq1JPK pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2').get_text().strip()
        price = parse_price(article.find('span', class_='aajkfN wOOxir _0m5pni KVKCn3 ZkIJC- r9BRio').get_text().strip())
        # link = article.find('a')
        cursor.execute('INSERT INTO article VALUES (?, ?, ?)', (title, firm, price))
        # wpisanie zmiennych do wartości
    db.commit()

if len(argv) > 1 and argv[1] == 'setup':
    cursor.execute('''CREATE TABLE article (Item TEXT, firm TEXT, price REAL)''')
    # tworzenie tabeli zawierającej informacje o produktach
    quit

for page in range (1,10):
    number+1;
    parse_from_page(number)

db.close()
