import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @pytest.mark.parametrize('station', [0])
    def test_make_order(self, main_page, order_page, station):
        main_page.get_main_page()
        order_page.click_accept_cookies()
        order_page.click_order_button_in_menu()
        # заполняю первую страницу формы
        order_page.fill_form_fields_first_page(station)
        order_page.click_next_button()
        assert order_page.get_text_from_rent_header() == 'Про аренду'
        # заполняю вторую страницу формы
        order_page.fill_form_fields_second_page()
        order_page.finalize_order()
