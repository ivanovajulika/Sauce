from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage

# locators
BTN_CANCEL = (By.ID, "cancel")
BTN_CONTINUE = (By.ID, "continue")


class Checkout_page(InventoryPage):
    def checkout_user(self, first_name="John", last_name="Smith", zip_postal_code=122):
        first_name_input = self.browser.find_element(By.CSS_SELECTOR, "#first-name")
        first_name_input.send_keys(first_name)
        last_name_input = self.browser.find_element(By.CSS_SELECTOR, "#last-name")
        last_name_input.send_keys(last_name)
        zip_postal_code_input = self.browser.find_element(
            By.CSS_SELECTOR, "#postal-code"
        )
        zip_postal_code_input.send_keys(zip_postal_code)
        self.browser.find_element(By.CSS_SELECTOR, "#continue").click()

    def finish_btn(
        self,
    ):  # Негативный тест-кейс - не должно быть перехода на checkout-complete!
        self.browser.find_element(By.CSS_SELECTOR, "#finish").click()
        assert "checkout-complete" not in self.browser.current_url, "Wrong page"

    def btn_cancel_click(self):
        btn_cancel = self.browser.find_element(*BTN_CANCEL)
        btn_cancel.click()
        assert "cart" in self.browser.current_url, "Wrong page"

    def checkout_user_not_click(
        self, first_name="John", last_name="Smith", zip_postal_code=122
    ):
        first_name_input = self.browser.find_element(By.CSS_SELECTOR, "#first-name")
        first_name_input.send_keys(first_name)
        last_name_input = self.browser.find_element(By.CSS_SELECTOR, "#last-name")
        last_name_input.send_keys(last_name)
        zip_postal_code_input = self.browser.find_element(
            By.CSS_SELECTOR, "#postal-code"
        )
        zip_postal_code_input.send_keys(zip_postal_code)

    def btn_continue_click(self):
        btn_continue = self.browser.find_element(*BTN_CONTINUE)
        btn_continue.click()
        assert "checkout-step-two" in self.browser.current_url, "Wrong page"
