from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from locators.main_page_locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def click_cookie_button(self):
        self.driver.find_element(*MainPageLocators.cookie_btn).click()

    def scroll_to_list(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*MainPageLocators.faq_div))

    def click_on_question(self, question_number):
        self.driver.find_element(*MainPageLocators.questions[question_number]).click()

    def get_text_of_answer(self, question_number):
        return self.driver.find_element(*MainPageLocators.answers[question_number]).text

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(locator))

    def check_current_url(self):
        return self.driver.current_url

    def switch_to_another_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
