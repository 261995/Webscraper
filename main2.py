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


# def parse_price(price):
#     return float(price.replace(' ', '').replace('zł','').replace(',', '.'))
# funkcja do sformatowania ceny do floata


def main():

    url = "https://www.zalando-lounge.pl/campaigns/ZZO1M4A/1"

    payload = {
        "email": EMAIL,
        "password": PASSWORD,
    }

    headers = {
        "cookie": "zl_customer=eyJnZW5kZXIiOiIiLCJyb2xlIjoiZ3Vlc3QifQ%3D%3D; zl_deeplink=%2Fcampaigns%2FZZO1M4A%2F1; Zalando-Client-Id=b57cbb97-da5a-4ad8-a97b-9654b4cab7c9; _abck=4CD8171C2F80615EEC0A87B675A3496E~-1~YAAQf2ReaNWCd3h%2BAQAAdQ%2FAeQdi8O7nI9btBdIaYE3VK0ygrADiwrP%2FeB39uPV9nn5at0Q6bH3y6gHgtwGunDw0o984i1YR9F7kWYUDxkRl5EIaW1br65UMIYwvfs%2BeK4oCvQptnV3ZhEnBbvySsaALXbmbuBEfa0%2BFlEXyIp8IMz%2FHI7VQUvrKSFBWEPJ6gODeV1DdpBCyWk%2BfeJ4665B8T6qc6p6yn73hUiiM%2B4ptnlG8VWzpx2tAkbJOhCwTa2GRJJ9ToSEK7%2FW6r0vDWP2tLpCm2ZOWJgc7LZKN%2F95kJxeYoY2LNBBBdeM1xFs35FM%2FCW6GF1RulQ8RCfc0TiIi6FIYlWwJHwp6ZGS5zNo%2Fe5gBa7qEFYOZVVOYI6%2FOodZbyFq1ub%2FEO%2F6yAG8bPFSAzzcJw%2FioPybG%2Fxfp6xTttfI%3D~-1~-1~-1; zl_webviewos=; zl_webview_ga_cid=; zl_webview_ga_tid=; zl_webview_appversion=",
        "Authorization": "Basic emFsLnVzZXJAbXl0cmFzaGVtYWlsLmNvbTp6YWwudXNlcjEyMzQ="
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

if __name__ == '__main__':
    main()

def parse_from_page():

    pageURL = 'https://www.zalando-lounge.pl/campaigns/ZZO1M4A/1'


    page = requests.get(pageURL)  # zapytanie pobrania zawartości strony
    bs = BeautifulSoup(page.text, 'html.parser')  # pobranie zawartości zapytania
    # print (bs)


    title = bs.find_all(text='Kurtka')
    # cursor.execute('INSERT INTO article VALUES (?, ?, ?)', (title, color, price))
    # wpisanie zmiennych do wartości

    print("Title:")
    print(title)
    print ('koniec funkcji')

    # db.commit()

if len(argv) > 1 and argv[1] == 'setup':
    cursor.execute('''CREATE TABLE article (Item TEXT, Firm TEXT, Color TEXT, Price REAL)''')
    # tworzenie tabeli zawierającej informacje o produktach
    quit()

parse_from_page()

db.close()