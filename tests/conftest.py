"""This conftest file keeps all the pytest fixtures"""

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def driver():
	gecko_driver = 'drivers/geckodriver'
	service = Service(gecko_driver)
	driver = webdriver.Firefox(service=service)
	yield driver
	driver.quit()