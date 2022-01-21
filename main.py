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
def parse_from_page1():

    page1URL = 'https://www.zalando-lounge.pl/campaigns/ZZO1M4A/1'


    page = requests.get(page1URL)  # zapytanie pobrania zawartości strony
    bs = BeautifulSoup(page.text, 'html.parser')  # pobranie zawartości zapytania
    # print (bs)


    title = bs.find_all("div", class_="styles__StyledText-cia9rt-0 zUiGX").get_text().strip().split(' - ')
    firm = bs.find_all("span", class_="articleName___uppercase___byJM8").get_text().strip()
    color = bs.find_all("span", class_="styles__StyledText-cia9rt-0 zUiGX").get_text().strip().split(' - ')
    size = bs.find_all("span", class_="styles__StyledText-cia9rt-0 ljhdMk").get_text()
    price = bs.find_all("span", class_="styles__StyledText-cia9rt-0 ixsQUL").get_text().strip().split('&')

    cursor.execute('INSERT INTO article VALUES (?, ?, ?)', (title, firm, color, size, price))
    # wpisanie zmiennych do wartości

    # print(title)
    # print ('koniec parse')

    db.commit()

def parse_from_page2():

    page2URL = 'https://www.zalando-lounge.pl/campaigns/ZZO1KHB/1'


    page = requests.get(page2URL)  # zapytanie pobrania zawartości strony
    bs = BeautifulSoup(page.text, 'html.parser')  # pobranie zawartości zapytania
    # print (bs)


    title = bs.find_all("div", class_="styles__StyledText-cia9rt-0 zUiGX").get_text().strip().split(' - ')
    firm = bs.find_all("span", class_="articleName___uppercase___byJM8").get_text().strip()
    color = bs.find_all("span", class_="styles__StyledText-cia9rt-0 zUiGX").get_text().strip().split(' - ')
    size = bs.find_all("span", class_="styles__StyledText-cia9rt-0 ljhdMk").get_text()
    price = bs.find_all("span", class_="styles__StyledText-cia9rt-0 ixsQUL").get_text().strip().split('&')

    cursor.execute('INSERT INTO article VALUES (?, ?, ?)', (title, firm, color, size, price))
    # wpisanie zmiennych do wartości

    # print(title)
    # print ('koniec parse')

    db.commit()

def parse_from_page3():

    page3URL = 'https://www.zalando-lounge.pl/campaigns/ZZO1MAY/1'


    page = requests.get(page3URL)  # zapytanie pobrania zawartości strony
    bs = BeautifulSoup(page.text, 'html.parser')  # pobranie zawartości zapytania
    # print (bs)


    title = bs.find_all("div", class_="styles__StyledText-cia9rt-0 zUiGX").get_text().strip().split(' - ')
    firm = bs.find_all("span", class_="articleName___uppercase___byJM8").get_text().strip()
    color = bs.find_all("span", class_="styles__StyledText-cia9rt-0 zUiGX").get_text().strip().split(' - ')
    size = bs.find_all("span", class_="styles__StyledText-cia9rt-0 ljhdMk").get_text()
    price = bs.find_all("span", class_="styles__StyledText-cia9rt-0 ixsQUL").get_text().strip().split('&')

    cursor.execute('INSERT INTO article VALUES (?, ?, ?)', (title, firm, color, size, price))
    # wpisanie zmiennych do wartości

    # print(title)
    # print ('koniec parse')

    db.commit()

if len(argv) > 1 and argv[1] == 'setup':
    cursor.execute('''CREATE TABLE article (Item TEXT, Firm TEXT, Color TEXT, Size TEXT, Price REAL)''')
    # tworzenie tabeli zawierającej informacje o produktach
    quit()

parse_from_page1()
parse_from_page2()
parse_from_page3()

db.close()