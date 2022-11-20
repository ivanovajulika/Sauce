from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.item_id4 import ItemPage_4
import allure
from allure_commons.types import AttachmentType


# это пример теста
@allure.feature("Sauce Labs")
@allure.story("ТС_001_01 это пример теста")
@allure.severity("blocker")
def test_user_can_go_cart(browser):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(browser, link)
    # page.open_page()
    page.element_cart()


# это пример теста
@allure.feature("Sauce Labs")
@allure.story("ТС_001_02 это пример теста")
@allure.severity("critical")
def test_user_can_go_continue_shopping(browser):
    link = "https://www.saucedemo.com/cart.html"
    page = CartPage(browser, link)
    page.open_page()
    page.user_can_go_continue_shopping()
    with allure.step("Делаем скриншот"):
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG,
        )


@allure.feature("US_002.00 | Products > Страница выбора товаров.")
@allure.story("TC_002.01.01 | Products > Количество товаров на странице 'Products'")
def test_count_products(browser):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(browser, link)
    # page.open_page()
    page.count_products()


@allure.feature("US_002.00 | Products > Страница выбора товаров.")
@allure.story("TC_002.01.02 | Products > Фото товара на странице 'Products'")
def test_photo_products(browser):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(browser, link)
    # page.open_page()
    page.should_be_img_backpack()
    page.should_be_img_bike_light()
    page.should_be_img_bolt_t_shirt()
    page.should_be_img_fleece_jacket()
    page.should_be_img_onesie()
    page.should_be_img_t_shirt()


@allure.feature("US_002.00 | Products > Страница выбора товаров.")
@allure.story("TC_002.02.01 | Products > Цена товара на странице 'Products' - Backpack")
@allure.severity("minor")
def test_link_to_price_backpack(browser):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(browser, link)
    # page.open_page()
    page.should_be_item_backpack()
    page.price_backpack()


@allure.feature("US_002.00 | Products > Страница выбора товаров.")
@allure.story(
    "TC_002.04.01 | Products > Ссылка на страницу товара из карточки товара 'Products' - Backpack."
)
@allure.severity("critical")
def test_link_to_inventory_backpack(browser):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(browser, link)
    # page.open_page()
    page.should_be_item_backpack()
    page.item_backpack()


@allure.feature("US_003.00 | Inventory item > Страница товара.")
@allure.story(
    "TC_003.00.01 | Inventory item > Переход на страницу товара по клику на картинку товара в его карточке."
)
def test_link_go_from_img(browser):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(browser, link)
    page.open_page()
    page.img_backpack()
    link = "https://www.saucedemo.com/inventory-item.html?id=4"
    page = ItemPage_4(browser, link)
    page.photo_size_required()


@allure.feature("US_003.00 | Inventory item > Страница товара.")
@allure.story(
    "TC_003.00.03 | Inventory item > Удаление товара из корзины на странице 'Inventory item'."
)
def test_add_remove_backpack(browser):
    link = "https://www.saucedemo.com/inventory-item.html?id=4"
    page = ItemPage_4(browser, link)
    # page.open_page()
    page.add_to_cart()
    page.remove_from_cart_btn()
    page.cart_counter(quantity="1")
    page.go_to_cart()
    page.cart_page_counter()
    page.return_to_item_page()
    page.remove_from_cart()
    page.add_to_cart_btn()
    page.empty_cart_counter()
    page.go_to_cart()
    page.empty_cart()


@allure.feature("US_010.00 | Filter")
@allure.story("TC_010.00.01 | Filter > Проверка наличия фильтра на странице 'Products'")
def test_filter_is_present(browser):
    assert "inventory" in browser.current_url, "Wrong page"
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(browser, link)
    page.should_be_filter()
