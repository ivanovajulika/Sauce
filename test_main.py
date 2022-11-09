from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

username = "standard_user"
password = "secret_sauce"


def test_user_can_auth():

    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1080")
    options.headless = True
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    browser.get("https://www.saucedemo.com/")
    browser.implicitly_wait(1)

    username_input = browser.find_element(By.XPATH, '//*[@id="user-name"]')
    username_input.send_keys(username)
    password_input = browser.find_element(By.XPATH, '//*[@id="password"]')
    password_input.send_keys(password)
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    browser.implicitly_wait(10)
    browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').click()
    browser.quit()
