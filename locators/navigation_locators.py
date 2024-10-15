from selenium.webdriver.common.by import By


class NavigationLocators:

    SAMOKAT_LOGO = (By.XPATH, '//a[contains(@class, "Header_LogoScooter")]')  # получаю логотип Самоката
    YANDEX_LOGO = (By.XPATH, '//a[contains(@class, "Header_LogoYandex")]')  # получаю логотип Яндекса
    DZEN_BUTTON_FIND = (By.XPATH, '//button[contains(text(), "Найти")]')  # получаю кнопку Найти на странице Дзена
