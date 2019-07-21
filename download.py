import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://octodex.github.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
semua = soup.findAll('img', {'class' : 'lazy'})

for x in semua:
	print(x['data-src'])