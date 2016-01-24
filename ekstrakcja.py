import requests
from bs4 import BeautifulSoup

url = "http://olx.pl/gdansk/q-konsola/?search%5Bdist%5D=5"
r = requests.get(url)

soup = BeautifulSoup(r.content)

g_data = soup.find_all("a", {"class": "marginright5 link linkWithHash detailsLink"})

for item in g_data:
    print item.text