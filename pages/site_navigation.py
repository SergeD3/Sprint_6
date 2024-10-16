import allure

from locators.main_page_locators import MainPageLocators
from locators.navigation_locators import NavigationLocators
from pages.base_page import BasePage


class SiteNavigation(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = NavigationLocators()
        self.main_page_locators = MainPageLocators()

    @allure.step('Нажимаю на лого в меню')
    def click_logo(self, logo_type: str):
        if logo_type == 'samokat':
            self.click_element(self.locators.SAMOKAT_LOGO)
            self.basic_wait_element(self.main_page_locators.MENU_ORDER_BUTTON, by_visibility=True)
        elif logo_type == 'yandex':
            self.click_element(self.locators.YANDEX_LOGO)
            self.basic_switch_to_opened_window()
            self.basic_wait_element(self.locators.DZEN_BUTTON_FIND, by_visibility=True)

    @allure.step('Сравниваю текущий url с ожидаемым')
    def check_current_url(self, url):
        current_url = self.get_current_url()
        assert current_url == url

