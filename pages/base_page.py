from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


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

    def cart_counter(self, quantity):
        text = self.browser.find_element(By.ID, "shopping_cart_container").text
        assert text == quantity

    def go_to_cart(self):
        self.browser.find_element(By.XPATH, "//div[3]/a").click()

    def empty_cart_counter(self):
        text = self.browser.find_element(
            By.CSS_SELECTOR, "#shopping_cart_container"
        ).text
        assert text == ""
