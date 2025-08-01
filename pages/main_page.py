import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Ожидание загрузки кнопки заказа вверху страницы")
    def wait_visibility_of_order_btn_top(self):
        self.wait_visibility_of_element(MainPageLocators.order_btn_top)

    @allure.step("Клик на кнопку заказа вверху страницы")
    def click_on_order_btn_top(self):
        self.click_on_element(MainPageLocators.order_btn_top)

    @allure.step("Ожидание загрузки кнопки Самокат в логотипе")
    def wait_visibility_of_scooter_btn(self):
        self.wait_visibility_of_element(MainPageLocators.scooter_btn)

    @allure.step("Клик на кнопку Самокат в логотипе")
    def click_on_scooter_btn(self):
        self.click_on_element(MainPageLocators.scooter_btn)

    @allure.step("Ожидание загрузки заголовка на главной странице")
    def wait_visibility_of_home_header(self):
        self.wait_visibility_of_element(MainPageLocators.home_header)

    @allure.step("Ожидание загрузки кнопки Яндекс в логотипе")
    def wait_visibility_of_yandex_btn(self):
        self.wait_visibility_of_element(MainPageLocators.yandex_btn)

    @allure.step("Клик на кнопку Яндекс в логотипе")
    def click_on_yandex_btn(self):
        self.click_on_element(MainPageLocators.yandex_btn)

    @allure.step("Ожидание загрузки блока на странице Дзен")
    def wait_visibility_of_dzen(self):
        self.wait_visibility_of_element(MainPageLocators.dzen_div)

    @allure.step("Скролл до раздела вопрос-ответ")
    def scroll_to_drop_list(self):
        self.scroll_to_element(MainPageLocators.faq_div)

    @allure.step("Клик на вопрос из списка")
    def click_on_question(self, question_number):
        self.click_on_element(MainPageLocators.questions[question_number])

    @allure.step("Ожидание видимости ответа")
    def wait_visibility_of_answer(self, question_number):
        self.wait_visibility_of_element(MainPageLocators.answers[question_number])

    @allure.step("Получить текст ответа")
    def get_text_of_answer(self, question_number):
        return self.get_text_of_element(MainPageLocators.answers[question_number])


