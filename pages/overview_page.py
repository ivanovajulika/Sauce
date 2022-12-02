from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage

BTN_FINISH = (By.CSS_SELECTOR, "#finish")
BTN_BACK_HOME = (By.ID, "back-to-products")
IMG_PONY = (By.CLASS_NAME, "pony_express")
THANK_YOUR = (By.CLASS_NAME, "complete-header")
ORDER_TEXT = (By.CLASS_NAME, "complete-text")
BTN_CANCEL = (By.ID, "cancel")
PAYMENT = (By.CLASS_NAME, "summary_value_label")
DELIVERY = ()


class Overview_page(InventoryPage):
    def go_to_finish(self):
        """Метод кликает на кнопку Finish"""
        self.browser.find_element(*BTN_FINISH).click()

    def cancel_btn(self):
        """Метод кликает на кнопку Cancel и проверяет, что произошел переход на страницу Products"""
        btn_cancel = self.browser.find_element(*BTN_CANCEL)
        btn_cancel.click()
        assert "inventory" in self.browser.current_url, "Wrong page"

    def should_be_overview(self):
        """Метод проверяет наличие и содержание информации о заказе
        (наименование, количество товара, краткое описание, платежная информация, доставка, итоговая стоимость)"""
        assert self.element_is_present(*PAYMENT)
        assert (
            self.browser.find_element(*PAYMENT).text == "SauceCard #31337"
        ), "Wrong payment information"


class Complete_page(InventoryPage):
    def back_home_btn(self):
        """Метод кликает на кнопку Back home и проверяет, что произошел переход на страницу Products"""
        btn_back_home = self.browser.find_element(*BTN_BACK_HOME)
        btn_back_home.click()
        assert "inventory" in self.browser.current_url, "Wrong page"

    def btn_back_home_is_present(self):
        """Метод проверяет наличие  кнопки Back home"""
        assert self.element_is_present(*BTN_BACK_HOME)

    def thank_you_is_present(self):
        """Метод проверяет наличие надписи THANK YOU FOR YOUR ORDER"""
        assert self.element_is_present(*THANK_YOUR)
        thank_your = self.browser.find_element(*THANK_YOUR)
        assert thank_your.text == "THANK YOU FOR YOUR ORDER", "Wrong text"

    def order_dispatched(self):
        """Метод проверяет наличие надписи Your order has been dispatched,
        and will arrive just as fast as the pony can get there!"""
        assert self.element_is_present(*ORDER_TEXT)
        order_text = self.browser.find_element(*ORDER_TEXT)
        assert (
            order_text.text
            == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
        ), "Wrong text"

    def picture_is_present(self):
        """Метод проверяет наличие картинки Pony express и ее размер"""
        assert self.element_is_present(*IMG_PONY)
        img_pony = self.browser.find_element(*IMG_PONY)
        self.browser.implicitly_wait(10)
        img_pony_size = img_pony.size
        assert img_pony_size == {"height": 381, "width": 523}

    def should_be_complete(self):
        """Метод проверяет наличие кнопки Back home, картинки Pony express и ее размер,
        наличие надписей THANK YOU FOR YOUR ORDER и Your order has been dispatched"""
        self.btn_back_home_is_present()
        self.thank_you_is_present()
        self.order_dispatched()
        self.picture_is_present()
