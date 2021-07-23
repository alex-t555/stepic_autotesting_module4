""" test_product_page.py
"""

from inspect import ArgInfo
from _pytest.mark import param
from _pytest.outcomes import xfail
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from .pages.product_page import ProductPage


links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", 
            marks=pytest.mark.xfail
        ),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser: WebDriver, link: str) -> None:
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_product_to_basket()