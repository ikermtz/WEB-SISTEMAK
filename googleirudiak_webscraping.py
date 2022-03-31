# -*- coding:UTF-8-*-

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# REQUESTS --> deskargatutako HTML
# params:
#   q: bilaketa terminoa
#   tbm: google zerbitzua
uri = "https://www.google.com/search?q=pinarello+f12&tbm=isch"
headers = {'Host' :'www.google.com',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}

erantzuna = requests.get(uri, headers=headers, allow_redirects=False)
kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)
html = erantzuna.content
file = open("google_img_search_results.html", "wb")
file.write(html)
file.close()

#SELENIUM + GECKODRIVER --> renderizar HTML
browser = webdriver.Firefox()
browser.get(uri)
WebDriverWait(browser, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "rg_i.Q4LuWd")))
html = browser.page_source
browser.close()


# html-a parseatu
soup = BeautifulSoup(html, 'html.parser')
# DOM zuhaitzean "class" atributuaren balioa "rg_i Q4LuWd" duten irudi guztiak bilatu
img_results = soup.find_all('img', {'class': 'rg_i Q4LuWd'})

for idx, each in enumerate(img_results):
    src = ""
    if each.has_attr('src'):
        src = each['src']
    else:
        src = each['data-src']
    print(str(idx) + " " + src)