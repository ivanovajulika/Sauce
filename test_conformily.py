import pytest
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
import allure

link = "https://www.saucedemo.com/inventory.html"


@allure.feature("US_004.00 | Your cart > Страница корзины. Кнопка 'Корзина'.")
@allure.story(
    "TC_004.01.01 | Your cart > Cоответствие выбранного товара добавленному в 'Корзину'."
)
def test_conformity_item(browser):
    page = InventoryPage(browser, link)

    title = browser.find_element(By.CSS_SELECTOR, "#item_5_title_link > div").text
    desc = browser.find_element(
        By.XPATH, '//*[@id="inventory_container"]//div[4]/div[2]/div[1]/div'
    ).text
    pr = browser.find_element(
        By.XPATH, '//*[@id="inventory_container"]//div[4]/div[2]/div[2]/div'
    ).text
    dict_id5 = {"name": title, "description": desc, "price": pr}
    browser.find_element(
        By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'
    ).click()

    page.go_to_cart()

    title_item = browser.find_element(By.CSS_SELECTOR, "#item_5_title_link > div").text
    desc_item = browser.find_element(
        By.XPATH, '//*[@id="cart_contents_container"]//div[1]/div[3]/div[2]/div[1]'
    ).text
    pr_item = browser.find_element(
        By.XPATH,
        '//*[@id="cart_contents_container"]//div[1]/div[3]/div[2]/div[2]/div',
    ).text
    dict_id5_item = {"name": title_item, "description": desc_item, "price": pr_item}

    assert dict_id5_item == dict_id5
