""" login_page.py
"""

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self) -> None:
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self) -> None:
        assert 'login' in self.browser.current_url, \
            'Current url is not login url.'

    def should_be_login_form(self) -> None:
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'Login form is not present.'

    def should_be_register_form(self) -> None:
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'Register form is not present.'