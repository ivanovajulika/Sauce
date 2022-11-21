from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# locators
BTN_FILTER = (By.CLASS_NAME, "product_sort_container")
ALL_NAMES = (By.CLASS_NAME, "inventory_item_name")
ALL_PRICES = (By.CLASS_NAME, "inventory_item_price")


class InventoryPage(BasePage):
    def element_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, ".shopping_cart_container")

    def item_backpack(self):
        self.browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]').click()
        assert "id=4" in self.browser.current_url, "Wrong page"

    def should_be_item_backpack(self):
        assert self.element_is_present(By.ID, "item_4_title_link"), "Element is absent"

    def img_backpack(self):
        self.browser.find_element(By.CSS_SELECTOR, "#item_4_img_link > img").click()
        assert "id=4" in self.browser.current_url, "Wrong page"

    def count_products(self):
        elements = len(self.browser.find_elements(By.CSS_SELECTOR, ".inventory_item"))
        assert elements == 6

    def price_backpack(self):
        price = self.browser.find_element(
            By.XPATH, "(//*[@class='inventory_item_price'])[1]"
        ).text
        assert price == "$29.99", "Wrong price"

    # проверка наличия фильтра
    def should_be_filter(self):
        assert self.element_is_present(*BTN_FILTER), "Element is absent"

    # нажать кнопку фильтр
    def click_filter(self):
        self.browser.find_element(*BTN_FILTER).click()

    # выбор меню фильтра Z-A
    def choice_z_a(self):
        select = Select(self.browser.find_element(By.TAG_NAME, "select"))
        select.select_by_value("za")

    # выбор меню фильтра A-Z
    def choice_a_z(self):
        select = Select(self.browser.find_element(By.TAG_NAME, "select"))
        select.select_by_value("az")

    # выбор меню фильтра Price (low to high)
    def choice_price_lo_to_hi(self):
        select = Select(self.browser.find_element(By.TAG_NAME, "select"))
        select.select_by_value("lohi")

    # выбор меню фильтра Price (high to low)
    def choice_price_hi_to_lo(self):
        select = Select(self.browser.find_element(By.TAG_NAME, "select"))
        select.select_by_value("hilo")

    # проверка сортировки списка названий товаров в реверсивном порядке
    def get_all_names_and_sort_reverse_alfabet(self):
        all_names = list(self.browser.find_elements(*ALL_NAMES))
        list_all_names = []
        for count, name in enumerate(all_names):
            name = all_names[count].text
            list_all_names.append(name)
        assert sorted(list_all_names, reverse=True) == list_all_names

    #  проверка сортировки списка названий товаров в алфавитном порядке
    def get_all_names_and_sort_alfabet(self):
        all_names = list(self.browser.find_elements(*ALL_NAMES))
        list_all_names = []
        for count, name in enumerate(all_names):
            name = all_names[count].text
            list_all_names.append(name)
        assert sorted(list_all_names, reverse=False) == list_all_names

    # проверка сортировки по цене товара low to hi
    def get_all_prices_and_sort_low_to_hi(self):
        all_prices = list(self.browser.find_elements(*ALL_PRICES))
        list_all_prices = []
        for count, name in enumerate(all_prices):
            name = all_prices[count].text
            list_all_prices.append(float(name[1:]))
        assert sorted(list_all_prices, reverse=False) == list_all_prices

        # проверка сортировки по цене товара в hi to low порядке

    def get_all_prices_and_sort_hi_to_low(self):
        all_prices = list(self.browser.find_elements(*ALL_PRICES))
        list_all_prices = []
        for count, name in enumerate(all_prices):
            name = all_prices[count].text
            list_all_prices.append(float(name[1:]))
        assert sorted(list_all_prices, reverse=True) == list_all_prices

    def should_be_img_backpack(self):
        element = self.browser.find_element(By.CSS_SELECTOR, "#item_4_img_link > img")
        img = element.get_attribute("src")
        assert (
            img
            == "https://www.saucedemo.com/static/media/sauce-backpack-1200x1500.34e7aa42.jpg"
        )

    def should_be_img_bike_light(self):
        element = self.browser.find_element(By.CSS_SELECTOR, "#item_0_img_link > img")
        img = element.get_attribute("src")
        assert (
            img
            == "https://www.saucedemo.com/static/media/bike-light-1200x1500.a0c9caae.jpg"
        )

    def should_be_img_bolt_t_shirt(self):
        element = self.browser.find_element(By.CSS_SELECTOR, "#item_1_img_link > img")
        img = element.get_attribute("src")
        assert (
            img
            == "https://www.saucedemo.com/static/media/bolt-shirt-1200x1500.c0dae290.jpg"
        )

    def should_be_img_fleece_jacket(self):
        element = self.browser.find_element(By.CSS_SELECTOR, "#item_5_img_link > img")
        img = element.get_attribute("src")
        assert (
            img
            == "https://www.saucedemo.com/static/media/sauce-pullover-1200x1500.439fc934.jpg"
        )

    def should_be_img_onesie(self):
        element = self.browser.find_element(By.CSS_SELECTOR, "#item_2_img_link > img")
        img = element.get_attribute("src")
        assert (
            img
            == "https://www.saucedemo.com/static/media/red-onesie-1200x1500.1b15e1fa.jpg"
        )

    def should_be_img_t_shirt(self):
        element = self.browser.find_element(By.CSS_SELECTOR, "#item_3_img_link > img")
        img = element.get_attribute("src")
        assert (
            img
            == "https://www.saucedemo.com/static/media/red-tatt-1200x1500.e32b4ef9.jpg"
        )
