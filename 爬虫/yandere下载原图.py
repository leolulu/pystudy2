import re
import requests

pic_num = 0
page_counter = 0
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
}
base_url = 'https://yande.re/post?page={}'

session = requests.session()

while page_counter < 20:
    r = session.get(base_url.format(page_counter), headers=headers)

    for i in re.findall('https://files.yande.re/jpeg.*?.jpg', r.content.decode()):
        print('url: ',i)
        pic_name = re.findall('yande.re%(.*?).jpg',i)[-1].replace('%20','_')
        print('pic_name: ',pic_name)
        img = session.get(i, headers=headers)
        with open('./public/gelbooru/{}.jpg'.format(pic_name), 'wb') as f:
            f.write(img.content)
        print('pic_num: ',pic_num)
        pic_num += 1

    page_counter += 1