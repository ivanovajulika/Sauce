from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):
    def element_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, ".shopping_cart_container")

    def item_backpack(self):
        self.browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]').click()
        assert "id=4" in self.browser.current_url, "Wrong page"
