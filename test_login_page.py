import pytest
from selenium.webdriver.common.by import By
import allure

# TestData
list_username = [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
]


@allure.feature("US_001.00 | Login page > Страница авторизации.")
@allure.story("TC_001.00.01 Login page > Авторизация под валидными данными")
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param(
            "locked_out_user", marks=pytest.mark.xfail(reason="User was not registred")
        ),
        "problem_user",
        "performance_glitch_user",
    ],
)
def test_user_can_auth(browser, username):
    assert "inventory" in browser.current_url, "Wrong page"


@allure.feature("US_001.00 | Login page > Страница авторизации.")
@allure.story("TC_001.00.02 | Login page > Авторизация при пустом поле 'Password'")
@pytest.mark.parametrize("password", [""])
@pytest.mark.parametrize("username", list_username)
def test_password_is_empty(browser, password, username):
    assert "inventory" not in browser.current_url, "Wrong page"
    error_message = browser.find_element(By.CLASS_NAME, "error-message-container")
    assert (
        error_message.text == "Epic sadface: Password is required"
    ), "Wrong error message"


@allure.feature("US_001.00 | Login page > Страница авторизации.")
@allure.story("TC_001.00.03 | Login page > Авторизация при пустом поле 'Username'")
@pytest.mark.parametrize("username", [""])
def test_username_is_empty(browser, username):
    assert "inventory" not in browser.current_url, "Wrong page"
    error_message = browser.find_element(By.CLASS_NAME, "error-message-container")
    assert (
        error_message.text == "Epic sadface: Username is required"
    ), "Wrong error message"


@allure.feature("US_001.00 | Login page > Страница авторизации.")
@allure.story(
    "TC_001.00.04 | Login page > Авторизация при вводе в поле 'Password' валидного логина"
)
@pytest.mark.parametrize("password", list_username)
@pytest.mark.parametrize("username", list_username)
def test_password_is_login(browser, password, username):
    error_message = browser.find_element(By.CLASS_NAME, "error-message-container")
    assert (
        error_message.text
        == "Epic sadface: Username and password do not match any user in this service"
    ), " Wrong error message"


@allure.feature("US_001.00 | Login page > Страница авторизации.")
@allure.story(
    "TC_001.00.07 | Login Page > Авторизация при вводе пробелов в поле Username'"
)
@pytest.mark.parametrize("username", ["   "])
def test_username_is_whitespace(browser, username):
    assert "inventory" not in browser.current_url, "Wrong page"
    error_message = browser.find_element(By.CLASS_NAME, "error-message-container")
    assert (
        error_message.text
        == "Epic sadface: Username and password do not match any user in this service"
    ), "Wrong error message"


@allure.feature("US_001.00 | Login page > Страница авторизации.")
@allure.story(
    "TC_001.00.08 | Login page > Авторизация при вводе пробелов в поле 'Password'"
)
@pytest.mark.parametrize("password", ["   "])
@pytest.mark.parametrize("username", list_username)
def test_password_is_whitespace(browser, password, username):
    assert "inventory" not in browser.current_url, "Wrong page"
    error_message = browser.find_element(By.CLASS_NAME, "error-message-container")
    assert (
        error_message.text
        == "Epic sadface: Username and password do not match any user in this service"
    ), "Wrong error message"


@allure.feature("US_001.00 | Login page > Страница авторизации.")
@allure.story("TC_001.00.10 | Login page > Авторизация заблокированного пользователя")
@pytest.mark.parametrize("username", ["locked_out_user"])
def test_locked_out_user(browser, username):
    assert "inventory" not in browser.current_url, "Wrong page"
    error_message = browser.find_element(By.CLASS_NAME, "error-message-container")
    assert (
        error_message.text == "Epic sadface: Sorry, this user has been locked out."
    ), "Wrong error message"


@allure.feature("US_001.00 | Login page > Страница авторизации.")
@allure.story(
    "AT_001.00.12 | Login page > Авторизация при вводе в поле 'Username' с латинскими и русскими буквами"
)
@pytest.mark.parametrize("password", list_username)
@pytest.mark.parametrize("username", ["stаndаrt_usеr"])
def test_username_with_rusletters(browser, username):
    assert "inventory" not in browser.current_url, "Wrong page"
    error_message = browser.find_element(By.CLASS_NAME, "error-message-container")
    assert (
        error_message.text
        == "Epic sadface: Username and password do not match any user in this service"
    ), "Wrong error message"
