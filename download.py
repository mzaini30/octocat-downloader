import requests
import urllib.request
from bs4 import BeautifulSoup

url = 'https://octodex.github.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
semua = soup.findAll('img', {'class' : 'lazy'})

data_gambar = []

for x in semua:
	data_gambar.append(x['data-src'])

for x in data_gambar:
	urllib.request.urlretrieve('https://octodex.github.com' + x, '.' + x)
	print(x.replace('/images/', '') + ' sudah didownload')