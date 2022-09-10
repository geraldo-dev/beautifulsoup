from selenium import webdriver
from bs4 import BeautifulSoup as bs
from time import sleep

drive = webdriver.ChromiumEdge()

drive.get('https://github.com/geraldo-dev')
page = bs(drive.page_source, 'html.parser')

sleep(2)

print(page.prettify())