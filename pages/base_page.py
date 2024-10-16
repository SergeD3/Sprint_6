import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Открываю страницу.')
    def get_page(self, url, locator):
        self.driver.get(url)
        self.basic_wait_element(locator)

    @allure.step('Переключаюсь на вторую открытую вкладку.')
    def basic_switch_to_opened_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получаю текущий url.')
    def get_current_url(self) -> str:
        return self.driver.current_url

    @allure.step('Поиск элемента по локатору.')
    def find_element_by_locator(self, locator):
        self.basic_wait_element(locator, by_visibility=True)
        return self.driver.find_element(*locator)

    @allure.step('Кликаю по элементу.')
    def click_element(self, locator):
        self.basic_wait_element(locator, by_clickable=True)
        self.driver.find_element(*locator).click()

    @allure.step('Прокручиваю страницу до элемента.')
    def scroll_to_element(self, locator):
        element = self.find_element_by_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.basic_wait_element(locator, by_visibility=True)

    @allure.step('Ввожу значение в поле.')
    def add_text_to_element(self, locator, text):
        self.basic_wait_element(locator, by_visibility=True)
        self.click_element(locator)
        self.find_element_by_locator(locator).clear()
        self.find_element_by_locator(locator).send_keys(text)

    @allure.step('Получаю текст элемента.')
    def get_text_from_element(self, locator) -> str:
        self.basic_wait_element(locator, by_visibility=True)
        text = self.driver.find_element(*locator).text
        return text

    @allure.step('Получаю значение(value) элемента.')
    def get_element_value(self, locator) -> str:
        self.basic_wait_element(locator, by_visibility=True)
        attribute = self.driver.find_element(*locator).get_attribute("value")
        return attribute

    @staticmethod
    @allure.step('Изменяю локатор.')
    def format_locators(locator, num) -> tuple:
        method, locator = locator
        locator = locator.format(num=num)
        return method, locator

    @allure.step('Сравниваю значение в поле с ожидаемым значением.')
    def check_element_text(self, locator, text) -> bool:
        element_text = self.get_text_from_element(locator)
        assert element_text == text

    @allure.step('Ожидаю отображение элемента или его кликабельность.')
    def basic_wait_element(self, locator, by_visibility: bool = False, by_clickable: bool = False):
        if by_visibility is True and by_clickable is False:
            self.wait.until(expected_conditions.visibility_of_element_located(locator))
        elif by_visibility is False and by_clickable is True:
            self.wait.until(expected_conditions.element_to_be_clickable(locator))
        elif by_visibility is True and by_clickable is True:
            print('Ошибка: необходимо задавать только один способ ожидания.')

    @allure.step('Ожидаю прекращение отображения элемента на странице.')
    def basic_wait_until_not_visibility(self, locator):
        self.wait.until_not(expected_conditions.visibility_of_element_located(locator))


