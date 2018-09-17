import re
import requests

pic_num = 0
page_counter = 0
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
}
base_url = 'https://gelbooru.com/index.php?page=post&s=list&pid={}'

session = requests.session()

while page_counter < 20:
    r = session.get(base_url.format(page_counter*42), headers=headers)

    for i in re.findall('<img src="(http.*?)"', r.content.decode()):
        print('url: ',i)
        pic_name = re.findall('thumbnail_(.*?).jpg',i)[0]
        img = session.get(i, headers=headers)
        with open('./public/gelbooru/{}.jpg'.format(pic_name), 'wb') as f:
            f.write(img.content)
        print('pic_num: ',pic_num)
        pic_num += 1

    page_counter += 1
