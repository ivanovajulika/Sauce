import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


# TestData
link = "https://www.saucedemo.com/"
# standard_user = "standard_user"
# password = "secret_sauce"


@pytest.fixture
def username():
    return "standard_user"


@pytest.fixture
def password():
    return "secret_sauce"


@pytest.fixture(scope="function")
def browser(username, password):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1080")
    options.headless = True
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    browser.get(link)
    browser.implicitly_wait(10)

    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()
    browser.implicitly_wait(10)
    assert "inventory" in browser.current_url, "Wrong page"

    yield browser
    browser.quit()
