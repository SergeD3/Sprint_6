import pytest

from locators import main_page_locators
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 10)
    return wait


@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    return main_page


@pytest.fixture
def order_page(driver):
    ord_page = OrderPage(driver)
    return ord_page

