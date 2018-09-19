import requests
from lxml import etree
import os

session = requests.session()
header={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    "cookie": "__cfduid=d903e3abeaca2effe91e7b839a96be7211527491373; _ga=GA1.3.1213173136.1527491373; _ga=GA1.2.2716196.1533521826; _gid=GA1.2.2067292582.1537358233; _gid=GA1.3.2067292582.1537358233; Hm_lvt_ba7c84ce230944c13900faeba642b2b4=1537359428,1537361149,1537362700,1537363469; Hm_lpvt_ba7c84ce230944c13900faeba642b2b4=1537363858"
}

r = session.get('https://boards.4chan.org/s/catalog',headers = header)

base_html = etree.HTML(r.content)
print(
    etree.tostring(base_html).decode()
)

threads = base_html.xpath("//div[@class='thread']")

for thread in threads:
    thread_url = thread.xpath("./a/@href")[0]
    thread_name = thread.xpath("./div[@class='teaser']/b/text()")[0]
    print('开始处理thread: ', thread_name)

    in_r = session.get('https:' + thread_url)
    in_html = etree.HTML(in_r.content)

    post_container = in_html.xpath("//div[contains(@class,'postContainer')]")

    try:
        os.makedirs('./public/4chan/'+thread_name)

        for post in post_container:
            imgs = post.xpath(".//a[@class='fileThumb']/@href")
            print(imgs)
            f_name = post.xpath(".//div[@class='fileText']/a/text()")
            print(f_name)

            if len(imgs) > 0:
                print('downloading: ', f_name[0])
                img = session.get('https:' + imgs[0])
                with open('./public/4chan/'+thread_name+'/' + f_name[0], 'wb') as f:
                    f.write(img.content)
    except:
        print('新建文件夹失败，跳过该thread.')
