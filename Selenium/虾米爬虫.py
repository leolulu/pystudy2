from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://passport.xiami.com/?redirectURL=https://www.xiami.com")

browser.find_element_by_id('account').send_keys('348699103@qq.com')
browser.find_element_by_id('password').send_keys('226818')

time.sleep(5)

browser.find_element_by_id('submit').click()






time.sleep(5)
browser.quit()