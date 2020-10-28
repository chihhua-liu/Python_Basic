#demo44

# import requests
# from bs4 import BeautifulSoup
#
# URL1 = "https://www.uuu.com.tw/"
#
# response = requests.get(URL1)
# print(response.status_code, response.headers['content-type'])
#
# soup = BeautifulSoup(response.content, "html.parser")
# print(soup.title.name, soup.title.string)

#---------------------------------------------------
# demo44'
import requests
from bs4 import BeautifulSoup

URL1 = "https://www.uuu.com.tw/"

response = requests.get(URL1)
print(response.status_code, response.headers['content-type'])

soup = BeautifulSoup(response.content, "html.parser")
print(soup.title.name, soup.title.string)
# print(soup.prettify())
promotions = soup.find('div', {'id': 'MianBanner'})
# print(promotions.prettify())
links = promotions.find_all('a')
for link in links:
    print(link.get('href'))
    print(link.text)