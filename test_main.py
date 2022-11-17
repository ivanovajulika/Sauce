from pages.inventory_page import InventoryPage
import time


# def test_user_can_go_cart(browser):
#     link = "https://www.saucedemo.com/inventory.html"
#     page = InventoryPage(browser, link)
#     page.open_page()
#     page.element_cart()


# def test_user_can_go_continue_shopping(browser):
#     link = "https://www.saucedemo.com/cart.html"
#     page = CartPage(browser, link)
#     page.open_page()
#     page.user_can_go_continue_shopping()


# TC_002.04.01 | Products > Ссылка на страницу товара из карточки товара "Products" - Backpack.
def test_link_to_inventory_backpack(browser):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(browser, link)
    page.open_page()
    time.sleep(5)
    page.element_is_present()
    page.item_backpack()
    time.sleep(5)


# AT_002.02.01 | Products > Цена товара на странице "Products" - Backpack
# @allure.feature("Sauce Labs")
# @allure.story("TC_002.02.01")
# @allure.severity("minor")
def test_link_to_price_backpack(browser):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(browser, link)
    page.open_page()
    time.sleep(5)
    page.item_backpack()
    time.sleep(5)
    page.price_backpack()
    time.sleep(5)
