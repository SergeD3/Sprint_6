from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(driver, 10)

    def get_page(self, url, locator):
        self.driver.get(url)
        self.wait_element(locator)

    def find_element_by_locator(self, locator):
        self.wait_element(locator, by_visibility=True)
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.wait_element(locator, by_clickable=True)
        self.driver.find_element(*locator).click()

    def scroll_to_element(self, locator):
        element = self.find_element_by_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_element(locator, by_visibility=True)

    def add_text_to_element(self, locator, text):
        self.wait_element(locator, by_visibility=True)
        self.click_element(locator)
        self.find_element_by_locator(locator).clear()
        self.find_element_by_locator(locator).send_keys(text)

    def get_text_from_element(self, locator) -> str:
        self.wait_element(locator, by_visibility=True)
        text = self.driver.find_element(*locator).text
        return text
    
    def get_element_attr(self, locator) -> str:
        self.wait_element(locator, by_visibility=True)
        attribute = self.driver.find_element(*locator).get_attribute("value")
        return attribute

    @staticmethod
    def format_locators(locator, num) -> tuple:
        method, locator = locator
        locator = locator.format(num=num)
        return method, locator

    def wait_element(self, locator, by_visibility: bool = False, by_clickable: bool = False):
        if by_visibility is True and by_clickable is False:
            self.wait.until(expected_conditions.visibility_of_element_located(locator))
        elif by_visibility is False and by_clickable is True:
            self.wait.until(expected_conditions.element_to_be_clickable(locator))
        elif by_visibility is True and by_clickable is True:
            print('Ошибка: необходимо задавать только один способ ожидания.')
