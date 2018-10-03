from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()

browser.get("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1538585588341&di=22845fa476382089ce91a1d611ec6568&imgtype=jpg&src=http%3A%2F%2Fimg2.imgtn.bdimg.com%2Fit%2Fu%3D1815276212%2C1041795570%26fm%3D214%26gp%3D0.jpg")

print(browser.page_source)
sleep(5)

browser.quit()