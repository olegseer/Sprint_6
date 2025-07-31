import allure
from data import TestData
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestLogoTransfer:

    @allure.title("Проверка перехода на главную страницу Самоката по клику на лого Самоката")
    def test_logo_transfer_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_element(MainPageLocators.order_btn_top)
        main_page.click_on_element(MainPageLocators.order_btn_top)
        main_page.wait_visibility_of_element(MainPageLocators.scooter_btn)
        main_page.click_on_element(MainPageLocators.scooter_btn)
        main_page.wait_visibility_of_element(MainPageLocators.home_header)
        assert main_page.check_current_url() == TestData.main_url

    @allure.title("Проверка перехода на главную страницу Дзена по клику на лого Яндекса ")
    @allure.description("Переход осуществляется через редирект")
    def test_logo_transfer_to_dzen_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_element(MainPageLocators.yandex_btn)
        main_page.click_on_element(MainPageLocators.yandex_btn)
        main_page.switch_to_another_tab()
        main_page.wait_visibility_of_element(MainPageLocators.dzen_div)
        assert TestData.dzen_url in main_page.check_current_url(), 'Тест иногда падает из-за капчи'
