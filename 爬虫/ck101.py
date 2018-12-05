from lxml import etree
from selenium import webdriver
import pandas as pd
from time import sleep


co = webdriver.ChromeOptions()
# co.add_argument('--headless')
# co.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options=co)
url = "https://ck101.com/forum.php?mod=forumdisplay&fid=70&page={}"

article_data = pd.DataFrame({
    'page_num': [],
    'title': []
}, dtype='int32')

for i in range(671):
    page_num = i+1
    browser.get(url.format(page_num))
    print(url.format(page_num))
    sleep(10)
    xpath_result = etree.HTML(browser.page_source).xpath("//div[@class='titleBox']//a/@title")
    

    for title in xpath_result:
        print(page_num,title)
        article_data = article_data.append(pd.DataFrame({'page_num':[page_num],'title':[title]}),ignore_index=True)
    print(article_data)

    article_data.to_excel('./download/{}.xlsx'.format(page_num))

print(xpath_result)
