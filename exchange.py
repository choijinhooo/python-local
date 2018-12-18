import requests
from bs4 import BeautifulSoup

url = "http://m.exchange.daum.net/mobile/exchange/exchangeMain.daum"
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')
exchanges = soup.select("#asiaBody > table > tbody > tr")


for exchange in exchanges:
     print(exchange.select_one("td.name").text)
     print(exchange.select_one("td.idx").text)
     print("----------")

exchanges = soup.select("#mideastBody > table > tbody > tr")


for exchange in exchanges:
     print(exchange.select_one("td.name").text)
     print(exchange.select_one("td.idx").text)
     print("----------")

exchanges = soup.select("#aficaBody > table > tbody > tr")


for exchange in exchanges:
     print(exchange.select_one("td.name").text)
     print(exchange.select_one("td.idx").text)
     print("----------")

exchanges = soup.select("#europeBody > table > tbody > tr")


for exchange in exchanges:
     print(exchange.select_one("td.name").text)
     print(exchange.select_one("td.idx").text)
     print("----------")





