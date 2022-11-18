from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By


class ItemPage_4(InventoryPage):
    def photo_size_required(self):
        photo = self.browser.find_element(By.CSS_SELECTOR, ".inventory_details_img")
        assert photo.size == {"height": 623, "width": 496}

    def add_to_cart(self):
        self.browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def remove_from_cart_btn(self):
        assert self.element_is_present(By.ID, "remove-sauce-labs-backpack")

    def cart_counter(self):
        text = self.browser.find_element(By.ID, "shopping_cart_container").text
        assert text == "1"

    def go_to_cart(self):
        self.browser.find_element(By.XPATH, "//div[3]/a").click()

    def cart_page_counter(self):
        text = self.browser.find_element(By.CLASS_NAME, "cart_quantity").text
        assert text == "1"

    def return_to_item_page(self):
        self.browser.find_element(By.ID, "item_4_title_link").click()

    def remove_from_cart(self):
        self.browser.find_element(By.ID, "remove-sauce-labs-backpack").click()

    def add_to_cart_btn(self):
        assert self.element_is_present(By.ID, "add-to-cart-sauce-labs-backpack")

    def empty_cart_counter(self):
        text = self.browser.find_element(
            By.CSS_SELECTOR, "#shopping_cart_container"
        ).text
        assert text == ""

    def empty_cart(self):
        assert not self.element_is_present(By.CLASS_NAME, "cart_quantity")
