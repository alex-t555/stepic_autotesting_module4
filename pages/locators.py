""" locators.py
"""

from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_invalid')


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, '#content_inner h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '#content_inner .product_main .price_color')
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button[type="submit"]')
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages>div:first-child strong')
    MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, '#messages>div:last-child strong')
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, '#messages strong')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')