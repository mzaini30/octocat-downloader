import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://octodex.github.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
semua = soup.findAll('img', {'class' : 'lazy'})

data_gambar = []

for x in semua:
	data_gambar.append(x['data-src'])

urllib.request.urlretrieve('https://octodex.github.com' + data_gambar[0], '.' + data_gambar[0])