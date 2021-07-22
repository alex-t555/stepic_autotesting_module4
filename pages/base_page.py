""" base_page.py
"""

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class BasePage():

    def __init__(self, browser: WebDriver, url: str):
        self.browser = browser
        self.url = url
    
    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how: str, what: str, timeout: int=4) -> bool:
        try:
            WebDriverWait(driver=self.browser, timeout=timeout).until(
                lambda d: d.find_element(how, what)
            )
        except TimeoutException:
            return False
        return True