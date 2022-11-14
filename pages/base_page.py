from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class BasePage():

    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open_page(self):
        self.browser.get(self.link)
