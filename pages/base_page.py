from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
BTN_CART = (By.ID, "shopping_cart_container")
BTN_SIDEBAR = (By.ID, "react-burger-menu-btn")
MENU_ABOUT = (By.ID, "about_sidebar_link")
MENU_LOGOUT = (By.ID, "logout_sidebar_link")
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
        assert "inventory" in self.browser.current_url, "Wrong page"

    def should_be_menu_sidebar(self):
        self.browser.find_element(*BTN_SIDEBAR).click()
        assert self.element_is_present(*MENU_ALL_ITEMS), "Element is absent"
        assert self.element_is_present(*MENU_ABOUT), "Element is absent"
        assert self.element_is_present(*MENU_LOGOUT), "Element is absent"
        assert self.element_is_present(*MENU_RESET), "Element is absent"
        self.browser.find_element(*CROSS_BTN).click()

    def go_to_about(self):
        self.browser.find_element(*BTN_SIDEBAR).click()
        self.browser.find_element(*MENU_ABOUT).click()
        assert "saucelabs.com" in self.browser.current_url, "Wrong page"
        self.browser.back()

    def go_to_logout(self):
        self.browser.find_element(*BTN_SIDEBAR).click()
        self.browser.find_element(*MENU_LOGOUT).click()
        assert "saucedemo.com" in self.browser.current_url, "Wrong page"
