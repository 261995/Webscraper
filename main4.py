import sqlite3
# biblioteka dla baz danych
from sys import argv
import requests
from bs4 import BeautifulSoup
import re

# EMAIL = 'zal.user@mytrashemail.com'
# PASSWORD = 'zal.user.1234'

db = sqlite3.connect('baza.db')
cursor=db.cursor()
# stworzenie obiektu cursor


def parse_from_page():

    URL = 'https://www.wykop.pl/najnowsze/'

    page = requests.get(URL)  # zapytanie pobrania zawartości strony
    bs = BeautifulSoup(page.content, 'html.parser')  # pobranie zawartości zapytania

    for h2 in bs.find_all('li', class_='link iC'):
        tag = h2.find()
        # print(h2)
        title = h2.find('p').get_text()
        print(title)
    # tags = bs.find_all('a', class_='tag affect create')
    # print(tags)

    # items = bs.find_all("ul", id="articleListWrapper")
    # title = bs.find_all("div", class_="styles__StyledText-cia9rt-0 zUiGX").get_text().strip().split(' - ')
    # firm = bs.find_all("span", class_="articleName___uppercase___byJM8").get_text().strip()
    # color = bs.find_all("span", class_="styles__StyledText-cia9rt-0 zUiGX").get_text().strip().split(' - ')
    # size = bs.find_all("span", class_="styles__StyledText-cia9rt-0 ljhdMk").get_text()
    # price = bs.find_all("span", class_="styles__StyledText-cia9rt-0 ixsQUL").get_text().strip().split('&')

    # cursor.execute('INSERT INTO article VALUES (?, ?, ?)', (title, firm, color, size, price))
    # wpisanie zmiennych do wartości

    # print(title)
    # print ('koniec parse')

    db.commit()

# def parse_from_page2():
#
#     page2URL = 'https://www.zalando-lounge.pl/campaigns/ZZO1KHB/1'
#
#
#     page = requests.get(page2URL)  # zapytanie pobrania zawartości strony
#     bs = BeautifulSoup(page.text, 'html.parser')  # pobranie zawartości zapytania
#     # print (bs)
#
#     items = bs.find_all("ul", id="articleListWrapper")
#     title = bs.find_all("div", class_="styles__StyledText-cia9rt-0 zUiGX").get_text().strip().split(' - ')
#     firm = bs.find_all("span", class_="articleName___uppercase___byJM8").get_text().strip()
#     color = bs.find_all("span", class_="styles__StyledText-cia9rt-0 zUiGX").get_text().strip().split(' - ')
#     size = bs.find_all("span", class_="styles__StyledText-cia9rt-0 ljhdMk").get_text()
#     price = bs.find_all("span", class_="styles__StyledText-cia9rt-0 ixsQUL").get_text().strip().split('&')
#
#     cursor.execute('INSERT INTO article VALUES (?, ?, ?)', (title, firm, color, size, price))
#     # wpisanie zmiennych do wartości
#
#     # print(title)
#     # print ('koniec parse')
#
#     db.commit()
#
# def parse_from_page3():
#
#     page3URL = 'https://www.zalando-lounge.pl/campaigns/ZZO1MAY/1'
#
#
#     page = requests.get(page3URL)  # zapytanie pobrania zawartości strony
#     bs = BeautifulSoup(page.text, 'html.parser')  # pobranie zawartości zapytania
#     # print (bs)
#
#     items = bs.find_all("ul", id="articleListWrapper")
#     title = bs.find_all("div", class_="styles__StyledText-cia9rt-0 zUiGX").get_text().strip().split(' - ')
#     firm = bs.find_all("span", class_="articleName___uppercase___byJM8").get_text().strip()
#     color = bs.find_all("span", class_="styles__StyledText-cia9rt-0 zUiGX").get_text().strip().split(' - ')
#     size = bs.find_all("span", class_="styles__StyledText-cia9rt-0 ljhdMk").get_text()
#     price = bs.find_all("span", class_="styles__StyledText-cia9rt-0 ixsQUL").get_text().strip().split('&')
#
#     cursor.execute('INSERT INTO article VALUES (?, ?, ?)', (title, firm, color, size, price))
#     # wpisanie zmiennych do wartości
#
#     # print(title)
#     # print ('koniec parse')
#
#     db.commit()
#
# if len(argv) > 1 and argv[1] == 'setup':
#     cursor.execute('''CREATE TABLE article (Item TEXT, Firm TEXT, Color TEXT, Size TEXT, Price REAL)''')
#     # tworzenie tabeli zawierającej informacje o produktach
#     quit()

parse_from_page()
# parse_from_page1()
# parse_from_page2()
# parse_from_page3()

db.close()