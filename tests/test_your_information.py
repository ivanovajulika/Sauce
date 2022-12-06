import allure
import pytest
from conf import link, list_username
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import Checkout_page


@allure.feature("US_005.00 | Checkout: your information > Страница 'Ваша информация'")
@allure.story(
    "TC_005.01.01 | Checkout: your information > Работа кнопки 'CANCEL' на странице 'Checkout: your information' без ввода личных данных."
)
@pytest.mark.parametrize("username", list_username)
def test_cansel_empty_input(browser):
    page = InventoryPage(browser, link)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.btn_cancel_click()


@allure.feature("US_005.00 | Checkout: your information > Страница 'Ваша информация'")
@allure.story(
    "TC_005.02.01 | Checkout: your information > Работа кнопки 'CANCEL' на странице 'Checkout: your information' после ввода личных данных ."
)
@pytest.mark.parametrize("username", list_username)
def test_cansel_user_input(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_random()
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
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param("problem_user", marks=pytest.mark.xfail(reason="problem_user")),
        "performance_glitch_user",
    ],
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
    assert "checkout-step-two" in browser.current_url, "Wrong page"


@allure.feature("US_005.00 | Checkout: your information > Страница 'Ваша информация'")
@allure.story(
    "TC_005.02.02 | Checkout: your information > Отсутствие вводимых личных данных на странице 'Checkout: your information' и работа кнопки 'CONTINUE' (негативный тест)."
)
@pytest.mark.parametrize("username", list_username)
def test_continue_empty_input(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_random()
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.btn_continue_click()
    assert "checkout-step-two" not in browser.current_url, "Wrong page"


@allure.feature("US_005.00 | Checkout: your information > Страница 'Ваша информация'")
@allure.story(
    "TC_005.02.03 | Checkout: your information > Отсутствие вводимых данных в поле 'First name' на странице 'Checkout: your information' и работа кнопки 'CONTINUE' (негативный тест)."
)
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param("problem_user", marks=pytest.mark.xfail(reason="Test Failed")),
        "performance_glitch_user",
    ],
)
def test_continue_empty_input_fist_name(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_random()
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user_not_click(first_name="", last_name="Smith", zip_postal_code=122)
    page.btn_continue_click()
    page.error_message_first()
    assert "checkout-step-two" not in browser.current_url, "Wrong page"


@allure.feature("US_005.00 | Checkout: your information > Страница 'Ваша информация'")
@allure.story(
    "TC_005.02.04| Checkout: your information > Отсутствие вводимых данных в поле 'Last name' на странице 'Checkout: your information' и работа кнопки 'CONTINUE' (негативный тест)."
)
@pytest.mark.parametrize("username", list_username)
def test_continue_empty_input_last_name(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_random()
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user_not_click(first_name="John", last_name="", zip_postal_code=122)
    page.btn_continue_click()
    page.error_message_last()
    assert "checkout-step-two" not in browser.current_url, "Wrong page"


@allure.feature("US_005.00 | Checkout: your information > Страница 'Ваша информация'")
@allure.story(
    "TC_005.02.05| Checkout: your information > Отсутствие вводимых данных в поле 'Zip/Postal Code' на странице 'Checkout: your information' и работа кнопки 'CONTINUE' (негативный тест)."
)
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param("problem_user", marks=pytest.mark.xfail(reason="Test Failed")),
        "performance_glitch_user",
    ],
)
def test_continue_empty_zip_code(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_random()
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user_not_click(
        first_name="John", last_name="Smith", zip_postal_code=""
    )
    page.btn_continue_click()
    page.error_message_zip()
    assert "checkout-step-two" not in browser.current_url, "Wrong page"


@allure.feature("US_005.00 | Checkout: your information > Страница 'Ваша информация'")
@allure.story(
    "TC_005.02.06| Checkout: your information > Первичная проверка достоверности вводимых данных в поле 'First name' на странице  на странице 'Checkout: your information' (негативный тест)."
)
@pytest.mark.parametrize(
    "username",
    [
        pytest.param("standard_user", marks=pytest.mark.xfail(reason="standard_user")),
        "problem_user",
        pytest.param(
            "performance_glitch_user",
            marks=pytest.mark.xfail(reason="performance_glitch_user"),
        ),
    ],
)
def test_fist_name(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_random()
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user_not_click(
        first_name=123, last_name="Smith", zip_postal_code=10022
    )
    page.btn_continue_click()
    assert "checkout-step-two" not in browser.current_url, "Wrong page"


@allure.feature("US_005.00 | Checkout: your information > Страница 'Ваша информация'")
@allure.story(
    "TC_005.02.07| Checkout: your information > Первичная проверка достоверности вводимых данных в поле 'Last name' на странице  на странице 'Checkout: your information' (негативный тест)."
)
@pytest.mark.parametrize(
    "username",
    [
        pytest.param("standard_user", marks=pytest.mark.xfail(reason="standard_user")),
        "problem_user",
        pytest.param(
            "performance_glitch_user",
            marks=pytest.mark.xfail(reason="performance_glitch_user"),
        ),
    ],
)
def test_last_name(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_random()
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user_not_click(
        first_name="John", last_name=123, zip_postal_code=10022
    )
    page.btn_continue_click()
    assert "checkout-step-two" not in browser.current_url, "Wrong page"


@allure.feature("US_005.00 | Checkout: your information > Страница 'Ваша информация'")
@allure.story(
    "TC_005.02.08| Checkout: your information > Первичная проверка достоверности вводимых данных в поле 'Zip/Postal Code' на странице  на странице 'Checkout: your information' (негативный тест)."
)
@pytest.mark.parametrize(
    "username",
    [
        pytest.param("standard_user", marks=pytest.mark.xfail(reason="standard_user")),
        "problem_user",
        pytest.param(
            "performance_glitch_user",
            marks=pytest.mark.xfail(reason="performance_glitch_user"),
        ),
    ],
)
def test_zip_code(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_random()
    page.go_to_cart()
    page = CartPage(browser, link)
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user_not_click(
        first_name="John", last_name="Smith", zip_postal_code="abc"
    )
    page.btn_continue_click()
    assert "checkout-step-two" not in browser.current_url, "Wrong page"
