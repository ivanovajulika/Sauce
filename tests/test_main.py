import pytest
import allure
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.item_id4 import ItemPage_4
from pages.checkout_page import Checkout_page
from pages.inventory_page import ALL_ID, ALL_NAMES


link = "https://www.saucedemo.com/inventory.html"


@allure.feature("US_002.00 | Products > Страница выбора товаров.")
@allure.story("TC_002.01.01 | Products > Количество товаров на странице 'Products'")
def test_count_products(browser):
    page = InventoryPage(browser, link)
    page.count_products()


@allure.feature("US_002.00 | Products > Страница выбора товаров.")
@allure.story("TC_002.01.02 | Products > Фото товара на странице 'Products'")
def test_photo_products(browser):
    page = InventoryPage(browser, link)
    page.should_be_img_all_item()


@allure.feature("US_002.00 | Products > Страница выбора товаров.")
@allure.story("TC_002.02.01 | Products > Цена товара на странице 'Products' - Backpack")
@allure.severity("minor")
def test_link_to_price_backpack(browser):
    page = InventoryPage(browser, link)
    page.should_be_item_backpack()
    page.price_backpack()


@allure.feature("US_002.00 | Products > Страница выбора товаров.")
@allure.story(
    "TC_002.02.02 | Products > Цена товара на странице 'Products' - Bolt T-Shirt"
)
@allure.severity("minor")
def test_link_to_price_t_shirt(browser):
    page = InventoryPage(browser, link)
    page.should_be_item_t_shirt()
    page.price_t_shirt()


@allure.feature("US_002.00 | Products > Страница выбора товаров.")
@allure.story("TC_002.02.03 | Products > Цена товара на странице 'Products' - Onesie")
@allure.severity("minor")
def test_link_to_price_onesie(browser):
    page = InventoryPage(browser, link)
    page.should_be_item_onesie()
    page.price_onesie()


@allure.feature("US_002.00 | Products > Страница выбора товаров.")
@allure.story(
    "TC_002.02.04 | Products > Цена товара на странице 'Products' - Bike Light"
)
@allure.severity("minor")
def test_link_to_price_bike_light(browser):
    page = InventoryPage(browser, link)
    page.should_be_item_bike_light()
    page.price_bike_light()


@allure.feature("US_002.00 | Products > Страница выбора товаров.")
@allure.story(
    "TC_002.02.05 | Products > Цена товара на странице 'Products' - Fleece Jacket"
)
@allure.severity("minor")
def test_link_to_price_fleece_jacket(browser):
    page = InventoryPage(browser, link)
    page.should_be_item_fleece_jacket()
    page.price_fleece_jacket()


@allure.feature("US_002.00 | Products > Страница выбора товаров.")
@allure.story(
    "TC_002.02.06 | Products > Цена товара на странице 'Products' - T-Shirt (Red)"
)
@allure.severity("minor")
def test_link_to_price_t_shirt_red(browser):
    page = InventoryPage(browser, link)
    page.should_be_item_t_shirt_red()
    page.price_t_shirt_red()


@allure.feature("US_002.00 | Products > Страница выбора товаров.")
@allure.story(
    "TC_002.04.00 | Products > Ссылка на страницу товара из карточки товара 'Products'."
)
@allure.severity("critical")
def test_get_all_links(browser):
    all_names = browser.find_elements(*ALL_NAMES)
    list_all_link = []
    for index in range(len(all_names)):
        name = browser.find_elements(*ALL_NAMES)[index]
        name.click()
        link = browser.current_url
        list_all_link.append(link[-4:])
        page = ItemPage_4(browser, link)
        page.return_to_inventory_page()

    all_id = browser.find_elements(*ALL_ID)
    list_all_id = []
    for i in range(len(all_id)):
        id_ = all_id[i].get_attribute("id")
        id = "id=" + id_[5]
        list_all_id.append(id)

    assert list_all_id == list_all_link, "Wrong page"


