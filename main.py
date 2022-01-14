from bs4 import BeautifulSoup
from requests import get

adr = 'https://www.zalando.pl/mezczyzni-promocja/?sale=true'
print ('1')
page = get(adr) # zapytanie pobrania zawartości strony
print ('2')
bs = BeautifulSoup(page.content, 'html.parser') # pobranie zawartości zapytania


for kpgVnb in bs.find_all('div', class_='kpgVnb w8MdNG cYylcv QylWsg _75qWlu iOzucJ JT3_zV DvypSJ'):
    print(kpgVnb)
    print('slowo')





