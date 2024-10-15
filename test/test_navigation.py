import allure
import pytest
import data


class TestNavigation:

    @pytest.mark.parametrize('logo_type, url', [
        ['samokat', data.URLS.get('main_page')],
        ['yandex', data.URLS.get('dzen_page')]
    ])
    @allure.title(f'Тестирование переходов по нажатию на логотипы: Самокат, Яндекс.')
    @allure.description('Проверяю, что при нажатии на логотип происходит редирект.')
    def test_navigation_logo(self, navigation, order_page, logo_type, url):
        order_page.get_order_page()
        navigation.click_logo(logo_type=logo_type)
        assert navigation.get_current_url() == url
