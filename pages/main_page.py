from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def click_cookie_button(self):
        self.driver.find_element(*MainPageLocators.cookie_btn).click()

    def scroll_to_list(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*MainPageLocators.faq_div))

    def click_on_question(self, question_number):
        self.driver.find_element(*MainPageLocators.questions[question_number]).click()

    def get_text_of_answer(self, question_number):
        return self.driver.find_element(*MainPageLocators.answers[question_number]).text

    def check_current_url(self):
        return self.driver.current_url

    def switch_to_another_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
