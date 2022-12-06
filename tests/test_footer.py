from pages.overview_page import Overview_page, Complete_page
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.item_id4 import ItemPage_4
from conf import link, list_username
from pages.checkout_page import Checkout_page
import allure
import pytest


@allure.feature("US_009.00 | Footer")
@allure.story(
    "TC_009.00.01 | Footer > Наличие футера и работа его элементов на странице 'Products'."
)
@pytest.mark.parametrize("username", list_username)
def test_footer_inventory(browser):
    page = InventoryPage(browser, link)
    page.should_be_footer()


@allure.feature("US_009.00 | Footer")
@allure.story(
    "TC_009.00.02 | Footer > Наличие футера и работа его элементов на странице товара 'Inventory item'."
)
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param("problem_user", marks=pytest.mark.xfail(reason="problem_user")),
        "performance_glitch_user",
    ],
)
def test_footer_inventory_item(browser):
    page = InventoryPage(browser, link)
    page.item_backpack()
    page = ItemPage_4(browser, link)
    page.should_be_footer()


@allure.feature("US_009.00 | Footer")
@allure.story(
    "TC_009.00.03 | Footer > Наличие футера и работа его элементов на странице товара 'Your cart'."
)
@pytest.mark.parametrize("username", list_username)
def test_footer_cart_page(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.should_be_footer()


@allure.feature("US_009.00 | Footer")
@allure.story(
    "TC_009.00.04 | Footer > Наличие футера и работа его элементов на странице товара 'Checkout: your information."
)
@pytest.mark.parametrize("username", list_username)
def test_footer_your_information(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.should_be_footer()


@allure.feature("US_009.00 | Footer")
@allure.story(
    "TC_009.00.05| Footer > Наличие футера и работа его элементов на странице товара 'Checkout: overview."
)
@pytest.mark.parametrize("username", list_username)
def test_footer_overview_page(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user()
    page = Overview_page(browser, link)
    page.should_be_footer()


@allure.feature("US_009.00 | Footer")
@allure.story(
    "TC_009.00.06| Footer > Наличие футера и работа его элементов на странице товара 'Checkout: complete!."
)
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param("problem_user", marks=pytest.mark.xfail(reason="problem_user")),
        "performance_glitch_user",
    ],
)
def test_footer_complete_page(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user()
    page = Overview_page(browser, link)
    page.go_to_finish()
    page = Complete_page(browser, link)
    page.should_be_footer()
