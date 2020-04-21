import requests
from bs4 import BeautifulSoup
url = "https://www.books.com.tw/web/sys_bbotm/books/020806/?loc=P_0001_3_006"
for times in range(5):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    title = soup.select('h4 a')
    pagging = soup.select('.cnt_page a')
    price = soup.select('strong+ strong')
    next_url = pagging[4]['href']
    url = next_url
    for each_title,each_price in zip(title, price):
        print('書名:',each_title.text, ' 售價:',each_price.get_text())