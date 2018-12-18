import requests
from bs4 import BeautifulSoup

url = "http://lostark.game.onstove.com/News/Notice/List"
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')
losts = soup.select("#list > div.list.list--default > ul > li")

for lost in losts:
     print(lost.select_one("div.list__subject").text)
     print(lost.select_one("div.list__date").text)
     print("----------")

