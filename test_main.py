from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# TestData
link = "https://www.saucedemo.com/"
standard_user = "standard_user"
locked_out_user = "locked_out_user"
problem_user = "problem_user"
performance_glitch_user = "performance_glitch_user"
password = "secret_sauce"


# TC_001.00.01 Login page > Авторизация под валидными данными
def test_user_can_auth():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1080")
    options.headless = True
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    browser.get(link)
    browser.implicitly_wait(10)

    username_input = browser.find_element(By.XPATH, '//*[@id="user-name"]')
    username_input.send_keys(standard_user)
    password_input = browser.find_element(By.XPATH, '//*[@id="password"]')
    password_input.send_keys(password)
    btn_login = browser.find_element(By.XPATH, '//*[@id="login-button"]')
    btn_login.click()
    browser.implicitly_wait(10)
    assert "inventory" in browser.current_url, "Wrong page"
    browser.quit()


# TC_001.00.02 | Login page > Авторизация при пустом поле "Password"
def test_password_is_empty():
    password_empty = ""
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1080")
    options.headless = True
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    browser.get(link)
    browser.implicitly_wait(10)

    username_input = browser.find_element(By.XPATH, '//*[@id="user-name"]')
    username_input.send_keys(standard_user)
    password_input = browser.find_element(By.XPATH, '//*[@id="password"]')
    password_input.send_keys(password_empty)
    btn_login = browser.find_element(By.XPATH, '//*[@id="login-button"]')
    btn_login.click()
    browser.implicitly_wait(10)
    assert "inventory" not in browser.current_url, "Wrong page"
    error_message = browser.find_element(By.CLASS_NAME, "error-message-container")
    assert (
        error_message.text == "Epic sadface: Password is required"
    ), "Wrong error message"
    browser.quit()


# TC_001.00.10 | Login page > Авторизация заблокированного пользователя
def test_locked_out_user():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1080")
    options.headless = True
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    browser.get(link)
    browser.implicitly_wait(10)

    username_input = browser.find_element(By.XPATH, '//*[@id="user-name"]')
    username_input.send_keys(locked_out_user)
    password_input = browser.find_element(By.XPATH, '//*[@id="password"]')
    password_input.send_keys(password)
    btn_login = browser.find_element(By.XPATH, '//*[@id="login-button"]')
    btn_login.click()
    browser.implicitly_wait(10)
    assert "inventory" not in browser.current_url, "Wrong page"
    error = browser.find_element(
        By.XPATH, '//*[@id="login_button_container"]//div[3]/h3'
    )
    assert error.text == "Epic sadface: Sorry, this user has been locked out."
    browser.quit()


# AT_010.00.01 | Filter > Проверка наличия фильтра на странице "Products"
def test_filter_is_present():
    # browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1080")
    options.headless = True
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    browser.get(link)
    browser.implicitly_wait(10)

    username_input = browser.find_element(By.XPATH, '//*[@id="user-name"]')
    username_input.send_keys(standard_user)
    password_input = browser.find_element(By.XPATH, '//*[@id="password"]')
    password_input.send_keys(password)
    btn_login = browser.find_element(By.XPATH, '//*[@id="login-button"]')
    btn_login.click()
    browser.implicitly_wait(10)
    assert (
        "inventory" in browser.current_url
    ), "Wrong page"  # проверяем, что на нужной странице
    try:
        browser.find_element(By.CLASS_NAME, "product_sort_container")
    except NoSuchElementException:
        assert False
    assert True
    browser.quit()

    # TC_001.00.03 | Login page > Авторизация при пустом поле "Username"
    def test_username_is_empty():
        username_empty = ""
        # browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1600,1080")
        options.headless = True
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options
        )

        browser.get(link)
        browser.implicitly_wait(10)

        username_input = browser.find_element(By.XPATH, '//*[@id="user-name"]')
        username_input.send_keys(username_empty)
        password_input = browser.find_element(By.XPATH, '//*[@id="password"]')
        password_input.send_keys(password)
        btn_login = browser.find_element(By.XPATH, '//*[@id="login-button"]')
        btn_login.click()
        browser.implicitly_wait(10)
        assert "inventory" not in browser.current_url, "Wrong page"
        error_message = browser.find_element(By.CLASS_NAME, "error-message-container")
        assert (
            error_message.text == "Epic sadface: Username is required"
        ), "Wrong error message"
        browser.quit()


# TC_001.00.08 | Login page > Авторизация при вводе пробелов в поле "Password"
def test_password_is_whitespace():
    password_whitespace = "   "
    # browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1080")
    options.headless = True
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    browser.get(link)
    browser.implicitly_wait(10)

    username_input = browser.find_element(By.XPATH, '//*[@id="user-name"]')
    username_input.send_keys(standard_user)
    password_input = browser.find_element(By.XPATH, '//*[@id="password"]')
    password_input.send_keys(password_whitespace)
    btn_login = browser.find_element(By.XPATH, '//*[@id="login-button"]')
    btn_login.click()
    browser.implicitly_wait(10)
    assert "inventory" not in browser.current_url, "Wrong page"
    error_message = browser.find_element(By.CLASS_NAME, "error-message-container")
    assert (
        error_message.text == "Epic sadface: Username and password do not match any user in this service"
    ), "Wrong error message"
    browser.quit()
