import requests

url_lists = [
    'https://gelbooru.com//images/31/cf/31cf8416122571a02cc8e92215feab69.webm',
    'https://simg3.gelbooru.com//images/25/fc/25fced1435faabaa9e8fb37b5ecebeb5.webm',
    'https://simg3.gelbooru.com//images/bb/96/bb96901c0c0fd3240ca91c834a751424.webm',
    'https://gelbooru.com//images/4c/f1/4cf18bfe99c213664685a4c38a32c989.webm',
    'https://gelbooru.com//images/cd/ad/cdad9187ae1eb6560775e8b571b23cbd.webm'
]
i = 0

session = requests.session()

for item in url_lists:
    i += 1
    r = session.get(item)
    with open('./download/{}.webm'.format(i), 'wb') as f:
        f.write(r.content)
