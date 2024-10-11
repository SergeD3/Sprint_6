import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_element_with_wait(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def scroll_to_element_with_wait(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait.until(expected_conditions.visibility_of_element_located(locator))

    def add_text_to_element(self, locator, text):
        self.click_element_with_wait(locator)
        self.driver.find_element(*locator).send_keys(text)

    def get_text_from_element(self, locator) -> str:
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    @staticmethod
    def format_locators(locator, num) -> tuple:
        method, locator = locator
        locator = locator.fomat(num=num)
        return method, locator
