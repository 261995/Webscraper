import requests
from bs4 import BeautifulSoup

address = 'https://www.zalando-lounge.pl/event#'

response = requests.get(address)  # zapytanie pobrania zawartości strony
bs = BeautifulSoup(response.content, 'html.parser')
print(bs)