import allure
import pytest
from data import TestData
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestMainPageDropList:

    @allure.title("Проверка списка вопрос-ответ")
    @allure.description("Проверка, что при клике на вопрос, появляется соответсвующий ответ")
    @pytest.mark.parametrize('question_number, expected_answer', TestData.test_data_question_answer)
    def test_click_dropdown_list_answer_text_expected(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_element(MainPageLocators.faq_div)
        main_page.click_on_question(question_number)
        main_page.wait_visibility_of_answer(question_number)
        assert main_page.get_text_of_answer(question_number) == expected_answer
