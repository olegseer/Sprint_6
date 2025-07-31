from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def click_on_question(self, question_number):
        self.driver.find_element(*MainPageLocators.questions[question_number]).click()

    def wait_visibility_of_answer(self, question_number):
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(MainPageLocators.answers[question_number]))

    def get_text_of_answer(self, question_number):
        return self.driver.find_element(*MainPageLocators.answers[question_number]).text

    def check_current_url(self):
        return self.driver.current_url

    def switch_to_another_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
