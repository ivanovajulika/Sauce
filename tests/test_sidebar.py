import allure
import pytest
from conf import link, list_username
from pages.inventory_page import InventoryPage
from pages.checkout_page import Checkout_page
from pages.overview_page import Overview_page
from pages.cart_page import CartPage
from pages.item_id4 import ItemPage_4


@allure.feature("US_011.00 | Sidebar")
@allure.story("TC_011.01.01 | Sidebar > Работа Sidebar на странице 'Products'")
@pytest.mark.parametrize("username", list_username)
def test_should_be_menu_sidebar(browser):
    page = InventoryPage(browser, link)
    page.should_be_menu_sidebar()


@allure.feature("US_011.00 | Sidebar")
@allure.story("TC_011.01.02 | Sidebar > Работа Sidebar на странице 'Your cart'")
@pytest.mark.parametrize("username", list_username)
def test_should_be_menu_sidebar_cart(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_backpack()
    page.go_to_cart()
    page = CartPage(browser, link)
    page.should_be_menu_sidebar()


@allure.feature("US_011.00 | Sidebar")
@allure.story("TC_011.01.03 | Sidebar > Работа Sidebar на странице 'Inventory item'")
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param("problem_user", marks=pytest.mark.xfail(reason="problem_user")),
        "performance_glitch_user",
    ],
)
def test_should_be_menu_sidebar_item(browser):
    page = InventoryPage(browser, link)
    page.item_backpack()
    page = ItemPage_4(browser, link)
    page.should_be_menu_sidebar()


@allure.feature("US_011.00 | Sidebar")
@allure.story(
    "TC_011.01.04 | Sidebar > Работа Sidebar на странице 'Checkout: your information'"
)
@pytest.mark.parametrize("username", list_username)
def test_should_be_menu_sidebar_checkout(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_backpack()
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.should_be_menu_sidebar()


@allure.feature("US_011.00 | Sidebar")
@allure.story(
    "TC_011.01.05 | Sidebar > Работа Sidebar на странице 'Checkout: overview'"
)
@pytest.mark.parametrize("username", list_username)
def test_should_be_menu_sidebar_overview(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_backpack()
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user()
    page = Checkout_page(browser, link)
    page.should_be_menu_sidebar()


@allure.feature("US_011.00 | Sidebar")
@allure.story(
    "TC_011.01.06 | Sidebar > Работа Sidebar на странице 'Checkout: complete!'"
)
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param("problem_user", marks=pytest.mark.xfail(reason="problem_user")),
        "performance_glitch_user",
    ],
)
def test_should_be_menu_sidebar_complete(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_backpack()
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user()
    page = Overview_page(browser, link)
    page.go_to_finish()
    page.should_be_menu_sidebar()


@allure.feature("US_011.00 | Sidebar")
@allure.story(
    "TC_011.02.01 | Sidebar > Переход по меню Sidebar со страницы 'Your cart' на страницу 'Products'"
)
@pytest.mark.parametrize("username", list_username)
def test_navigating_sidebar(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.return_to_inventory_page()


@allure.feature("US_011.00 | Sidebar")
@allure.story(
    "TC_011.02.02 | Sidebar > Переход со страницы 'Products' на страницу 'https://saucelabs.com/' по пункту меню 'About'"
)
@pytest.mark.parametrize("username", list_username)
def test_navigating_sidebar_about(browser):
    page = InventoryPage(browser, link)
    page.go_to_about()


@allure.feature("US_011.00 | Sidebar")
@allure.story(
    "TC_011.02.03 | Sidebar > Обнуление корзины на странице 'Products' по клику на пункт меню 'Reset app state'"
)
@pytest.mark.parametrize("username", list_username)
def test_sidebar_reset_cart_inventory(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_backpack()
    page.cart_counter(quantity=1)
    page.go_to_cart()
    browser.implicitly_wait(5)
    page = CartPage(browser, link)
    page.cart_page_counter(quantity=1)
    page.user_can_go_continue_shopping()
    browser.implicitly_wait(5)
    page = InventoryPage(browser, link)
    page.reset_cart()
    page.empty_cart_counter()
    page.go_to_cart()
    browser.implicitly_wait(5)
    page = CartPage(browser, link)
    page.empty_cart_page()


@allure.feature("US_011.00 | Sidebar")
@allure.story(
    "TC_011.02.04 | Sidebar > Обнуление корзины на странице 'Your cart' по клику на пункт меню 'Reset app state'"
)
@pytest.mark.parametrize("username", list_username)
def test_sidebar_reset_cart_yourcart(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_backpack()
    page.cart_counter(quantity=1)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.cart_page_counter(quantity=1)
    page.reset_cart()
    page.empty_cart_counter()
    page.browser.refresh()
    page.empty_cart_page()


@allure.feature("US_011.00 | Sidebar")
@allure.story(
    "TC_011.02.05 | Sidebar > Выход из аккаунта со страницы 'Products' по клику на пункт меню 'Logout'"
)
@pytest.mark.parametrize("username", list_username)
def test_sidebar_logout(browser):
    page = InventoryPage(browser, link)
    page.go_to_logout()
