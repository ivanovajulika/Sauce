from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

BTN_ADD_TO_CART = (By.CLASS_NAME, "btn_primary")
BTN_REMOVE = (By.ID, "remove-sauce-labs-backpack")
BTN_BACK = (By.ID, "back-to-products")
DETAILS_IMG = (By.CSS_SELECTOR, ".inventory_details_img")


class ItemPage_4(InventoryPage):
    def photo_size_required(self):
        """Метод проверяет наличие фотографии на странице 'Backpack'"""
        photo = self.browser.find_element(*DETAILS_IMG)

    def add_to_cart(self):
        """Метод добавляет товар в корзину на странице 'Backpack'"""
        self.browser.find_element(*BTN_ADD_TO_CART).click()

    def remove_from_cart_btn(self):
        """Метод проверяет наличие кнопки REMOVE на странице 'Backpack'"""
        assert self.element_is_present(*BTN_REMOVE)

    def remove_from_cart(self):
        """Метод удаляет товар из корзины на странице 'Backpack'"""
        self.browser.find_element(*BTN_REMOVE).click()

    def add_to_cart_btn_is_present(self):
        """Метод проверяет наличие кнопки ADD to cart на странице 'Backpack'"""
        assert self.element_is_present(*BTN_ADD_TO_CART)

    def back_to_products_btn_is_present(self):
        """Метод проверяет наличие кнопки Back to products на странице 'Backpack'"""
        assert self.element_is_present(*BTN_BACK)

    def back_to_products(self):
        """Метод проверяет переход по кнопке Back to products на страницу Inventory"""
        self.browser.find_element(*BTN_BACK).click()
        assert "inventory" in self.browser.current_url, "Wrong page"
