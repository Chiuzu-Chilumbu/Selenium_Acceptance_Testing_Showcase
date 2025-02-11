"""This conftest file keeps all the pytest fixtures"""

import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.add_remove_elements import AddRemoveElementsPage # Impo

@pytest.fixture
def driver():
    """
    Pytest fixture to initialize WebDriver with Chrome in both
    local and CI environments.
    """
    # Initialize ChromeDriver with a specific version (optional for CI stability)
    service = Service(ChromeDriverManager().install())

    # Configure ChromeOptions for headless mode in CI
    chrome_options = Options()
    if os.getenv("CI"):  # Only apply these options in CI environments
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

    # Create WebDriver instance
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def add_remove_page(driver):
    """Fixture to initialise and return the AddRemoveElements Page"""
    page = AddRemoveElementsPage(driver)
    page.load()
    return page