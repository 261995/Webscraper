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

search = input("Wpisz frazę którą chcesz wyszukać:")

URL = f"https://www.wykop.pl/szukaj/{search}/?"
page = requests.get(URL).text  # zapytanie pobrania zawartości strony
bs = BeautifulSoup(page, 'html.parser')  # pobranie zawartości zapytania

page_text = bs.find('div', class_='wblock rbl-block pager').p
pages = int(str(page_text).split('</a')[-3].split('>')[-1])

for page in range(1, pages + 1):
    URL2 = f"https://www.wykop.pl/szukaj/{search}/strona/{pages}/"
    page = requests.get(URL2).text  # zapytanie pobrania zawartości strony
    bs = BeautifulSoup(page, 'html.parser')  # pobranie zawartości zapytania

    div = bs.find('div', class_='indent')
    items = div.find_all(text=re.compile(search))

    for item in div:
        parent = item.parent
        if parent.name !='a':
            continue
        link = parent['href']
        next_parent = item.find_parent(class_='h2')
        title = next_parent.find('title')
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

db.close()