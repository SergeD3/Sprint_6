import allure
import pytest
import data


class TestMainPage:

    @allure.title('При клике на вопрос появляется блок с ответом.')
    @allure.description('Проверяю, что при клике по вопросу появляется соответствующий ответ')
    @pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_faq_questions_answers(self, driver, num, main_page):
        main_page.get_main_page()
        main_page.scroll_to_question_and_click(num=num)
        text = main_page.get_answer_text(num=num)
        assert text == data.check_texts[num]
