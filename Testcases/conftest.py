from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
        print('Launching Chrome browser.......')
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\sadguru\\Downloads\\geckodriver.exe")
        print('Launching firefox browser.......')
    elif browser == "edge":
        driver = webdriver.Edge(executable_path="C:\\Users\\sadguru\\Downloads\\msedgedriver.exe")
        print('launching edge browser..........')
    else:
        driver = webdriver.Chrome(executable_path="C:\\Users\\sadguru\\Downloads\\chromedriver.exe")

    driver.maximize_window()

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")