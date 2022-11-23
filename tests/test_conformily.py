from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By
import allure
import time

link = "https://www.saucedemo.com/inventory.html"
ALL_NAMES = (By.CLASS_NAME, "inventory_item_name")
ALL_DESC = (By.CSS_SELECTOR, ".inventory_item_desc")
ALL_PRICES = (By.CLASS_NAME, "inventory_item_price")


@allure.feature("US_004.00 | Your cart > Страница корзины. Кнопка 'Корзина'.")
@allure.story(
    "TC_004.01.01 | Your cart > Cоответствие выбранного товара добавленному в 'Корзину'."
)
def test_conformity_item(browser):
    page = InventoryPage(browser, link)

    title = browser.find_element(By.CSS_SELECTOR, "#item_5_title_link > div").text
    desc = browser.find_element(By.XPATH, '(//*[@class="inventory_item_desc"])[4]').text
    pr = browser.find_element(By.XPATH, '(//*[@class="inventory_item_price"])[4]').text
    dict_id5 = {"name": title, "description": desc, "price": pr}
    browser.find_element(
        By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'
    ).click()

    page.go_to_cart()

    title_item = browser.find_element(By.CSS_SELECTOR, "#item_5_title_link > div").text
    desc_item = browser.find_element(
        By.XPATH, '(//*[@class="inventory_item_desc"])'
    ).text
    pr_item = browser.find_element(
        By.XPATH, '(//*[@class="inventory_item_price"])'
    ).text
    dict_id5_item = {"name": title_item, "description": desc_item, "price": pr_item}

    assert dict_id5_item == dict_id5


@allure.feature("US_004.00 | Your cart > Страница корзины. Кнопка 'Корзина'.")
@allure.story(
    "TC_004-01-04 | Your cart >  проверить количество выбранного товара в корзине."
)
def test_add_to_cart_btn_add(browser):
    page = InventoryPage(browser, link)
    page.add_to_cart_backpack()
    page.cart_counter(quantity="1")
    page.add_to_cart_bike_light()
    page.cart_counter(quantity="2")
    page.add_to_cart_bolt_t_shirt()
    page.cart_counter(quantity="3")
    page.add_to_cart_fleece_jacket()
    page.cart_counter(quantity="4")
    page.add_to_cart_onesie()
    page.cart_counter(quantity="5")
    page.add_to_cart_allthethings_t_shirt()
    page.cart_counter(quantity="6")
    page.go_to_cart()
    page.count_products_in_the_cart()


@allure.feature("US_004.00 | Your cart > Страница корзины. Кнопка 'Корзина'.")
@allure.story(
    "TC_004-04-00 | Your cart >  проверить в корзине соответствие названия, описания, цены."
)
def test_conform_all_items(browser):
    page = InventoryPage(browser, link)
    page.open_page()
    all_names = list(browser.find_elements(*ALL_NAMES))
    list_all_names = []
    list_all = []
    list_all_in_cart = []
    for count, name in enumerate(all_names):
        name = all_names[count].text
        list_all_names.append(name)

    all_desc = list(browser.find_elements(*ALL_DESC))
    list_all_desc = []
    for count, desc in enumerate(all_desc):
        desc = all_desc[count].text
        list_all_desc.append(desc)

    all_prices = list(browser.find_elements(*ALL_PRICES))
    list_all_prices = []
    for count, name in enumerate(all_prices):
        name = all_prices[count].text
        list_all_prices.append(float(name[1:]))

    for i in range(len(list_all_desc)):
        list_all.append(list((list_all_names[i], list_all_desc[i], list_all_prices[i])))

    page.add_all_items()
    time.sleep(5)
    page.go_to_cart()
    page = CartPage(browser, link)
    page.open_page()

    all_names = list(browser.find_elements(*ALL_NAMES))
    list_all_names_cart = []
    for count, name in enumerate(all_names):
        name = all_names[count].text
        list_all_names_cart.append(name)

    all_desc = list(browser.find_elements(*ALL_DESC))
    list_all_desc_cart = []
    for count, desc in enumerate(all_desc):
        desc = all_desc[count].text
        list_all_desc_cart.append(desc)

    all_prices = list(browser.find_elements(*ALL_PRICES))
    list_all_prices_cart = []
    for count, name in enumerate(all_prices):
        name = all_prices[count].text
        list_all_prices_cart.append(float(name[1:]))

    for i in range(len(list_all_desc)):
        list_all_in_cart.append(
            list(
                (list_all_names_cart[i], list_all_desc_cart[i], list_all_prices_cart[i])
            )
        )

    time.sleep(5)
    assert list_all == list_all_in_cart
