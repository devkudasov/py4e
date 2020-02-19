from bs4 import BeautifulSoup
from urllib.request import urlopen

print(sum([int(tag.contents[0]) for tag in BeautifulSoup(urlopen('http://py4e-data.dr-chuck.net/comments_373035.html').read(), 'html.parser')('span')]))
