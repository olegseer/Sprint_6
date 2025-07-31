from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class OrderPage(BasePage):

    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    def filling_first_form(self, test_data):
        self.send_keys_to_input(OrderPageLocators.name, test_data[0])
        self.send_keys_to_input(OrderPageLocators.last_name, test_data[1])
        self.send_keys_to_input(OrderPageLocators.address, test_data[2])
        self.send_keys_to_input(OrderPageLocators.metro, test_data[3])
        self.click_on_element(OrderPageLocators.station_metro)
        self.send_keys_to_input(OrderPageLocators.phone, test_data[4])
        self.wait_element_stay_clickable(OrderPageLocators.next_btn)
        self.click_on_element(OrderPageLocators.next_btn)

    def filling_second_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.make_order_btn)
        self.click_on_element(OrderPageLocators.when_deliver)
        self.send_keys_to_input(OrderPageLocators.when_deliver, test_data[5])
        self.click_on_element(OrderPageLocators.grey_scooter)
        self.click_on_element(OrderPageLocators.rent_time)
        self.click_on_element(OrderPageLocators.rent_time_option)
        self.send_keys_to_input(OrderPageLocators.comment, test_data[6])
        self.click_on_element(OrderPageLocators.make_order_btn)
        self.wait_visibility_of_element(OrderPageLocators.yes_btn)
        self.click_on_element(OrderPageLocators.yes_btn)

    def check_success_order(self):
        return self.driver.find_element(*OrderPageLocators.success_order_text).is_displayed()
