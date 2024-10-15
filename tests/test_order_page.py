import pytest


class TestOrderPage:

    @pytest.mark.parametrize('station, button, timeline, color', [
        [0, 'menu', 'past', 'black'],
        [1, 'main_page', 'future', 'grey']
    ])
    def test_make_order(self, main_page, order_page, station, button, timeline, color):
        main_page.get_main_page()
        order_page.click_accept_cookies()
        order_page.click_order_button_on_main_page(variant=button)
        # заполняю первую страницу формы
        order_page.fill_form_fields_first_page(station_index=station)
        order_page.click_next_button()
        assert order_page.get_text_from_rent_header() == 'Про аренду'
        # заполняю вторую страницу формы
        order_page.fill_form_fields_second_page(timeline=timeline, color=color)
        order_page.finalize_order()
        assert order_page.check_order_status_header()
