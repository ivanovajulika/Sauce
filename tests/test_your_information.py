import allure
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import Checkout_page

link = "https://www.saucedemo.com/inventory.html"


@allure.feature("US_005.00 | Checkout: your information > Страница 'Ваша информация'")
@allure.story(
    "TC_005.01.01 | Checkout: your information > Работа кнопки 'CANCEL' на странице 'Checkout: your information' без ввода личных данных."
)
def test_cansel_empty_input(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.btn_cancel_click()


@allure.feature("US_005.00 | Checkout: your information > Страница 'Ваша информация'")
@allure.story(
    "TC_005.01.02 | Checkout: your information > Работа кнопки 'CANCEL' на странице 'Checkout: your information' после ввода личных ."
)
def test_cansel_user_input(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user_not_click()
    page.btn_cancel_click()


@allure.feature("US_005.00 | Checkout: your information > Страница 'Ваша информация'")
@allure.story(
    "TC_005.02.01 | Checkout: your information > Ввод валидных данных на странице'Checkout: your information' и работа кнопки 'CONTINUE'"
)
def test_continue_user_input(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_random()
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user_not_click()
    page.btn_continue_click()


@allure.feature("US_005.00 | Checkout: your information > Страница 'Ваша информация'")
@allure.story(
    "TC_005.02.02 | Checkout: your information > Отсутствие вводимых личных данных на странице 'Checkout: your information' и работа кнопки 'CONTINUE' (негативный тест)."
)
@pytest.mark.xfail
def test_continue_epmty_input(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_random()
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.btn_continue_click()
    assert "checkout-step-two" not in browser.current_url, "Wrong page"
