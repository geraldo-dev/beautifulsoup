from selenium import webdriver
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup as bs
from time import sleep

options = Options()
options.add_argument('--headless')

drive = webdriver.ChromiumEdge(options=options)

drive.get('https://github.com/geraldo-dev')
sleep(2)
page = bs(drive.page_source, 'html.parser')


name = page.find("span", class_='p-name vcard-fullname d-block overflow-hidden')
nick_name = page.find("span", class_="p-nickname vcard-username d-block")
description = page.find("div", class_="p-note user-profile-bio mb-3 js-user-profile-bio f4")

print('-->', nick_name.get_text())