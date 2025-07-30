from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from data import TestData


class TestLogoTransfer:

    driver = None

    def test_logo_transfer_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_element(MainPageLocators.order_btn_top)
        main_page.click_on_element(MainPageLocators.order_btn_top)
        main_page.wait_visibility_of_element(MainPageLocators.scooter_btn)
        main_page.click_on_element(MainPageLocators.scooter_btn)
        main_page.wait_visibility_of_element(MainPageLocators.home_header)
        assert main_page.check_current_url() == TestData.main_url

    def test_logo_transfer_to_dzen_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_element(MainPageLocators.yandex_btn)
        main_page.click_on_element(MainPageLocators.yandex_btn)
        main_page.switch_to_another_tab()
        main_page.wait_visibility_of_element(MainPageLocators.dzen_div)
        assert main_page.check_current_url() == TestData.dzen_url
