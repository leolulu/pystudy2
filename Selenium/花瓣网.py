from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('http://huaban.com/')


r = browser.find_element_by_xpath("//div[@class='search-box']")
r.find_element_by_xpath(".//*[@id='query']").send_keys('shit')


time.sleep(5)
browser.quit()
