import sqlite3
# biblioteka dla baz danych
from sys import argv
import requests
from bs4 import BeautifulSoup

EMAIL = 'zal.user@mytrashemail.com'
PASSWORD = 'zal.user.1234'

db = sqlite3.connect('baza.db')
cursor=db.cursor()
# stworzenie obiektu cursor


# def parse_price(price):
#     return float(price.replace(' ', '').replace('zł','').replace(',', '.'))
# funkcja do sformatowania ceny do floata

def main():

    URL = 'https://www.zalando-lounge.pl/event'

    # Create payload
    payload = {
        "email": EMAIL,
        "password": PASSWORD,
    }

    # Perform login
    result = requests.Session().post(URL, data = payload)

if __name__ == '__main__':
    main()

# Scrape url
def parse_from_page():
    pageURL = 'https://www.zalando-lounge.pl/campaigns/ZZO1M4A/1'
    page = requests.get(pageURL)  # zapytanie pobrania zawartości strony
    bs = BeautifulSoup(page.text, 'html.parser')  # pobranie zawartości zapytania

    print (bs)

    title = bs.find_all(text='Kurtka')
    # cursor.execute('INSERT INTO article VALUES (?, ?, ?)', (title, color, price))
    # wpisanie zmiennych do wartości

    print("Title:")
    print(title)
    print ('koniec parse')

    # db.commit()

if len(argv) > 1 and argv[1] == 'setup':
    cursor.execute('''CREATE TABLE article (Item TEXT, Color TEXT, Price REAL)''')
    # tworzenie tabeli zawierającej informacje o produktach
    quit()

parse_from_page()

db.close()