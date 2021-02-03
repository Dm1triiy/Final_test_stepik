from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

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
              # return LoginPage(browser=self.browser, url=self.browser.current_url)
    #def should_be_add_basket(self):
      #  assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
