from selenium.webdriver.common.by import By


class MainPageLocators:
    # элементы меню
    MENU_ORDER_BUTTON = (
        By.XPATH,
        '//div[starts-with(@class, "Header")]/button[contains(text(), "Заказать")]'
    )  # получаю кнопку Заказать в меню

    # элементы блока Вопросы о важном
    FAQ = (By.CSS_SELECTOR, '.accordion')  # основной блок с вопросами-ответами

    FAQ_QUESTION_TEMPLATE = (
        By.XPATH,
        '//div[@id="accordion__heading-{num}" and @role="button"]'
    )  # шаблон селектора для получения вопроса под номером №

    FAQ_ANSWER_TEMPLATE = (
        By.XPATH,
        '//div[@id="accordion__panel-{num}"]/p'
    )  # шаблон селектора для получения ответа под номером №

    FAQ_LAST_QUESTION = (
        By.XPATH,
        '//div[@id="accordion__heading-7" and @role="button"]'
    )  # селектор последнего вопроса на странице
