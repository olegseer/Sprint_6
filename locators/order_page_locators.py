from selenium.webdriver.common.by import By


class OrderPageLocators:
    name = [By.XPATH, '//input[@placeholder="* Имя"]']  # поле Имя
    last_name = [By.XPATH, '//input[@placeholder="* Фамилия"]']  # поле Фамилия
    address = [By.XPATH, '//input[contains(@placeholder, "* Адрес")]']  # поле Адрес
    metro = [By.XPATH, '//input[contains(@placeholder, "* Станция")]']  # поле Станция метро
    phone = [By.XPATH, '//input[contains(@placeholder, "* Телефон")]']  # поле Телефон
    when_deliver = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']  # поле Когда привезти самокат
    rent_time = [By.XPATH, '//input[@placeholder="* Срок аренды"]']  # поле Срок аренды
    black_scooter = [By.ID, 'black']  # выбор черного самоката
    grey_scooter = [By.ID, 'grey']  # выбор серого самоката
    comment = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]']  # поле Комментарий для курьера
    next_btn = [By.XPATH, '//button[text()="Далее"]']  # кнопка Далее
    back_btn = [By.XPATH, '//button[text()="Назад"]']  # кнопка Назад
    make_order_btn = [By.XPATH, '//button[text()="Заказать"]']  # кнопка Заказать
    yes_btn = [By.XPATH, '//button[text()="Да"]']  # кнопка Да
    no_btn = [By.XPATH, '//button[text()="Нет"]']  # кнопка Нет
    watch_status_btn = [By.XPATH, '//button[text()="Посмотреть статус"]']  # кнопка Посмотреть статус

