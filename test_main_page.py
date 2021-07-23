""" test_main_page.py
"""

from selenium.webdriver.chrome.webdriver import WebDriver

from .pages.main_page import MainPage
from .pages.login_page import LoginPage


link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser: WebDriver) -> None:
    page = MainPage(browser=browser, url=link)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser=browser, url=browser.current_url)
    page.should_be_login_page()


def test_guest_should_see_login_link(browser: WebDriver) -> None:
    page = MainPage(browser=browser, url=link)
    page.open()
    page.should_be_login_link()