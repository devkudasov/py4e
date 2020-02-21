from urllib.request import urlopen
import json

try:
    print(sum([comment['count'] for comment in json.loads(urlopen(input('Enter URL: ')).read())['comments']]))
except:
    quit()
