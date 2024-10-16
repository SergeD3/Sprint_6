import pytest

from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.site_navigation import SiteNavigation


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    return main_page


@pytest.fixture
def order_page(driver):
    ord_page = OrderPage(driver)
    return ord_page


@pytest.fixture
def navigation(driver):
    navigation = SiteNavigation(driver)
    return navigation

