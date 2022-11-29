import allure
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.item_id4 import ItemPage_4
from pages.checkout_page import Checkout_page
from pages.overview_page import Overview_page, Complete_page

link = "https://www.saucedemo.com/inventory.html"


@allure.feature("US_009.00 | Footer")
@allure.story(
    "TC_009.00.01 | Footer > Наличие футера и работа его элементов на странице 'Products'."
)
def test_footer_inventory(browser):
    page = InventoryPage(browser, link)
    page.should_be_footer()


@allure.feature("US_009.00 | Footer")
@allure.story(
    "TC_009.00.02 | Footer > Наличие футера и работа его элементов на странице товара 'Inventory item'."
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
def test_footer_cart_page(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.should_be_footer()


@allure.feature("US_009.00 | Footer")
@allure.story(
    "TC_009.00.04 | Footer > Наличие футера и работа его элементов на странице товара 'Checkout: your information."
)
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


@allure.feature("US_010.00 | Filter")
@allure.story("TC_010.00.01 | Filter > Проверка наличия фильтра на странице 'Products'")
def test_filter_is_present(browser):
    assert "inventory" in browser.current_url, "Wrong page"
    page = InventoryPage(browser, link)
    page.should_be_filter()


@allure.feature("US_010.00 | Filter")
@allure.story("TC_010.00.02 | Filter > Работа фильтра на странице 'Products' (Z-A).")
def test_sorted_z_to_a(browser):
    assert "inventory" in browser.current_url, "Wrong page"
    page = InventoryPage(browser, link)
    # нажать на символ фильтр
    page.click_filter()
    # выбрать в дропдаун меню Z-A
    page.choice_z_a()
    # создать список из всех наименований товаров
    list_all_names = page.get_all_names()
    # проверить, что все наименования отсортированы.
    assert sorted(list_all_names, reverse=True) == list_all_names


@allure.feature("US_010.00 | Filter")
@allure.story("TC_010.00.03 | Filter > Работа фильтра на странице 'Products' (A-Z).")
def test_sorted_a_to_z(browser):
    assert "inventory" in browser.current_url, "Wrong page"
    page = InventoryPage(browser, link)
    # нажать на символ фильтр
    page.click_filter()
    # выбрать в дропдаун меню Z-A
    page.choice_a_z()
    # создать список из всех наименований товаров
    list_all_names = page.get_all_names()
    # проверить, что все наименования отсортированы.
    assert sorted(list_all_names, reverse=False) == list_all_names


@allure.feature("US_010.00 | Filter")
@allure.story(
    "TC_010.00.04 | Filter > Работа фильтра Price на странице 'Products' (low to high)"
)
def test_sorted_low_to_hi(browser):
    assert "inventory" in browser.current_url, "Wrong page"
    page = InventoryPage(browser, link)
    # нажать на символ фильтр
    page.click_filter()
    # выбрать в дропдаун меню Price (low to high)
    page.choice_price_lo_to_hi()
    # создать список из всех цен товаров
    list_all_prices = page.get_all_prices()
    # проверить, что все наименования отсортированы.
    assert sorted(list_all_prices, reverse=False) == list_all_prices


@allure.feature("US_010.00 | Filter")
@allure.story(
    "TC_010.00.05 | Filter > Работа фильтра Price на странице 'Products' (high to low)"
)
def test_sorted_hi_to_low(browser):
    assert "inventory" in browser.current_url, "Wrong page"
    page = InventoryPage(browser, link)
    # нажать на символ фильтр
    page.click_filter()
    # выбрать в дропдаун меню Price (high to low)
    page.choice_price_hi_to_lo()
    # создать список из всех цен товаров
    list_all_prices = page.get_all_prices()
    # проверить, что все наименования отсортированы.
    assert sorted(list_all_prices, reverse=True) == list_all_prices
