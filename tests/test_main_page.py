import pytest
import data

from pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_faq_questions_answers(self, driver, num):
        main_page = MainPage(driver)
        main_page.scroll_to_question_and_click(num=num)
        text = main_page.get_answer_text(num=num)
        assert text == data.check_texts[num]
