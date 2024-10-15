import allure
import pytest
import data

from pages.main_page import MainPage


class TestMainPage:

    @allure.description('Проверяю, что при клике по вопросу появляется соответствующий ответ')
    @pytest.mark.parametrize('num', [0, 1])
    def test_faq_questions_answers(self, driver, num, main_page):
        main_page.get_main_page()
        main_page.scroll_to_question_and_click(num=num)
        text = main_page.get_answer_text(num=num)
        assert text == data.check_texts[num]
