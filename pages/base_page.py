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

    @allure.step("Получить текст элемента")
    def get_text_of_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Заполнить поле")
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step("Проверить текущий URL")
    def check_current_url(self):
        return self.driver.current_url

    @allure.step("Переключить вкладку браузера")
    def switch_to_another_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Проверка отображения элемента")
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()