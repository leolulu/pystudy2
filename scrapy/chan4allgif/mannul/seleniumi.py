from selenium import webdriver


co = webdriver.chrome.options.Options()
co.add_argument('--headless')

browser = webdriver.Chrome(chrome_options=co)

browser.get('https://www.beastforum.com/showtopic-123113.html')

with open('./start.html', 'w', encoding='utf-8') as f:
    f.write(
        browser.page_source
    )
