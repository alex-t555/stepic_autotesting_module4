""" conftest.py
"""

from typing import Generator
import pytest
from _pytest.config.argparsing import Parser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


def pytest_addoption(parser: Parser) -> None:
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='en', help='Choose language: en, ru, es, fr, ...')


@pytest.fixture(scope='function')
def browser(request: pytest.FixtureRequest) -> Generator[WebDriver, None, None]:
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        _browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        _browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield _browser
    _browser.quit()