from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By


class ItemPage_4(InventoryPage):
    def photo_size_required(self):
        photo = self.browser.find_element(By.CSS_SELECTOR, ".inventory_details_img")
        assert photo.size == {"height": 623, "width": 496}
