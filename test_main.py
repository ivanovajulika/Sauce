from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import time
import allure
from allure_commons.types import AttachmentType


@allure.feature("Sauce Labs")
@allure.story("ТС_001_01")
@allure.severity("blocker")
def test_user_can_go_cart(browser):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(browser, link)
    page.open_page()
    page.element_cart()


@allure.feature("Sauce Labs")
@allure.story("ТС_001_02")
@allure.severity("critical")
def test_user_can_go_continue_shopping(browser):
    link = "https://www.saucedemo.com/cart.html"
    page = CartPage(browser, link)
    page.open_page()
    page.user_can_go_continue_shopping()
    with allure.step("Делаем скриншот"):
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG,
        )


# TC_002.04.01 | Products > Ссылка на страницу товара из карточки товара "Products" - Backpack.
@allure.feature("Sauce Labs")
@allure.story("TC_002.04.01")
@allure.severity("minor")
def test_link_to_inventory_backpack(browser):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(browser, link)
    page.open_page()
    time.sleep(5)
    page.element_is_present()
    page.item_backpack()
    time.sleep(5)
