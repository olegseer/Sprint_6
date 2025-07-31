import pytest

from data import TestData
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


class TestOrderPage:

    @pytest.mark.parametrize('button, test_data', [[MainPageLocators.order_btn_top, TestData.test_data_user_1],
                                                   [MainPageLocators.order_btn_bottom, TestData.test_data_user_2]])
    def test_order_all_fields_success(self, driver, button, test_data):
        order_page = OrderPage(driver)
        order_page.click_cookie_button()
        order_page.scroll_to_element(button)
        order_page.wait_visibility_of_element(button)
        order_page.click_on_element(button)
        order_page.filling_first_form(test_data)
        order_page.filling_second_form(test_data)
        assert order_page.check_success_order()

