import requests
from bs4 import BeautifulSoup

address = 'https://www.zalando-lounge.pl/campaigns/ZZO1L0Z/3'

page = requests.get(address)  # zapytanie pobrania zawartości strony
bs = BeautifulSoup(page.content, 'html.parser')  # pobranie zawartości zapytania
print (bs)

for articleListWrapper in bs.find_all('ul', class_='ArticlesListstyles__ListWrapper-do0tac-0 fZxbGo'):
    print('1')
    title = page.find_all('span',class_='articleName___uppercase___byJM8').get_text().strip().split(',')[0]
    print('2')
    print (title)