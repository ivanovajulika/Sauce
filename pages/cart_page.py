from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    def user_can_go_continue_shopping(self):
        self.browser.find_element(By.XPATH, '//*[@id="continue-shopping"]').click()

    def checkout_btn(self):
        self.browser.find_element(By.XPATH, "//div[2]/button[2]").click()
