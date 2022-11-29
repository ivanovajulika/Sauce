import allure
from pages.inventory_page import InventoryPage

link = "https://www.saucedemo.com/inventory.html"


@allure.feature("US_008.00 | Header")
@allure.story(
    "TC_008.01.01 | Header > Наличие хедера и его элементов на страницe 'Products'."
)
def test_should_be_elements_of_header(browser):
    page = InventoryPage(browser, link)
    page.should_be_logo()
    page.should_be_menu_sidebar()
    page.element_cart()
    page.should_be_hover()