@allure.feature("US_003.00 | Inventory item > Страница товара.")
@allure.story(
    "TC_003.00.01 | Inventory item > Переход на страницу товара по клику на картинку товара в его карточке."
)
def test_link_go_from_img(browser):
    page = InventoryPage(browser, link)
    page.img_backpack()
    page = ItemPage_4(browser, link)
    page.photo_size_required()


@allure.feature("US_003.00 | Inventory item > Страница товара.")
@allure.story(
    "TC_003.00.02 | Inventory item > Добавление товара в корзину на странице 'Inventory item'"
)
def test_add_all_products_by_one(browser):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(browser, link)
    list_all_names = page.get_all_names()
    count = len(list_all_names)
    for index in range(count):
        name = browser.find_elements(*ALL_NAMES)[index]
        name.click()
        link = browser.current_url
        page = ItemPage_4(browser, link)
        page.add_to_cart_btn_is_present()
        page.add_to_cart()
        page.cart_counter(quantity="1")
        page.go_to_cart()
        page = CartPage(browser, link)
        page.cart_page_counter(quantity="1")
        page.reset_cart()
        page.return_to_inventory_page()


@allure.feature("US_003.00 | Inventory item > Страница товара.")
@allure.story(
    "TC_003.00.03 | Inventory item > Удаление товара из корзины на странице 'Inventory item'."
)
def test_add_remove_backpack(browser):
    link = "https://www.saucedemo.com/inventory-item.html?id=4"
    page = ItemPage_4(browser, link)
    page.add_to_cart()
    page.remove_from_cart_btn()
    browser.implicitly_wait(5)
    page.cart_counter(quantity="1")
    page.go_to_cart()
    page = CartPage(browser, link)
    page.cart_page_counter(quantity="1")
    page.return_to_item_page()
    page = ItemPage_4(browser, link)
    page.remove_from_cart()
    page.add_to_cart_btn_is_present()
    page.empty_cart_counter()
    page.go_to_cart()
    page = CartPage(browser, link)
    page.empty_cart_page()


@allure.feature("US_004.00 | Your cart > Страница корзины. Кнопка 'Корзина'.")
@allure.story(
    "TC_004.01.01 | Your cart > Cоответствие выбранного товара добавленному в 'Корзину'."
)
def test_conformity_item(browser):
    # Создаем экземпляр страницы с товарами
    page = InventoryPage(browser, link)
    # Создаем словарь из значений товара и кладем его в корзину
    dict_id5 = page.list_item()
    # Переходим в корзину
    page.go_to_cart()
    # Создаем экземпляр страницы корзины
    page = CartPage(browser, link)
    # Создаем словарь из значений товара в корзине
    dict_id5_item = page.list_item_id5()
    assert dict_id5_item == dict_id5


@allure.feature("US_004.00 | Your cart > Страница корзины. Кнопка 'Корзина'.")
@allure.story(
    "TC_004.01.02 | Your cart > Работа кнопки 'Корзина': ввод валидных данных - добавить 1 товар в корзину."
)
def test_add_to_cart_random_item(browser):
    page = InventoryPage(browser, link)
    # добавить в корзину 1 любой товар
    page.add_to_cart_random()
    # проверить, что кнопка remove присутствует
    page.btn_remove_is_present_random()
    # Создаем список из списков всех товаров положенных в корзину
    list_all_remove = page.get_all_items_remove()
    # проверяем счетчик на кнопке Корзина
    page.cart_counter(quantity="1")
    # перейти в корзину
    page.go_to_cart()
    # создаем экземпляр страницы корзины
    page = CartPage(browser, link)
    # Создаем список из списков всех товаров в корзине
    list_all_items_in_cart = page.all_items()
    assert list_all_remove == list_all_items_in_cart


