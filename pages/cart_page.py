from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By


# locators
BTN_CHECKOUT = (By.ID, "checkout")
BTN_CONTINUE = (By.ID, "continue-shopping")
BTN_REMOVE_CART = (By.CLASS_NAME, "cart_button")
QTY = (By.CLASS_NAME, "cart_quantity")
QTY_IN_CART = (By.CSS_SELECTOR, ".cart_item_label")
CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")


class CartPage(InventoryPage):
    def user_can_go_continue_shopping(self):
        """Метод кликает кнопку Continue, происходит возврат на страницу Products"""
        assert self.element_is_present(*BTN_CONTINUE)
        self.browser.find_element(*BTN_CONTINUE).click()
        assert "inventory" in self.browser.current_url

    def checkout_btn(self):
        """Метод кликает кнопку Checkout, происходит переход на страницу Your information"""
        self.browser.find_element(*BTN_CHECKOUT).click()

    def return_to_item_page(self):
        """Метод перехода со страницы Корзина на страницу 'Backpack' по клику на ссылку
        данного товара"""
        self.browser.find_element(By.ID, "item_4_title_link").click()

    def cart_page_counter(self, quantity):
        """Метод сверяет значение количества товара в колонке QTY с количеством quantity"""
        text = self.browser.find_element(*QTY).text
        if quantity >= 0:
            assert (
                int(text) == quantity
            ), f" Wrong quantity, quantity={quantity}, QTY={text}"
        else:
            assert (
                int(text) != quantity
            ), f" Wrong quantity, quantity={quantity}, QTY={text}"

    def change_cart_page_counter(self, quantity):
        """Метод отправляет значение quantity в колонку QTY"""
        qty = self.browser.find_element(*QTY)
        value = quantity
        qty.send_keys(value)

    def empty_cart_page(self):
        """Метод проверяет, что значение колонке QTY отсутствует"""
        assert not self.element_is_present(*QTY)

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

    def remove_cart_page(self, index=0):
        """Метод кликает кнопку Remove на странице Your cart"""
        btn_remove = self.browser.find_elements(*BTN_REMOVE_CART)[index]
        btn_remove.click()

    def quantity_all_items_in_cart(self):
        """Метод сравнивает фактическое кол-во товаров в корзине и количество на счетчике Корзина"""
        all_items = len(list(self.browser.find_elements(*QTY_IN_CART)))
        quantity_on_cart_badge = (self.browser.find_element(*CART_BADGE)).text
        assert all_items == int(quantity_on_cart_badge)
