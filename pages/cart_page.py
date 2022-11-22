from pages.base_page import BasePage
from selenium.webdriver.common.by import By


# locators
BTN_CHECKOUT = (By.ID, "checkout")


class CartPage(BasePage):
    def user_can_go_continue_shopping(self):
        self.browser.find_element(By.XPATH, '//*[@id="continue-shopping"]').click()

    def checkout_btn(self):
        self.browser.find_element(*BTN_CHECKOUT).click()

    # возврат со страницы Корзина на страницу 'Backpack'
    def return_to_item_page(self):
        self.browser.find_element(By.ID, "item_4_title_link").click()

    # количество товара на странице Your Cart
    def cart_page_counter(self):
        text = self.browser.find_element(By.CLASS_NAME, "cart_quantity").text
        assert text == "1"

    def empty_cart_page(self):
        assert not self.element_is_present(By.CLASS_NAME, "cart_quantity")
