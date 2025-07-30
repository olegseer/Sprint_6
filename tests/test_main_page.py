import pytest
from selenium import webdriver
from pages.main_page import MainPage
from data import TestData


class TestMainPageDropList:

    driver = None

    # @classmethod
    # def setup_class(cls):
    #     cls.driver = webdriver.Firefox()
    #     cls.driver.get(TestData.main_url)

    @pytest.mark.parametrize('question_number, expected_answer', TestData.test_data_question_answer)
    def test_click_dropdown_list_answer_text_expected(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_list()
        main_page.click_on_question(question_number)
        assert main_page.get_text_of_answer(question_number) == expected_answer

    # @classmethod
    # def teardown_class(cls):
    #     cls.driver.quit()
