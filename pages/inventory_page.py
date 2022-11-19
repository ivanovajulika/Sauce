from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):
    def element_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, ".shopping_cart_container")

    def item_backpack(self):
        self.browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]').click()
        assert "id=4" in self.browser.current_url, "Wrong page"

    def should_be_item_backpack(self):
        assert self.element_is_present(By.ID, "item_4_title_link"), "Element is absent"

    def img_backpack(self):
        self.browser.find_element(By.CSS_SELECTOR, "#item_4_img_link > img").click()
        assert "id=4" in self.browser.current_url, "Wrong page"

    def should_be_filter(self):
        assert self.element_is_present(
            By.CLASS_NAME, "product_sort_container"
        ), "Element is absent"
