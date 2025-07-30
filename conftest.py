import pytest
from selenium import webdriver
from data import TestData


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(TestData.main_url)
    yield driver
    driver.quit()
