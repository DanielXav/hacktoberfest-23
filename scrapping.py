import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

url = 'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer'

header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

site = requests.get(url, headers=header)
soup = BeautifulSoup(site.content, 'html.parser')
qtd_items = soup.find('div', id='listingCount').get_text().strip()

print(qtd_items)




