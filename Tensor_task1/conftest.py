# import pytest
# from selenium import webdriver
#
# @pytest.fixture
# def browser():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get("https://saby.ru/")
    driver.wait = WebDriverWait(driver, 15)
    yield driver
    driver.quit()