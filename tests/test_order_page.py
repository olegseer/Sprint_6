from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


class TestOrderPage:

    def test_order_all_fields_success(self, driver):
        order_page = OrderPage(driver)
        order_page.click_cookie_button()
        order_page.wait_visibility_of_element(MainPageLocators.order_btn_top)
        order_page.click_on_element(MainPageLocators.order_btn_top)
        order_page.filling_first_form()
        order_page.filling_second_form()
        assert order_page.check_success_order()




