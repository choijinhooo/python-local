import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'

rp = requests.get(url).text
soup = BeautifulSoup(rp,'html.parser')
select = soup.select_one("#KOSPI_now")
print(select.text)