import requests
from lxml import etree

headers = {
    "Cookie": "ADNF=a642803401bb64e8eda3f18ee36a7435; __utma=52483902.408065444.1446641088.1492218118.1492355795.289; _ga=GA1.2.408065444.1446641088; user_id=319612; pass_hash=f2ad63ed1614fcddb823dd9fa188feec8fc7c5e6; __cfduid=d6835714e71f517ccc437fddbf831d7191519553182; _gid=GA1.2.770386208.1537882525; resize-original=1; resize-notification=1; PHPSESSID=4qi1tkndb7ba9g142inms735p6; Hm_lvt_ba7c84ce230944c13900faeba642b2b4=1536924425,1537143399,1537882525,1537960936; gelcomPoop=1; Hm_lpvt_ba7c84ce230944c13900faeba642b2b4=1537961304",
    "Referer": "https://gelbooru.com/index.php?page=post&s=list&tags=animated&pid=84",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"

}
proxies = {
    "http": "socks5://127.0.0.1:1080",
    'https': 'socks5://127.0.0.1:1080'
}

base_url = 'https://gelbooru.com/index.php?page=post&s=list&tags=animated&pid={}'

for page_num in range(10):
    try:
        r_page = requests.get(base_url.format(page_num*42))
    except:
        pass
    html = etree.HTML(r_page.content)
    item_urls = html.xpath("//div[@class='contain-push']/div[@class='thumbnail-preview']//a/@href")
    for item_url in item_urls:
        r_item = requests.get("https:"+item_url)
        item_html = etree.HTML(r_item.content)
        video_url = item_html.xpath("//video/source/@src")
        if len(video_url) > 0:
            video_url = video_url[0]
            print('downloading: ', page_num, video_url)
            with open('./public/gelbooru/'+video_url.split('/')[-1],'wb') as f:
                try:    
                    f.write(requests.get(video_url).content)
                except Exception as e:
                    print(e)
