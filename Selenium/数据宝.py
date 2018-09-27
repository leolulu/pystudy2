from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

try:
    os.remove('./Selenium/html/数据宝.html')
except:
    pass

browser = webdriver.Chrome(executable_path='./chromedriver.exe')
browser.get('http://172.168.3.33:8800/reportmis/mis2/index.jsp')
browser.find_element_by_id('username').send_keys('1000001')
browser.find_element_by_id('password').send_keys('0743031166')
browser.find_element_by_id('login-button').click()

time.sleep(3)

browser.switch_to.frame('contentFrame')
browser.find_element_by_xpath("//a[text()='资源管理']").click()

time.sleep(3)

browser.switch_to.frame("resourceExplorer")
browser.switch_to.frame("resourceListFrame")

for temp in range(5):
    js="var q=document.documentElement.scrollTop=100000"
    browser.execute_script(js)
    time.sleep(1)

text = browser.find_elements_by_xpath("//table//tr/td[3]//a")

for t in text:
    print(t.text)

# main_page_html = browser.page_source
# with open('./Selenium/html/数据宝.html','w',encoding='utf-8') as f:
#     f.write(main_page_html)


time.sleep(5)
browser.quit()
