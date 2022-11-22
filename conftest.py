import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType
import os

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
    options.headless = False
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    browser.get(link)
    browser.implicitly_wait(10)

    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()
    browser.implicitly_wait(10)

    yield browser
    browser.quit()


# эта фикстура делает скриншот при failed test
# poetry run pytest --alluredir=allure-results
# allure serve allure-results


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        try:
            with open("failures", mode) as f:
                if "browser" in item.fixturenames:
                    web_driver = item.funcargs["browser"]
                else:
                    print("Fail to take screen-shot")
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=AttachmentType.PNG,
            )
        except Exception as e:
            print("Fail to take screen-shot: {}".format(e))
