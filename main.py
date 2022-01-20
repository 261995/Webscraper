import sqlite3
# biblioteka dla baz danych
from sys import argv
import requests
from lxml import html
from bs4 import BeautifulSoup

EMAIL = 'zal.user@mytrashemail.com'
PASSWORD = 'zal.user.1234'

db = sqlite3.connect('baza.db')
cursor=db.cursor()
# stworzenie obiektu cursor


def parse_price(price):
    return float(price.replace(' ', '').replace('zł','').replace(',', '.'))
# funkcja do sformatowania ceny do floata

print ('1')

def main():

    URL = 'https://www.zalando-lounge.pl/event'

    print('2')

    # Create payload
    payload = {
        "email": EMAIL,
        "password": PASSWORD,
    }

    print('3')

    # Perform login
    result = requests.Session().post(URL, data = payload)

    print('4')

    # Scrape url
    result = requests.Session().get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")


    result.ok
    result.status_code
    print(bucket_names)


if __name__ == '__main__':
    main()

# def parse_from_page():
#     page = requests.get(URL)  # zapytanie pobrania zawartości strony
#     bs = BeautifulSoup(page.content, 'html.parser')  # pobranie zawartości zapytania
#     for div in bs.find_all('span', class_='styles__StyledText-cia9rt-0 zUiGX'):
#         title = div.find_all('h3',class_='articleName___uppercase___byJM8').get_text().strip().split(',')[0]
#         cursor.execute('INSERT INTO article VALUES (?, ?, ?)', (title))
#         print (title)
#         # wpisanie zmiennych do wartości
#     print ('1')
#     db.commit()

if len(argv) > 1 and argv[1] == 'setup':
    cursor.execute('''CREATE TABLE article (Item TEXT, Firm TEXT, Color TEXT, Price REAL)''')
    # tworzenie tabeli zawierającej informacje o produktach
    quit()

# parse_from_page()

db.close()