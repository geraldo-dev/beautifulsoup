from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup as bs
from time import sleep

options = Options()
options.add_argument('--headless')

drive = webdriver.ChromiumEdge(options=options)

class UserGitHub:
    def __init__(self, drive):
        self.drive = drive

    def find_user_github(self, nick):
        dados = {}
        self.drive.get(f'https://github.com/{nick}')
        sleep(2)
        page = bs(self.drive.page_source, 'html.parser')
        

        name = page.find("span", class_='p-name vcard-fullname d-block overflow-hidden')
        nick_name = page.find("span", class_="p-nickname vcard-username d-block")
        description = page.find("div", class_="p-note user-profile-bio mb-3 js-user-profile-bio f4")

        dados['name'] = name.text
        dados['nick_name'] = nick_name.text
        dados['description'] = description.text

        return dados
        

user = UserGitHub(drive)
print(user.find_user_github('geraldo-dev'))