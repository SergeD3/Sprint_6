import time
import pytest

from pages.main_page import MainPage
from selenium.webdriver.support import expected_conditions


class TestMainPage:

    def test_dropdown_list_element_zero(self, driver, locators, wait):
        main_page = MainPage(driver)
        main_page.get_main_page()

        # скроллинг до блока FAQ

        # кликаю на элемент, чтобы получить текст и сравнить его с проверочным


