import bs4
from bs4 import BeautifulSoup
import requests
import sys

URL = 'your_library_url.com'

res = requests.get(URL)
res.raise_for_status()

makeSoup = bs4.BeautifulSoup(res.text, 'html.parser')
titles = makeSoup.select('title')

for title in titles:
    title = str(title).split('>')
    title = title[1].split('<')
    title = title[0]
    print(title)
