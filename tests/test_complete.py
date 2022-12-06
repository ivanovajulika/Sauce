import allure
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import Checkout_page
from pages.overview_page import Overview_page, Complete_page

link = "https://www.saucedemo.com/inventory.html"


@allure.feature(
    "US_007.00 | Checkout: complete! > Страница завершения оформления заказа."
)
@allure.story(
    "TC_007.00.01 | Checkout: complete! > Визуальная проверка корректного "
    "отображения графического интерфейса завершения заказа на странице."
)
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param("problem_user", marks=pytest.mark.xfail(reason="problem_user")),
        pytest.param(
            "performance_glitch_user",
            marks=pytest.mark.xfail(reason="performance_glitch_user"),
        ),
    ],
)
def test_should_be_complete(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user()
    page = Overview_page(browser, link)
    page.go_to_finish()
    page = Complete_page(browser, link)
    page.should_be_complete()


@allure.feature(
    "US_007.00 | Checkout: complete! > Страница завершения оформления заказа."
)
@allure.story(
    "TC_007.00.02 | Checkout: complete! > Проверка корректной работы кнопки 'BACK HOME'"
)
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param("problem_user", marks=pytest.mark.xfail(reason="problem_user")),
        pytest.param(
            "performance_glitch_user",
            marks=pytest.mark.xfail(reason="performance_glitch_user"),
        ),
    ],
)
def test_back_home(browser):
    test_should_be_complete(browser)
    page = Complete_page(browser, link)
    page.back_home_btn()
