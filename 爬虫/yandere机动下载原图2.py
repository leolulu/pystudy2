import re
import requests

pic_num = 0
page_counter = 0
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
}
base_url = 'https://yande.re/post?page={}&tags=girls_frontline'

session = requests.session()

while page_counter < 33:
    r = session.get(base_url.format(page_counter), headers=headers)

    for i in set(re.findall(r'https://files.yande.re/[jpeg|image].*?\.(?:jpg|png)', r.content.decode())):
        print('url: ', i)
        pic_name = re.findall(r'yande.re%(.*?)\.(?:jpg|png)',
                              i)[-1].replace('%20', '_')
        print('pic_name: ', pic_name)
        img = session.get(i, headers=headers)
        with open('./public/gelbooru/{}.jpg'.format(pic_name), 'wb') as f:
            f.write(img.content)
        print('pic_num: ', pic_num)
        pic_num += 1

    page_counter += 1
