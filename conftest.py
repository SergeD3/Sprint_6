import pytest

from locators import main_page_locators
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def locators():
    locators = main_page_locators.Locators()
    return locators


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 10)
    return wait
