from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://py4e-data.dr-chuck.net/known_by_Anton.html'
name = 'Fikret'

for i in range(7):
    tags = BeautifulSoup(urlopen(url).read(), 'html.parser')('a')
    name = tags[17].contents[0]
    url = tags[17].get('href', None)

print(name)
