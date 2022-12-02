import allure
import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import Checkout_page
from pages.overview_page import Overview_page
from pages.overview_page import Complete_page
from pages.item_id4 import ItemPage_4
from pages.inventory_page import ALL_NAMES

link = "https://www.saucedemo.com/inventory.html"


@allure.feature("US_008.00 | Header")
@allure.story(
    "TC_008.01.01 | Header > Наличие хедера и его элементов на страницe 'Products'."
)
def test_should_be_elements_of_header_on_inventory_page(browser):
    page = InventoryPage(browser, link)
    page.should_be_logo()
    page.should_be_menu_sidebar()
    page.element_cart()
    page.should_be_hover()


@allure.feature("US_008.00 | Header")
@allure.story(
    "TC_008.01.02 | Header > Наличие хедера и его элементов на страницe 'Your cart'."
)
def test_should_be_elements_of_header_on_cart_page(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.should_be_logo()
    page.should_be_menu_sidebar()
    page.element_cart()
    page.should_be_hover()


@allure.feature("US_008.00 | Header")
@allure.story(
    "TC_008.01.03 | Header > Наличие хедера и его элементов на странице 'Checkout: your information'."
)
def test_should_be_elements_of_header_on_checkout_page(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.should_be_logo()
    page.should_be_menu_sidebar()
    page.element_cart()
    page.should_be_hover()


@allure.feature("US_008.00 | Header")
@allure.story(
    "TC_008.01.04 | Header > Наличие хедера и его элементов на странице 'Checkout: overview'."
)
def test_should_be_elements_of_header_on_overview_page(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user()
    page = Overview_page(browser, link)
    page.should_be_logo()
    page.should_be_menu_sidebar()
    page.element_cart()
    page.should_be_hover()


@allure.feature("US_008.00 | Header")
@allure.story(
    "TC_008.01.05 | Header > Наличие хедера и его элементов на странице 'Checkout: complete!'"
)
def test_should_be_elements_of_header_on_checkout_complete_page(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user()
    page = Overview_page(browser, link)
    page.go_to_finish()
    page = Complete_page(browser, link)
    page.should_be_logo()
    page.should_be_menu_sidebar()
    page.element_cart()
    page.should_be_hover()


@allure.feature("US_008.00 | Header")
@allure.story(
    "TC_008.01.06 | Header > Наличие хедера и его элементов на странице товара 'Inventory item."
)
def test_should_be_elements_of_header_on_inventory_item(browser):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(browser, link)
    list_all_names = page.get_all_names()
    count = len(list_all_names)
    for index in range(count):
        name = browser.find_elements(*ALL_NAMES)[index]
        name.click()
        link = browser.current_url
        page = ItemPage_4(browser, link)
        page.should_be_hover()
        page.return_to_inventory_page()


@allure.feature("US_008.00 | Header")
@allure.story(
    "TC_008.02.01 | Header > Переход по клику на логотип со страницы 'You cart' на страницу 'Products'."
)
@pytest.mark.xfail
def test_click_on_logo_from_your_cart(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.should_be_click_on_logo()


@allure.feature("US_008.00 | Header")
@allure.story(
    "TC_008.02.02 | Header > Переход по клику на логотип со страницы Checkout: your information на страницу Products"
)
@pytest.mark.xfail
def test_click_on_logo_from_checkout_page(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.should_be_click_on_logo()


@allure.feature("US_008.00 | Header")
@allure.story(
    "TC_008.02.03 | Header > Переход по клику на логотип со страницы Checkout: overview на страницу Products"
)
@pytest.mark.xfail
def test_click_on_logo_from_overview_page(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user()
    page = Overview_page(browser, link)
    page.should_be_click_on_logo()


@allure.feature("US_008.00 | Header")
@allure.story(
    "TC_008.02.04 | Header > Переход по клику на логотип со страницы Checkout: complete! на страницу Products"
)
@pytest.mark.xfail
def test_click_on_logo_from_complete_page(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user()
    page = Overview_page(browser, link)
    page.go_to_finish()
    page = Complete_page(browser, link)
    page.should_be_click_on_logo()


@allure.feature("US_008.00 | Header")
@allure.story(
    "TC_008.02.05 | Header > Переход по клику на логотип со страницы товара Inventory item на страницу Products."
)
@pytest.mark.xfail
def test_click_on_logo_from_inventory_item(browser):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(browser, link)
    list_all_names = page.get_all_names()
    count = len(list_all_names)
    for index in range(count):
        name = browser.find_elements(*ALL_NAMES)[index]
        name.click()
        link = browser.current_url
        page = ItemPage_4(browser, link)
        page.should_be_click_on_logo()
        page.return_to_inventory_page()
