from .base_page import BasePage
from .locators import MainPageLocators


class BasketPage(BasePage):

    def should_be_basket_empty(self):
        assert self.is_not_element_present(*MainPageLocators.BASKET_ITEM), "Basket is not empty"
        assert self.is_element_present(*MainPageLocators.TEXT_BASKET_EMPTY), "Basket is not empty"
