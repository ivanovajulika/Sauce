from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from enchant.checker import SpellChecker
import random

# locators
BTN_FILTER = (By.CLASS_NAME, "product_sort_container")
ALL_NAMES = (By.CLASS_NAME, "inventory_item_name")
ALL_ID = (By.XPATH, "//*[@id]//a//div/..")
ALL_DESC = (By.CSS_SELECTOR, ".inventory_item_desc")
ALL_PRICES = (By.CLASS_NAME, "inventory_item_price")
ALL_IMG = (By.CSS_SELECTOR, "[class='inventory_item_img']:nth-last-child(1)")
BTN_ADD = (By.CLASS_NAME, "btn_primary")
BTN_REMOVE = (By.CSS_SELECTOR, "button[name^='remove-sauce']")
ALL_NAMES_REMOVE = (By.XPATH, "//button[contains(text(),'Remove')]/../../div/a/div")
ALL_DESC_REMOVE = (
    By.XPATH,
    "//button[contains(text(),'Remove')]/../../div/div[@class='inventory_item_desc']",
)
ALL_PRICES_REMOVE = (
    By.XPATH,
    "//button[contains(text(),'Remove')]/../../div/following-sibling::div/div",
)
BACKPACK = (By.XPATH, '//*[@id="item_4_title_link"]')
BOLT_T_SHIRT = (By.ID, "item_1_title_link")
ONESIE = (By.ID, "item_2_title_link")
BIKE_LIGHT = (By.ID, "item_0_title_link")
FLEECE_JACKET = (By.ID, "item_5_title_link")
T_SHIRT_RED = (By.ID, "item_3_title_link")


