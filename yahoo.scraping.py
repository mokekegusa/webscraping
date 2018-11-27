import requests
from bs4 import BeautifulSoup
import re

target_url = "https://www.yahoo.co.jp/"


r = requests.get(target_url)
soup = BeautifulSoup(r.text, 'lxml')

with open('originDataOld.html', mode='w', encoding = 'utf-8') as fw:
    fw.write(soup.prettify())

elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
for e in elems:
    print(e.getText())
