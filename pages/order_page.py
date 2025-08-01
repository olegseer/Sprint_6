import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Заполнение первой половины формы")
    def filling_first_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.name)
        self.send_keys_to_input(OrderPageLocators.name, test_data[0])
        self.send_keys_to_input(OrderPageLocators.last_name, test_data[1])
        self.send_keys_to_input(OrderPageLocators.address, test_data[2])
        self.send_keys_to_input(OrderPageLocators.metro, test_data[3])
        self.click_on_element(OrderPageLocators.station_metro)
        self.send_keys_to_input(OrderPageLocators.phone, test_data[4])
        self.click_on_element(OrderPageLocators.next_btn)

    @allure.step("Заполнение второй половины формы")
    def filling_second_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.when_deliver)
        self.click_on_element(OrderPageLocators.when_deliver)
        self.send_keys_to_input(OrderPageLocators.when_deliver, test_data[5])
        self.click_on_element(test_data[6])
        self.click_on_element(OrderPageLocators.rent_time)
        self.click_on_element(test_data[7])
        self.send_keys_to_input(OrderPageLocators.comment, test_data[8])
        self.click_on_element(OrderPageLocators.make_order_btn)
        self.wait_visibility_of_element(OrderPageLocators.yes_btn)
        self.click_on_element(OrderPageLocators.yes_btn)

    @allure.step("Проверка отображения текста об успешном бронировании")
    def check_success_order_text(self):
        return self.driver.find_element(*OrderPageLocators.success_order_text).is_displayed()
