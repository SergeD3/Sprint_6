import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @pytest.mark.parametrize('station', [0])
    def test_make_order(self, driver, station):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        order_page.click_order_button_in_menu()
        order_page.fill_form_fields(station)
        order_page.click_next_button()
        assert order_page.get_text_from_rent_header() == 'Про аренду'
