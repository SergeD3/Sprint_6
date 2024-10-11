import allure

from base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Перехожу на страницу main')
    def get_main_page(self, locators):
        self.driver.get(locators.URLS['main_page'])

    @allure.step('Кликаю на вопрос')
    def click_to_faq_question(self, locator, locators, num):
        actual_question = self.format_locators(locator, num)
        self.scroll_to_element_with_wait(locators.FAQ_LAST_QUESTION)
        self.click_element_with_wait(actual_question)

    @allure.step('Получаю текст ответа')
    def get_answer_text(self, locator):
        return self.get_text_from_element(locator)
