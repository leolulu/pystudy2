import requests
from lxml import etree
import os
from tqdm import tqdm
from retrying import retry
from concurrent.futures import ThreadPoolExecutor

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
proxies = {
    "http": "socks5://127.0.0.1:1080",
    'https': 'socks5://127.0.0.1:1080'
}

BASE_DIR = r'E:\裏\图\OneDrive - Office.Inc\附件\ugirls'


def xpath_get_from_url(url, xpath):
    return etree.HTML(requests.get(url, proxies=proxies, headers=headers).content).xpath(xpath)


def requests_get(url):
    return requests.get(url, proxies=proxies, headers=headers).content


@retry(wait_fixed=2000, stop_max_attempt_number=5)
def get_all_detail_urls(next_url):
    next_url_list = xpath_get_from_url(next_url, r"//li[@class='next']/a/@href")
    detail_page_urls = xpath_get_from_url(next_url, r"//div[contains(@class,'post-wrapper')]//h2/a/@href")

    for detail_page_url in tqdm(detail_page_urls):
        from_detail_page_get_img(detail_page_url)

    if len(next_url_list) > 0:
        get_all_detail_urls(next_url_list[0])


@retry(wait_fixed=2000, stop_max_attempt_number=5)
def from_detail_page_get_img(detail_page_url):
    try:
        title = xpath_get_from_url(detail_page_url, r"//h1[@class='entry-title']/span/text()")[0]
        folder_path = os.path.join(BASE_DIR, title)
        print(title)
        if os.path.exists(folder_path):
            return
        else:
            os.makedirs(folder_path)
        inner_page_url = [detail_page_url]
        inner_page_url.extend(xpath_get_from_url(inner_page_url[0], r"//div[@class='page-links']/a/@href"))
        img_urls = []
        for url in inner_page_url:
            img_urls.extend(xpath_get_from_url(url, r"//div[@class='entry-content']/p/img/@src"))
        with ThreadPoolExecutor(4) as exe:
            for img_url in img_urls:
                exe.submit(download_img, img_url, folder_path)
    except Exception as e:
        print(e)
        raise


@retry(wait_fixed=5000, stop_max_attempt_number=20)
def download_img(img_url, folder_path):
    try:
        file_name = os.path.join(folder_path, img_url.split('/')[-1])
        if not os.path.exists(file_name):
            with open(file_name, 'wb') as f:
                f.write(requests_get(img_url))
    except Exception as e:
        print(img_url, e)
        raise


if __name__ == '__main__':
    for next_url in ['https://pibys.win/tag/ugirls/', 'https://pibys.win/tag/ugirls_app/']:
        get_all_detail_urls(next_url)
