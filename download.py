import requests
import urllib.request
from bs4 import BeautifulSoup

url = 'https://octodex.github.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
semua = soup.findAll('img', {'class' : 'lazy'})

data_gambar = []

for x in semua:
	data_gambar.append('https://octodex.github.com' + x['data-src'])

print(data_gambar)