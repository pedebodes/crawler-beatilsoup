import requests
from bs4 import BeautifulSoup

op = "http://www.maconariaonline.com/lojas/?type=&busca=&dia=&estadocada=MG&cidadecada=Todas"
page = requests.get(op)
soup = BeautifulSoup(page.text, 'html.parser')
# x = soup.find_all(class_='col-md-12 alert alert-info mt-10')

# print(soup.find_all('a', td_=''))


divs = soup.findAll("table")
for div in divs:
    row = ''
    rows = div.findAll('tr')
    for row in rows:
        if(row.text.find("PHONE") > -1):
            print(row.text)

