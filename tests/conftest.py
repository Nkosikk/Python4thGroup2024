import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()

    elif browser.lower == 'edge':
        driver = webdriver.Edge()

    elif browser.lower == 'safari':
        driver = webdriver.Safari()

    else:
        driver = webdriver.Firefox()
        return driver


def pytest_addoption(parser):
    parser.addotion("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
