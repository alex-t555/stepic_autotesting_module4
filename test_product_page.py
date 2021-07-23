""" test_product_page.py
"""

from selenium.webdriver.chrome.webdriver import WebDriver

from .pages.product_page import ProductPage


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


def test_guest_can_add_product_to_basket(browser: WebDriver) -> None:
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_product_to_basket()