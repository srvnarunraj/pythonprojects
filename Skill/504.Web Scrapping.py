import requests
import bs4 as bs4
import html5lib

URL = "https://amazon.com"
r = requests.get(URL)
contents = r.content
bsoup = bs4.BeautifulSoup(contents,'html.parser')
print(bsoup.prettify())
# print(bsoup.title.text)

# images = []
# for img in bsoup.findAll('img'):
#     images.append(img.get('src'))
#
# print(images)