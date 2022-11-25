from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import allure

link = "https://www.saucedemo.com/inventory.html"


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
    "TC_004-04-00 | Your cart > Положить в корзину все товары и проверить в корзине соответствие названия, описания, цены."
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
