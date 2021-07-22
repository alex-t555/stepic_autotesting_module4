""" test_main_page.py
"""

from selenium.webdriver.chrome.webdriver import WebDriver


def test_guest_can_go_to_login_page(browser: WebDriver) -> None:
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    browser.find_element_by_css_selector('#login_link').click()