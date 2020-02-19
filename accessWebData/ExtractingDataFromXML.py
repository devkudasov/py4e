from urllib.request import urlopen
from xml.etree import ElementTree as et

try:
    print(sum([int(comment.find('count').text) for comment in et.fromstring(urlopen(input('Enter URL: ')).read()).findall('comments/comment')]))
except:
    quit()
