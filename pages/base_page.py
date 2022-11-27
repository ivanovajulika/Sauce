import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
BTN_CART = (By.ID, "shopping_cart_container")
BTN_SIDEBAR = (By.ID, "react-burger-menu-btn")
MENU_RESET = (By.ID, "reset_sidebar_link")
MENU_ALL_ITEMS = (By.ID, "inventory_sidebar_link")
CROSS_BTN = (By.ID, "react-burger-cross-btn")


class BasePage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open_page(self):
        self.browser.get(self.link)

    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    # получить значение счетчика на кнопке Корзина и сравнить с quantity
    def cart_counter(self, quantity):
        text = self.browser.find_element(*CART_BADGE).text
        assert text == quantity

    def go_to_cart(self):
        self.browser.find_element(*BTN_CART).click()

    # получить значение счетчика на кнопке Корзина и сравнить с ''
    # счетчик пуст
    def empty_cart_counter(self):
        text = self.browser.find_element(*CART_BADGE).text
        assert text == ""

    def element_cart(self):
        self.browser.find_element(*BTN_CART)

    def reset_cart(self):
        self.browser.find_element(*BTN_SIDEBAR).click()
        self.browser.find_element(*MENU_RESET).click()
        wait = WebDriverWait(self.browser, 10)
        cross_btn = wait.until(EC.presence_of_element_located(CROSS_BTN))
        cross_btn.click()

    def return_to_inventory_page(self):
        self.browser.find_element(*BTN_SIDEBAR).click()
        self.browser.find_element(*MENU_ALL_ITEMS).click()
