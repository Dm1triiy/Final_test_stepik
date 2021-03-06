from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.driver = None

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "not login in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form missing"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form missing"

    def register_new_user(self, email, password):
        reg_form = self.browser.find_element(*LoginPageLocators.REG_FORM_EMAIL)
        pas_form1 = self.browser.find_element(*LoginPageLocators.REG_FORM_PASS)
        pas_form2 = self.browser.find_element(*LoginPageLocators.REG_FORM_PASS_REP)
        reg_but = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_form.send_keys(email)
        pas_form1.send_keys(password)
        pas_form2.send_keys(password)
        reg_but.click()
