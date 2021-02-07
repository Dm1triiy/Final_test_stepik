from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BTN_OPEN_BASKET = (By.CSS_SELECTOR, "span>a.btn.btn-default")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket - items")
    TEXT_BASKET_EMPTY = (By.XPATH, "//p[contains(text(), 'Ваша корзина пуста')]")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_formm")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    ADDED = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>.alertinner>strong")
    NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    ALERT_PRICE = (By.CSS_SELECTOR, ".alertinner>p>strong")
    PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main>.price_color")
    SUCCESS_MES = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")



