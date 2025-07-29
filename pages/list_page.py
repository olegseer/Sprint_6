from main_page import MainPageScooter
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestList:

    def test_list(self):
        driver = webdriver.Firefox()
        driver.get('https://qa-scooter.praktikum-services.ru/')
        driver.find_element(*MainPageScooter.cookie_btn).click()
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*MainPageScooter.order_btn_bottom))
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageScooter.question_1))
        driver.find_element(*MainPageScooter.question_1).click()
        assert driver.find_element(*MainPageScooter.answer_1).text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        driver.quit()
