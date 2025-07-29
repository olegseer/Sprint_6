from selenium import webdriver
from selenium.webdriver.common.by import By


class MainPageScooter:
    cookie_btn = [By.ID, 'rcc-confirm-button']  # кнопка принятия куки
    yandex_btn = [By.XPATH, '//img[@alt="Yandex"]']  # кнопка Яндекс
    scooter_btn = [By.XPATH, '//img[@alt="Scooter"]']  # кнопка Самокат
    order_btn_top = []
    order_btn_bottom = [By.XPATH, '//button[contains(@class, "Button_Button__ra12g Button_Middle__1CSJM")]']  # кнопка заказа самоката внизу
    question_1 = [By.ID, 'accordion__heading-0']  # кнопка выпадающего списка
    answer_1 = [By.XPATH, '//div[@id="accordion__panel-0"]/p']  # ответ на 1ый вопрос
    question_2 = [By.ID, 'accordion__heading-1']
    answer_2 = [By.XPATH, '//div[@id="accordion__panel-1"]/p']
    title_3 = [By.ID, '//div[@id="accordion__heading-2"]']
    content_3 = [By.ID, '//div[@id="accordion__panel-2"]/p']
    title_4 = [By.ID, '//div[@id="accordion__heading-3"]']
    content_4 = [By.ID, '//div[@id="accordion__panel-3"]/p']
    title_5 = [By.ID, '//div[@id="accordion__heading-4"]']
    content_5 = [By.ID, '//div[@id="accordion__panel-4"]/p']
    title_6 = [By.ID, '//div[@id="accordion__heading-5"]']
    content_6 = [By.ID, '//div[@id="accordion__panel-5"]/p']
    title_7 = [By.ID, '//div[@id="accordion__heading-6"]']
    content_7 = [By.ID, '//div[@id="accordion__panel-6"]/p']
    title_8 = [By.ID, '//div[@id="accordion__heading-7"]']
    content_8 = [By.ID, '//div[@id="accordion__panel-7"]/p']

    def __init__(self, driver):
        self.driver = driver

    def click_cookie_button(self):
        self.driver.find_element(*self.cookie_btn).click()

    def click_question_1(self):
        self.driver.find_element(*self.question_1).click()

    def get_answer_1_text(self):
        return self.driver.find_element(*self.answer_1).text

    def click_question_2(self):
        self.driver.find_element(*self.question_2).click()

    def get_answer_2_text(self):
        return self.driver.find_element(*self.answer_2).text

    def scroll_to_list(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.order_btn_bottom))


class TestList:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_check_text_in_answer_1(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPageScooter(self.driver)
        main_page.click_cookie_button()
        main_page.scroll_to_list()
        main_page.click_question_1()
        assert main_page.get_answer_1_text() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    def test_check_text_in_answer_2(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPageScooter(self.driver)
        main_page.click_cookie_button()
        main_page.scroll_to_list()
        main_page.click_question_2()
        assert main_page.get_answer_2_text() == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
