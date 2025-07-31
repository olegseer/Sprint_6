from selenium.webdriver.common.by import By


class OrderPageLocators:
    name = [By.XPATH, '//input[@placeholder="* Имя"]']  # поле Имя
    last_name = [By.XPATH, '//input[@placeholder="* Фамилия"]']  # поле Фамилия
    address = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']  # поле Адрес
    metro = [By.XPATH, '//input[@placeholder="* Станция метро"]']  # поле Станция метро
    station_metro = [By.XPATH, '//li[@class="select-search__row"]']
    phone = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]']  # поле Телефон
    when_deliver = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']  # поле Когда привезти самокат
    rent_time = [By.XPATH, '//div[text()="* Срок аренды"]']  # поле Срок аренды
    rent_time_option = [By.XPATH, '//div[text()="сутки"]']
    black_scooter = [By.ID, 'black']  # выбор черного самоката
    grey_scooter = [By.ID, 'grey']  # выбор серого самоката
    comment = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]']  # поле Комментарий для курьера
    next_btn = [By.XPATH, '//button[text()="Далее"]']  # кнопка Далее
    back_btn = [By.XPATH, '//button[text()="Назад"]']  # кнопка Назад
    make_order_btn = [By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]']  # кнопка Заказать
    yes_btn = [By.XPATH, '//button[text()="Да"]']  # кнопка Да
    no_btn = [By.XPATH, '//button[text()="Нет"]']  # кнопка Нет
    watch_status_btn = [By.XPATH, '//button[text()="Посмотреть статус"]']  # кнопка Посмотреть статус
    success_order_text = [By.XPATH, '//div[text()="Заказ оформлен"]']  # текст успешного оформления заказа

