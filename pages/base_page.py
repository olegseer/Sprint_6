import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Нажатие на кнопку принятия куки")
    def click_cookie_button(self):
        self.driver.find_element(*MainPageLocators.cookie_btn).click()

    @allure.step("Клик на элемент")
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ожидание видимости элемента")
    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(locator))
