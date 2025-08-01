import allure
from curl import Urls
from pages.main_page import MainPage


class TestLogoTransfer:

    @allure.title("Проверка перехода на главную страницу Самоката по клику на лого Самоката")
    def test_logo_transfer_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_order_btn_top()
        main_page.click_on_order_btn_top()
        main_page.wait_visibility_of_scooter_btn()
        main_page.click_on_scooter_btn()
        main_page.wait_visibility_of_home_header()
        assert main_page.check_current_url() == Urls.main_url

    @allure.title("Проверка перехода на главную страницу Дзена по клику на лого Яндекса ")
    @allure.description("Переход осуществляется через редирект")
    def test_logo_transfer_to_dzen_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_yandex_btn()
        main_page.click_on_yandex_btn()
        main_page.switch_to_another_tab()
        main_page.wait_visibility_of_dzen()
        assert Urls.dzen_url in main_page.check_current_url(), 'Тест иногда падает из-за капчи'
