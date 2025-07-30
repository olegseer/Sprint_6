import pytest
from selenium import webdriver
from pages.main_page import MainPage
from data import TestData


class TestMainPageDropList:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')

    @pytest.mark.parametrize('question_number, expected_answer', TestData.test_data_question_answer)
    def test_check_text_in_answer(self, question_number, expected_answer):
        main_page = MainPage(self.driver)
        #main_page.click_cookie_button()
        main_page.scroll_to_list()
        main_page.click_on_element(question_number)
        assert main_page.get_text_of_element(question_number) == expected_answer

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


