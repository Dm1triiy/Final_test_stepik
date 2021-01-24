import pytest
import time
from selenium import webdriver

def test_basket_find(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(2)
    input = browser.find_elements_by_css_selector("#add_to_basket_form>button")
    assert input , "Basket not found"