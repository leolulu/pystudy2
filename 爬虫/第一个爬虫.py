import requests

r = requests.get('http://konachan.net/images/6.gif')

with open('./shit.gif','wb') as f:
    f.write(r.content)