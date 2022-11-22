from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

BTN_ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
BTN_REMOVE = (By.ID, "remove-sauce-labs-backpack")


class ItemPage_4(InventoryPage):
    def photo_size_required(self):
        photo = self.browser.find_element(By.CSS_SELECTOR, ".inventory_details_img")
        print(photo.size)
        # assert photo.size == {"height": 623, "width": 496}

    # нажать кнопку ADD to cart на странице 'Backpack'
    def add_to_cart(self):
        self.browser.find_element(*BTN_ADD_TO_CART).click()

    #  кнопка  REMOVE присутствует на странице 'Backpack'
    def remove_from_cart_btn(self):
        assert self.element_is_present(*BTN_REMOVE)

    def go_to_cart(self):
        self.browser.find_element(By.XPATH, "//div[3]/a").click()

    def remove_from_cart(self):
        self.browser.find_element(*BTN_REMOVE).click()

    # кнопка ADD to cart присутствует на странице 'Backpack'
    def add_to_cart_btn_is_present(self):
        assert self.element_is_present(*BTN_ADD_TO_CART)

    def empty_cart_counter(self):
        text = self.browser.find_element(
            By.CSS_SELECTOR, "#shopping_cart_container"
        ).text
        assert text == ""
