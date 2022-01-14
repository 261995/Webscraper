from bs4 import BeautifulSoup
from requests import get


adr = 'https://www.zalando.pl/mezczyzni-promocja/?sale=true'
print ('1')
page = get(adr) # zapytanie pobrania zawartości strony
print ('2')
bs = BeautifulSoup(page.content, 'html.parser') # pobranie zawartości zapytania


for offer in bs.find_all('div', class_='hPWzFB'):
# for offer in bs.find_all('div', class_='kpgVnb w8MdNG cYylcv QylWsg _75qWlu iOzucJ JT3_zV DvypSJ'):
    header = offer.find_all('span', class_='u-6V88 ka2E9k uMhVZi FxZV-M Kq1JPK pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2')
    local = offer.find_all('h3', class_='u-6V88 ka2E9k uMhVZi FxZV-M _6yVObe pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2').get_text().strip().split(',')[0]
    print(header)
    break




