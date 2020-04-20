import requests
from bs4 import BeautifulSoup

url = "https://www.books.com.tw/web/sys_bbotm/books/020806/?loc=P_0001_3_006"

for times in range(3):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.select('h4 a') 
    paging = soup.select('.nxt')
    next_url = paging[0]['href']
    url = next_url
    for each_title in articles:
        print(each_title.text, each_title['href'])