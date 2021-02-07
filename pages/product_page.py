from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED), \
            "Success message is presented, but should not be"

    def button_basket(self):
        btn_basket = self.browser.find_element(*ProductPageLocators.BASKET)
        btn_basket.click()
        self.solve_quiz_and_get_code()

    def added_to_basket(self):
        name = self.browser.find_element(*ProductPageLocators.NAME)
        added = self.browser.find_element(*ProductPageLocators.ADDED)
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        alert_price = self.browser.find_element(*ProductPageLocators.ALERT_PRICE)
        assert name.text == added.text , "wrong book name"
        assert price.text == alert_price.text , "wrong price"

    def should_not_be_success_message_after_adding_product_to_basket(self):
        btn_basket = self.browser.find_element(*ProductPageLocators.BASKET)
        btn_basket.click()
        self.solve_quiz_and_get_code()
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MES), "Success message is presented, but should not be"
        time.sleep(0)

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MES), "Success message is presented, but should not be"

    def message_disappeared_after_adding_product_to_basket(self):
        btn_basket = self.browser.find_element(*ProductPageLocators.BASKET)
        btn_basket.click()
        self.solve_quiz_and_get_code()
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MES), "Success message is presented, but should not be"
