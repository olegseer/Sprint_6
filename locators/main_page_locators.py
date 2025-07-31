from selenium.webdriver.common.by import By


class MainPageLocators:
    cookie_btn = [By.ID, 'rcc-confirm-button']  # кнопка принятия куки
    yandex_btn = [By.XPATH, '//img[@alt="Yandex"]']  # кнопка Яндекс
    scooter_btn = [By.XPATH, '//img[@alt="Scooter"]']  # кнопка Самокат
    order_btn_top = [By.XPATH, '//button[@class="Button_Button__ra12g"]']  # кнопка заказа самоката сверху
    order_btn_bottom = [By.XPATH, '//button[contains(@class, "Button_Button__ra12g Button_Middle__1CSJM")]']  # кнопка заказа самоката внизу
    home_header = [By.XPATH, '//div[contains(@class, "Home_Header")]']  # заголовок на главной странице
    faq_div = [By.XPATH, '//div[@class="Home_FAQ__3uVm4"]']  # раздел с вопросами
    dzen_div = [By.XPATH, '//*[@id="YA_SEARCH_APP_CONTAINER_MicroRoot"]/div']
    questions = {1: [By.ID, 'accordion__heading-0'],  # вопросы
                 2: [By.ID, 'accordion__heading-1'],
                 3: [By.ID, 'accordion__heading-2'],
                 4: [By.ID, 'accordion__heading-3'],
                 5: [By.ID, 'accordion__heading-4'],
                 6: [By.ID, 'accordion__heading-5'],
                 7: [By.ID, 'accordion__heading-6'],
                 8: [By.ID, 'accordion__heading-7']}
    answers = {1: [By.XPATH, '//div[@id="accordion__panel-0"]'],  # ответы
               2: [By.XPATH, '//div[@id="accordion__panel-1"]'],
               3: [By.XPATH, '//div[@id="accordion__panel-2"]'],
               4: [By.XPATH, '//div[@id="accordion__panel-3"]'],
               5: [By.XPATH, '//div[@id="accordion__panel-4"]'],
               6: [By.XPATH, '//div[@id="accordion__panel-5"]'],
               7: [By.XPATH, '//div[@id="accordion__panel-6"]'],
               8: [By.XPATH, '//div[@id="accordion__panel-7"]']}