class InventoryPage(BasePage):
    def item_backpack(self):
        """Метод находит на странице Products товар Backpack,
        кликает на него и переходит в его карточку товара,
        проверяет что находится в нужной карточке товара"""
        self.browser.find_element(*BACKPACK).click()
        assert "id=4" in self.browser.current_url, "Wrong page"

    def should_be_item_backpack(self):
        """Метод проверяет на странице Products наличие товара Backpack"""
        assert self.element_is_present(*BACKPACK), "Element is absent"

    def should_be_item_t_shirt(self):
        """Метод проверяет на странице Products наличие товара Bolt T-shirt"""
        assert self.element_is_present(*BOLT_T_SHIRT), "Element is absent"

    def should_be_item_onesie(self):
        """Метод проверяет на странице Products наличие товара Onesie"""
        assert self.element_is_present(*ONESIE), "Element is absent"

    def should_be_item_bike_light(self):
        """Метод проверяет на странице Products наличие товара Bike Light"""
        assert self.element_is_present(*BIKE_LIGHT), "Element is absent"

    def should_be_item_fleece_jacket(self):
        """Метод проверяет на странице Products наличие товара Fleece Jacket"""
        assert self.element_is_present(*FLEECE_JACKET), "Element is absent"

    def should_be_item_t_shirt_red(self):
        """Метод проверяет на странице Products наличие товара T-shirt (Red)"""
        assert self.element_is_present(*T_SHIRT_RED), "Element is absent"

    def should_be_description_backpack(self):
        """Метод проверяет на странице Products наличие описания товара Backpack"""
        assert self.element_is_present(
            By.XPATH, "(//*[@class='inventory_item_desc'])[1]"
        ), "Element is absent"

    def should_be_description_t_shirt(self):
        """Метод проверяет на странице Products наличие описания товара Bolt T-shirt"""
        assert self.element_is_present(
            By.XPATH, "(//*[@class='inventory_item_desc'])[3]"
        ), "Element is absent"

    def should_be_description_onesie(self):
        """Метод проверяет на странице Products наличие описания товара Onesie"""
        assert self.element_is_present(
            By.XPATH, "(//*[@class='inventory_item_desc'])[5]"
        ), "Element is absent"

    def should_be_description_bike_light(self):
        """Метод проверяет на странице Products наличие описания товара Bike Light"""
        assert self.element_is_present(
            By.XPATH, "(//*[@class='inventory_item_desc'])[2]"
        ), "Element is absent"

    def should_be_description_fleece_jacket(self):
        """Метод проверяет на странице Products наличие описания товара Fleece Jacket"""
        assert self.element_is_present(
            By.XPATH, "(//*[@class='inventory_item_desc'])[4]"
        ), "Element is absent"

    def should_be_description_t_shirt_red(self):
        """Метод проверяет на странице Products наличие описания товара T-shirt (Red)"""
        assert self.element_is_present(
            By.XPATH, "(//*[@class='inventory_item_desc'])[6]"
        ), "Element is absent"

    def img_backpack(self):
        """Метод находит на странице Products товар Backpack,
        кликает на его фото и переходит в его карточку товара,
         проверяет что находится в нужной карточке товара"""
        self.browser.find_element(By.CSS_SELECTOR, "#item_4_img_link > img").click()
        assert "id=4" in self.browser.current_url, "Wrong page"

    def count_products(self):
        """Метод подсчитывает общее количество товаров на странице Products и
        проверяет, что их 6"""
        elements = len(self.browser.find_elements(By.CSS_SELECTOR, ".inventory_item"))
        assert elements == 6

    def price_backpack(self):
        """Метод находит цену товара Backpack и проверяет, что цена $29.99"""
        price = self.browser.find_element(
            By.XPATH, "(//*[@class='inventory_item_price'])[1]"
        ).text
        assert price == "$29.99", "Wrong price"

    def price_t_shirt(self):
        """Метод находит цену товара Bolt T-shirt и проверяет, что цена $15.99"""
        price = self.browser.find_element(
            By.XPATH, "(//*[@class='inventory_item_price'])[3]"
        ).text
        assert price == "$15.99", "Wrong price"

    def price_onesie(self):
        """Метод находит цену товара Onesie и проверяет, что цена $7.99"""
        price = self.browser.find_element(
            By.XPATH, "(//*[@class='inventory_item_price'])[5]"
        ).text
        assert price == "$7.99", "Wrong price"

    def price_bike_light(self):
        """Метод находит цену товара Bike Light и проверяет, что цена $9.99"""
        price = self.browser.find_element(
            By.XPATH, "(//*[@class='inventory_item_price'])[2]"
        ).text
        assert price == "$9.99", "Wrong price"

    def price_fleece_jacket(self):
        """Метод находит цену товара Fleece Jacket и проверяет, что цена $49.99"""
        price = self.browser.find_element(
            By.XPATH, "(//*[@class='inventory_item_price'])[4]"
        ).text
        assert price == "$49.99", "Wrong price"

    def price_t_shirt_red(self):
        """Метод находит цену товара T-shirt (Red) и проверяет, что цена $15.99"""
        price = self.browser.find_element(
            By.XPATH, "(//*[@class='inventory_item_price'])[6]"
        ).text
        assert price == "$15.99", "Wrong price"

    def should_be_filter(self):
        """Метод проверяет на странице Products наличие элемента Filter"""
        assert self.element_is_present(*BTN_FILTER), "Element is absent"

    def click_filter(self):
        """Метод на странице Products кликает элемент Filter и вызывает появление drop-down menu"""
        self.browser.find_element(*BTN_FILTER).click()

    def choice_z_a(self):
        """Метод выбирает в drop-down menu элемента Filter пункт Name (Z to A) и кликает на него"""
        select = Select(self.browser.find_element(By.TAG_NAME, "select"))
        select.select_by_value("za")

    def choice_a_z(self):
        """Метод выбирает в drop-down menu элемента Filter пункт Name (A to Z) и кликает на него"""
        select = Select(self.browser.find_element(By.TAG_NAME, "select"))
        select.select_by_value("az")

    def choice_price_lo_to_hi(self):
        """Метод выбирает в drop-down menu элемента Filter пункт Price (low to high) и кликает на него"""
        select = Select(self.browser.find_element(By.TAG_NAME, "select"))
        select.select_by_value("lohi")

    def choice_price_hi_to_lo(self):
        """Метод выбирает в drop-down menu элемента Filter пункт Price (high to low) и кликает на него"""
        select = Select(self.browser.find_element(By.TAG_NAME, "select"))
        select.select_by_value("hilo")

    def get_all_names(self):
        """Метод возвращает список со всеми наименованиями товаров со страницы Products"""
        all_names = list(self.browser.find_elements(*ALL_NAMES))
        list_all_names = [name.text for name in all_names]
        return list_all_names

    def get_all_desc(self):
        """Метод возвращает список со всеми описаниями товаров со страницы Products"""
        all_desc = list(self.browser.find_elements(*ALL_DESC))
        list_all_desc = [desc.text for desc in all_desc]
        return list_all_desc

    def get_all_prices(self):
        """Метод возвращает список со всеми ценами товаров (цена товара без знака $)
        со страницы Products"""
        all_prices = list(self.browser.find_elements(*ALL_PRICES))
        list_all_prices = [float(price.text[1:]) for price in all_prices]
        return list_all_prices

    def should_be_img_all_item(self):
        """Метод создает список со всеми фото товаров со страницы Products и
        сравнивает с эталонным списком фото"""
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

    def list_required_img(self):
        """Метод возвращает эталонный список со всеми фото товаров со страницы Products"""
        list_required_img = [
            "https://www.saucedemo.com/static/media/sauce-backpack-1200x1500.34e7aa42.jpg",
            "https://www.saucedemo.com/static/media/bike-light-1200x1500.a0c9caae.jpg",
            "https://www.saucedemo.com/static/media/bolt-shirt-1200x1500.c0dae290.jpg",
            "https://www.saucedemo.com/static/media/sauce-pullover-1200x1500.439fc934.jpg",
            "https://www.saucedemo.com/static/media/red-onesie-1200x1500.1b15e1fa.jpg",
            "https://www.saucedemo.com/static/media/red-tatt-1200x1500.e32b4ef9.jpg",
        ]
        return list_required_img

    def add_all_items(self):
        """Метод добавляет все товары со страницы Products в корзину"""
        add_cart = list(self.browser.find_elements(*BTN_ADD))
        for btn_add_cart in add_cart:
            btn_add_cart.click()

    def add_to_cart_backpack(self):
        """Метод кликает кнопку Add to cart товара Backpack (добавляет его в корзину)"""
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"
        ).click()

    def add_to_cart_bike_light(self):
        """Метод кликает кнопку Add to cart товара Bike Light (добавляет его в корзину)"""
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light"
        ).click()

    def add_to_cart_bolt_t_shirt(self):
        """Метод кликает кнопку Add to cart товара Bolt T-shirt (добавляет его в корзину)"""
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()

    def add_to_cart_fleece_jacket(self):
        """Метод кликает кнопку Add to cart товара Fleece Jacket (добавляет его в корзину)"""
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket"
        ).click()

    def add_to_cart_onesie(self):
        """Метод кликает кнопку Add to cart товара Onsie (добавляет его в корзину)"""
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"
        ).click()

    def add_to_cart_allthethings_t_shirt(self):
        """Метод кликает кнопку Add to cart товара T-shirt (Red) (добавляет его в корзину)"""
        self.browser.find_element(
            By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)"
        ).click()

    def add_to_cart_random(self):
        """Метод кликает кнопку Add to cart одного рандомно выбранного товара (добавляет его в корзину)"""
        all_names = list(self.browser.find_elements(*BTN_ADD))
        random_index = random.randrange(len(all_names))
        add_cart_button = self.browser.find_elements(*BTN_ADD)[random_index]
        add_cart_button.click()

    def btn_remove_is_present_random(self):
        """Метод проверяет наличие кнопки Remove на странице Products"""
        wait = WebDriverWait(self.browser, 20)
        btn_remove = wait.until(EC.element_to_be_clickable(BTN_REMOVE))
        assert self.element_is_present(*BTN_REMOVE)

    def btn_remove_click_random(self):
        """Метод дожидается появления кнопки Remove и кликает на нее на странице Products"""
        wait = WebDriverWait(self.browser, 20)
        btn_remove = wait.until(EC.element_to_be_clickable(BTN_REMOVE))
        btn_remove.click()

    def get_all_items_remove(self):
        """Метод возвращает список из списков наименований, описаний и цен товаров,
        добавленных в корзину со страницы Products"""
        all_names_remove = list(self.browser.find_elements(*ALL_NAMES_REMOVE))
        list_all_names_remove = [name.text for name in all_names_remove]

        all_desc_remove = list(self.browser.find_elements(*ALL_DESC_REMOVE))
        list_all_desc_remove = [desc.text for desc in all_desc_remove]

        all_prices_remove = list(self.browser.find_elements(*ALL_PRICES_REMOVE))
        list_all_prices_remove = [price.text for price in all_prices_remove]

        list_all_remove = [
            (
                list_all_names_remove[i],
                list_all_desc_remove[i],
                list_all_prices_remove[i],
            )
            for i in range(len(all_names_remove))
        ]
        return list_all_remove

    def all_items(self):
        """Метод возвращает список из списков наименований, описаний и цен всех товаров,
        со страницы Products"""
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

    def list_item(self):
        """Метод возвращает словарь из наименования, описания и цены товара Fleece Jacket,
        затем добавляет его в корзину"""
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

    def spell_check(self, id):
        """Метод проверяет орфографические ошибки в описании товара,
        значение товара передается по id"""
        checker = SpellChecker("en_US")
        desc = self.browser.find_element(
            By.XPATH, f"(//*[@class='inventory_item_desc'])[{id}]"
        )
        checker.set_text(desc.text)
        possible_error = [i.word for i in checker]
        assert possible_error == [], f"Possibly a typo: {possible_error}"

    def get_all_id(self):
        """Метод возвращает список из списков всех id товаров со страницы"""
        all_id = list(self.browser.find_elements(*ALL_ID))
        list_all_id = ["id=" + id.get_attribute("id")[5:6] for id in all_id]

        return list_all_id

    def add_btn_is_present(self):
        """Метод проверяет наличие кнопки Add to cart для товаров на странице Products"""
        assert self.element_is_present(*BTN_ADD), "Element is absent"
