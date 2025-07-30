from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium import webdriver


class OrderPage(BasePage):

    def filling_of_field(self, field, keys):
        self.driver.find_element(*field).send_keys(keys)

    # def filling_first_form(self):
    #     self.driver