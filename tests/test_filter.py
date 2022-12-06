import allure
from conf import link, list_username
import pytest
from pages.inventory_page import InventoryPage


@allure.feature("US_010.00 | Filter")
@allure.story("TC_010.00.01 | Filter > Проверка наличия фильтра на странице 'Products'")
@pytest.mark.parametrize("username", list_username)
def test_filter_is_present(browser):
    assert "inventory" in browser.current_url, "Wrong page"
    page = InventoryPage(browser, link)
    page.should_be_filter()


@allure.feature("US_010.00 | Filter")
@allure.story("TC_010.00.02 | Filter > Работа фильтра на странице 'Products' (Z-A).")
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param("problem_user", marks=pytest.mark.xfail(reason="problem_user")),
        "performance_glitch_user",
    ],
)
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
@pytest.mark.parametrize("username", list_username)
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
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param("problem_user", marks=pytest.mark.xfail(reason="problem_user")),
        "performance_glitch_user",
    ],
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
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param("problem_user", marks=pytest.mark.xfail(reason="problem_user")),
        "performance_glitch_user",
    ],
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
