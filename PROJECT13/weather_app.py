import requests
from bs4 import BeautifulSoup

search = "weather in Ikeja"
url = f"https://www.google/com/search?7q={search}"

r = requests.get(url)

s = BeautifulSoup(r.text, 'html.parser')

update = s.find('div', class_='BNEawe').text

print(update)