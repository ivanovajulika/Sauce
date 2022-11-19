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

    def count_products(self):
        elements = len(self.browser.find_elements(By.CSS_SELECTOR, ".inventory_item"))
        assert elements == 6

    def price_backpack(self):
        price = self.browser.find_element(
            By.XPATH, "(//*[@class='inventory_item_price'])[1]"
        ).text
        assert price == "$29.99", "Wrong price"

    def should_be_filter(self):
        assert self.element_is_present(
            By.CLASS_NAME, "product_sort_container"
        ), "Element is absent"

    def should_be_img_backpack(self):
        element = self.browser.find_element(By.CSS_SELECTOR, "#item_4_img_link > img")
        img = element.get_attribute("src")
        assert (
            img
            == "https://www.saucedemo.com/static/media/sauce-backpack-1200x1500.34e7aa42.jpg"
        )

    def should_be_img_bike_light(self):
        element = self.browser.find_element(By.CSS_SELECTOR, "#item_0_img_link > img")
        img = element.get_attribute("src")
        assert (
            img
            == "https://www.saucedemo.com/static/media/bike-light-1200x1500.a0c9caae.jpg"
        )

    def should_be_img_bolt_t_shirt(self):
        element = self.browser.find_element(By.CSS_SELECTOR, "#item_1_img_link > img")
        img = element.get_attribute("src")
        assert (
            img
            == "https://www.saucedemo.com/static/media/bolt-shirt-1200x1500.c0dae290.jpg"
        )

    def should_be_img_fleece_jacket(self):
        element = self.browser.find_element(By.CSS_SELECTOR, "#item_5_img_link > img")
        img = element.get_attribute("src")
        assert (
            img
            == "https://www.saucedemo.com/static/media/sauce-pullover-1200x1500.439fc934.jpg"
        )

    def should_be_img_onesie(self):
        element = self.browser.find_element(By.CSS_SELECTOR, "#item_2_img_link > img")
        img = element.get_attribute("src")
        assert (
            img
            == "https://www.saucedemo.com/static/media/red-onesie-1200x1500.1b15e1fa.jpg"
        )

    def should_be_img_t_shirt(self):
        element = self.browser.find_element(By.CSS_SELECTOR, "#item_3_img_link > img")
        img = element.get_attribute("src")
        assert (
            img
            == "https://www.saucedemo.com/static/media/red-tatt-1200x1500.e32b4ef9.jpg"
        )
