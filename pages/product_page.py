""" product_page.py
"""

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self) -> None:
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()
        self.should_be_success_message_after_adding_product_to_basket()
        message_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        message_product_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_PRICE).text
        assert message_product_name == product_name, \
            'Product name is not correct in the success message after add product to basket.'
        assert message_product_price == product_price, \
            'Product price is not correct in the success message after add product to basket.'


    def should_be_success_message_after_adding_product_to_basket(self) -> None:
        self.should_be_success_message()
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_NAME), \
            'Product name is not present in the success message after add product to basket.'
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_PRICE), \
            'Product price is not present in the success message after add product to basket.'


    def should_be_success_message(self) -> None:
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES), \
            'Success message is not present.'


    def should_not_be_success_message(self) -> None:
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), \
            'Success message is present, but should not be.'


    def should_disappeared_success_message(self) -> None:
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), \
            'Success message is not disappeared.'