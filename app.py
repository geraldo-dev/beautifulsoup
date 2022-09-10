from selenium import webdriver
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup as bs
from time import sleep

options = Options()
options.add_argument('--headless')

drive = webdriver.ChromiumEdge(options=options)

drive.get('https://github.com/geraldo-dev')
page = bs(drive.page_source, 'html.parser')

sleep(2)

title_page = page.title.text
d = page.find("h1").find_all('span')[-1].text

print(type(d),d)