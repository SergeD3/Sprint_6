import allure
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import data


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()
        self.get_main_page()

    @allure.step('Открываю главную страницу MainPage')
    def get_main_page(self):
        self.get_page(data.URLS['main_page'], self.locators.MENU_ORDER_BUTTON)

    @allure.step('Кликаю на вопрос')
    def click_to_faq_question(self, locator):
        self.scroll_to_element_with_wait(self.locators.FAQ_LAST_QUESTION)
        self.click_element_with_wait(locator)

    @allure.step('Получаю текст ответа')
    def get_answer_text(self, num):
        locator = self.format_locators(self.locators.FAQ_ANSWER_TEMPLATE, num)
        return self.get_text_from_element(locator)

    @allure.step('Прокручиваю до конца страницы')
    def scroll_to_end_with_wait(self):
        self.scroll_to_element_with_wait(self.locators.FAQ_LAST_QUESTION)
        self.wait.until(expected_conditions.visibility_of_element_located(self.locators.FAQ_LAST_QUESTION))

    @allure.step('Прокручиваю до конца страницы и кликаю по вопросу.')
    def scroll_to_question_and_click(self, num):
        question_locator = self.format_locators(self.locators.FAQ_QUESTION_TEMPLATE, num)
        self.scroll_to_end_with_wait()
        self.click_to_faq_question(question_locator)
