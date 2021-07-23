""" base_page.py
"""

import math
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, \
                                        NoAlertPresentException

class BasePage():

    def __init__(self, browser: WebDriver, url: str) -> None:
        self.browser = browser
        self.url = url
    
    def open(self) -> None:
        self.browser.get(self.url)

    def is_element_present(self, how: str, what: str, timeout: int=4) -> bool:
        try:
            WebDriverWait(driver=self.browser, timeout=timeout).until(
                lambda d: d.find_element(how, what)
            )
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self) -> None:
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print("Your code: {}".format(alert_text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")