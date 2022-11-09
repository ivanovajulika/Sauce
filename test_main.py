from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

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
    browser.implicitly_wait(1)

    username_input = browser.find_element(By.XPATH, '//*[@id="user-name"]')
    username_input.send_keys(standard_user)
    password_input = browser.find_element(By.XPATH, '//*[@id="password"]')
    password_input.send_keys(password)
    btn_login = browser.find_element(By.XPATH, '//*[@id="login-button"]')
    btn_login.click()
    browser.implicitly_wait(10)
    assert "inventory" in browser.current_url, "Wrong page"
    browser.quit()  # comment
