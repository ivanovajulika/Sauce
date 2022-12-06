import allure
import pytest
from conf import *
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import Checkout_page
from pages.overview_page import Overview_page


@allure.feature(
    "US_006.00 | Checkout: overview > Страница проверки и подтверждения заказа.."
)
@allure.story(
    "TC_006.00.01 |  Checkout: overview > Отображение информации о заказе на странице 'Checkout: overview'"
)
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param("problem_user", marks=pytest.mark.xfail(reason="problem_user")),
        "performance_glitch_user",
    ],
)
def test_overview(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_random()
    page.go_to_cart()
    page = CartPage(browser, link)
    list_all_cart = page.all_items()
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user()
    page = Overview_page(browser, link)
    list_all_overview = page.all_items()
    assert list_all_cart == list_all_overview
    page.cart_counter(quantity=1)
    page.should_be_overview()


@allure.feature(
    "US_006.00 | Checkout: overview > Страница проверки и подтверждения заказа.."
)
@allure.story(
    "TC_006.00.02 |  Checkout: overview > Отображение информации "
    "о итоговой стоимости заказа на странице 'Checkout: overview'"
)
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param("problem_user", marks=pytest.mark.xfail(reason="problem_user")),
        "performance_glitch_user",
    ],
)
def test_total_sum(browser):
    test_overview(browser)
    page = Overview_page(browser, link)
    page.total()


@allure.feature(
    "US_006.00 | Checkout: overview > Страница проверки и подтверждения заказа.."
)
@allure.story(
    "TC_006.00.03 |  Checkout: overview > Бесплатная доставка  заказа на странице 'Checkout: overview'"
)
@pytest.mark.parametrize("username", list_username)
@pytest.mark.xfail
def test_free_delivery(browser):
    test_overview(browser)
    page = Overview_page(browser, link)
    page.free_delivery()


@allure.feature(
    "US_006.00 | Checkout: overview > Страница проверки и подтверждения заказа.."
)
@allure.story(
    "TC_006.01.01 |  Checkout: overview > Работа кнопки 'CANCEL' на странице 'Checkout: overview' "
    "при добавлении товара в корзину."
)
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param("problem_user", marks=pytest.mark.xfail(reason="problem_user")),
        "performance_glitch_user",
    ],
)
def test_cancel_overview(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_random()
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user()
    page = Overview_page(browser, link)
    page.cancel_btn()


@allure.feature(
    "US_006.00 | Checkout: overview > Страница проверки и подтверждения заказа.."
)
@allure.story(
    "TC_006.01.02 |  Checkout: overview > Работа кнопки 'CANCEL' на странице 'Checkout: overview' "
    "при отсутствии товаров в корзине."
)
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param("problem_user", marks=pytest.mark.xfail(reason="problem_user")),
        "performance_glitch_user",
    ],
)
def test_cancel_overview_empty_cart(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user()
    page = Overview_page(browser, link)
    page.cancel_btn()


@allure.feature(
    "US_006.00 | Checkout: overview > Страница проверки и подтверждения заказа.."
)
@allure.story(
    "TC_006.02.01 |  Checkout: overview > Работа кнопки 'FINISH' на странице 'Checkout: overview' "
    "при добавлении товара в корзину."
)
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param("problem_user", marks=pytest.mark.xfail(reason="problem_user")),
        "performance_glitch_user",
    ],
)
def test_finish_overview(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_random()
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user()
    page = Overview_page(browser, link)
    page.go_to_finish()
    assert "checkout-complete" in browser.current_url, "Wrong page"


@allure.feature(
    "US_006.00 | Checkout: overview > Страница проверки и подтверждения заказа.."
)
@allure.story(
    "TC_006.02.02 |  Checkout: overview > Работа кнопки 'FINISH' на странице 'Checkout: overview' "
    "при отсутствии товаров в корзине."
)
@pytest.mark.parametrize("username", list_username)
@pytest.mark.xfail
def test_finish_overview_empty_cart(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user()
    page = Overview_page(browser, link)
    page.go_to_finish()
    assert "checkout-complete" not in browser.current_url, "Wrong page"
