from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class InventoryPage(BasePage):
    def element_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, ".shopping_cart_container")

    def item_backpack(self):
        self.browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]').click()
        assert "id=4" in self.browser.current_url, "Wrong page"

    def element_is_present(self):
        try:
            self.browser.find_element(By.ID, "item_4_title_link")
        except NoSuchElementException:
            assert False
        assert True

    def price_backpack(self):
        self.browser.find_element(By.ID, "item_4_title_link")
        self.browser.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(1) > div.inventory_item_description > div.pricebar > div")
        text = self.browser.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(1) > div.inventory_item_description > div.pricebar > div").text
        assert text == "29.99", "Wrong price"