@allure.feature("US_004.00 | Your cart > Страница корзины. Кнопка 'Корзина'.")
@allure.story(
    "TC_004.01.04 | Your cart >  проверить количество выбранного товара в корзине."
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
@allure.story("TC_004.03.01 | Your cart > Оформление заказа с пустой Корзиной.")
@pytest.mark.xfail
def test_empty_cart_order(browser):
    # Негативный тест-кейс - не должно быть перехода на checkout-complete!
    page = InventoryPage(browser, link)
    page.empty_cart_counter()
    page.go_to_cart()
    page = CartPage(browser, link)
    page.empty_cart_page()
    page.checkout_btn()
    page = Checkout_page(browser, link)
    page.checkout_user()
    page.finish_btn()


@allure.feature("US_004.00 | Your cart > Страница корзины. Кнопка 'Корзина'.")
@allure.story(
    "TC_004.04.00 | Your cart > Положить в корзину все товары и проверить в корзине соответствие названия, описания, цены."
)
def test_conform_all_items(browser):
    # Создаем экземпляр страницы с товарами
    page = InventoryPage(browser, link)
    # Создаем список из списков всех товаров
    list_all_items = page.all_items()
    # Добавляем в корзину все товары
    page.add_all_items()
    # Переходим в корзину
    page.go_to_cart()
    # Создаем экземпляр страницы корзины
    page = CartPage(browser, link)
    # Создаем список из списков всех товаров в корзине
    list_all_items_in_cart = page.all_items()
    assert list_all_items == list_all_items_in_cart


@allure.feature("US_010.00 | Filter")
@allure.story("TC_010.00.01 | Filter > Проверка наличия фильтра на странице 'Products'")
def test_filter_is_present(browser):
    assert "inventory" in browser.current_url, "Wrong page"
    page = InventoryPage(browser, link)
    page.should_be_filter()


@allure.feature("US_010.00 | Filter")
@allure.story("TC_010.00.02 | Filter > Работа фильтра на странице 'Products' (Z-A).")
def test_sorted_z_to_a(browser):
    assert "inventory" in browser.current_url, "Wrong page"
    page = InventoryPage(browser, link)
    # нажать на символ фильтр
    page.click_filter()
    # выбрать в дропдаун меню Z-A
    page.choice_z_a()
    # создать список из всех наименований товаров
    list_all_names = page.get_all_names()
    # проверить, что все наименования отсортированы.
    assert sorted(list_all_names, reverse=True) == list_all_names


@allure.feature("US_010.00 | Filter")
@allure.story("TC_010.00.03 | Filter > Работа фильтра на странице 'Products' (A-Z).")
def test_sorted_a_to_z(browser):
    assert "inventory" in browser.current_url, "Wrong page"
    page = InventoryPage(browser, link)
    # нажать на символ фильтр
    page.click_filter()
    # выбрать в дропдаун меню Z-A
    page.choice_a_z()
    # создать список из всех наименований товаров
    list_all_names = page.get_all_names()
    # проверить, что все наименования отсортированы.
    assert sorted(list_all_names, reverse=False) == list_all_names


@allure.feature("US_010.00 | Filter")
@allure.story(
    "TC_010.00.04 | Filter > Работа фильтра Price на странице 'Products' (low to high)"
)
def test_sorted_low_to_hi(browser):
    assert "inventory" in browser.current_url, "Wrong page"
    page = InventoryPage(browser, link)
    # нажать на символ фильтр
    page.click_filter()
    # выбрать в дропдаун меню Price (low to high)
    page.choice_price_lo_to_hi()
    # создать список из всех цен товаров
    list_all_prices = page.get_all_prices()
    # проверить, что все наименования отсортированы.
    assert sorted(list_all_prices, reverse=False) == list_all_prices


@allure.feature("US_010.00 | Filter")
@allure.story(
    "TC_010.00.05 | Filter > Работа фильтра Price на странице 'Products' (high to low)"
)
def test_sorted_hi_to_low(browser):
    assert "inventory" in browser.current_url, "Wrong page"
    page = InventoryPage(browser, link)
    # нажать на символ фильтр
    page.click_filter()
    # выбрать в дропдаун меню Price (high to low)
    page.choice_price_hi_to_lo()
    # создать список из всех цен товаров
    list_all_prices = page.get_all_prices()
    # проверить, что все наименования отсортированы.
    assert sorted(list_all_prices, reverse=True) == list_all_prices
