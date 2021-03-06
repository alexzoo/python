# -*- coding: utf-8 -*-

from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)


    def open_main_page(self):
        wd = self.wd
        wd.get("http://alexzoos-macbook-pro.local/addressbook/group.php")


    def destroy(self):
        self.wd.quit()

