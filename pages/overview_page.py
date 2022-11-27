from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage


class Overview_page(InventoryPage):
    def go_to_finish(self):
        self.browser.find_element(By.CSS_SELECTOR, "#finish").click()
