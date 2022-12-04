from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By


# locators
BTN_CHECKOUT = (By.ID, "checkout")
BTN_CONTINUE = (By.ID, "continue-shopping")


class CartPage(InventoryPage):
    def user_can_go_continue_shopping(self):
        self.browser.find_element(*BTN_CONTINUE).click()

    def checkout_btn(self):
        self.browser.find_element(*BTN_CHECKOUT).click()

    # возврат со страницы Корзина на страницу 'Backpack'
    # по клику на ссылку на странице
    def return_to_item_page(self):
        self.browser.find_element(By.ID, "item_4_title_link").click()

    def cart_page_counter(self, quantity):
        """Метод сверяет количество товара из колонки QTY quantity"""
        text = self.browser.find_element(By.CLASS_NAME, "cart_quantity").text
        assert int(text) == quantity

    def empty_cart_page(self):
        assert not self.element_is_present(By.CLASS_NAME, "cart_quantity")

    def list_item_id5(self):
        title_item = self.browser.find_element(
            By.CSS_SELECTOR, "#item_5_title_link > div"
        ).text
        desc_item = self.browser.find_element(
            By.XPATH, '(//*[@class="inventory_item_desc"])'
        ).text
        pr_item = self.browser.find_element(
            By.XPATH, '(//*[@class="inventory_item_price"])'
        ).text
        dict_id5_item = {"name": title_item, "description": desc_item, "price": pr_item}
        return dict_id5_item

    def count_products_in_the_cart(self):
        """Метод проверяет, что в корзину добавлено все 6 товаров"""
        elements = len(self.browser.find_elements(By.CSS_SELECTOR, ".cart_item"))
        assert elements == 6
