from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# locators
BTN_FILTER = (By.CLASS_NAME, "product_sort_container")
ALL_NAMES = (By.CLASS_NAME, "inventory_item_name")
ALL_ID = (By.XPATH, "//*[@id]//a//div/..")
ALL_DESC = (By.CSS_SELECTOR, ".inventory_item_desc")
ALL_PRICES = (By.CLASS_NAME, "inventory_item_price")
ALL_IMG = (By.CSS_SELECTOR, "[class='inventory_item_img']:nth-last-child(1)")
BTN_ADD = (By.CLASS_NAME, "btn_primary")


class InventoryPage(BasePage):
    # на странице "Products" кликнуть по 'Backpack'
    # переход на страницу 'Backpack'
    def item_backpack(self):
        self.browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]').click()
        assert "id=4" in self.browser.current_url, "Wrong page"

    def should_be_item_backpack(self):
        assert self.element_is_present(By.ID, "item_4_title_link"), "Element is absent"

    # переход по клику на картинку
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

    # проверка наличия фотографий всех товаров
    def should_be_img_all_item(self):
        list_required_img = [
            "https://www.saucedemo.com/static/media/sauce-backpack-1200x1500.34e7aa42.jpg",
            "https://www.saucedemo.com/static/media/bike-light-1200x1500.a0c9caae.jpg",
            "https://www.saucedemo.com/static/media/bolt-shirt-1200x1500.c0dae290.jpg",
            "https://www.saucedemo.com/static/media/sauce-pullover-1200x1500.439fc934.jpg",
            "https://www.saucedemo.com/static/media/red-onesie-1200x1500.1b15e1fa.jpg",
            "https://www.saucedemo.com/static/media/red-tatt-1200x1500.e32b4ef9.jpg",
        ]
        all_img = list(self.browser.find_elements(*ALL_IMG))
        list_all_img = []
        for number, img in enumerate(all_img):
            img = all_img[number].get_attribute("src")
            list_all_img.append(img)
        assert list_all_img == list_required_img

    # Добавляем все товары в корзину
    def add_all_items(self):
        add_cart = list(self.browser.find_elements(*BTN_ADD))
        for btn_add_cart in add_cart:
            btn_add_cart.click()

    def add_to_cart_backpack(self):
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"
        ).click()

    def add_to_cart_bike_light(self):
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light"
        ).click()

    def add_to_cart_bolt_t_shirt(self):
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()

    def add_to_cart_fleece_jacket(self):
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket"
        ).click()

    def add_to_cart_onesie(self):
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"
        ).click()

    def add_to_cart_allthethings_t_shirt(self):
        self.browser.find_element(By.XPATH, "//div[6]/div[2]/div[2]/button").click()

    def count_products_in_the_cart(self):
        elements = len(self.browser.find_elements(By.CSS_SELECTOR, ".cart_item"))
        assert elements == 6

    # Создаем список из списков всех товаров
    def all_items(self):

        all_names = list(self.browser.find_elements(*ALL_NAMES))
        list_all_names = [name.text for name in all_names]

        all_desc = list(self.browser.find_elements(*ALL_DESC))
        list_all_desc = [desc.text for desc in all_desc]

        all_prices = list(self.browser.find_elements(*ALL_PRICES))
        list_all_prices = [price.text for price in all_prices]

        list_all = [
            (list_all_names[i], list_all_desc[i], list_all_prices[i])
            for i in range(len(all_names))
        ]
        return list_all

    # Словарь название, описание и цена 5 товара
    # И кладем его в корзину
    def list_item(self):
        title = self.browser.find_element(
            By.CSS_SELECTOR, "#item_5_title_link > div"
        ).text
        desc = self.browser.find_element(
            By.XPATH, '(//*[@class="inventory_item_desc"])[4]'
        ).text
        pr = self.browser.find_element(
            By.XPATH, '(//*[@class="inventory_item_price"])[4]'
        ).text
        dict_id5 = {"name": title, "description": desc, "price": pr}
        self.browser.find_element(
            By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'
        ).click()
        return dict_id5
