"""This conftest file keeps all the pytest fixtures"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # Initialize the ChromeDriver using webdriver_manager
    service = Service(ChromeDriverManager().install())

    # Configure ChromeOptions to run headlessly and with no sandbox for CI environment
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")  # This make Chromium reachable
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcomes limited resource problems
    chrome_options.add_argument("start-maximized")  # Starts Chrome maximized to avoid resolution issues
    chrome_options.add_argument("disable-infobars")  # Disables the "Chrome is being controlled by automated test software" infobar
    chrome_options.add_argument("--disable-extensions")  # Disables existing extensions
    chrome_options.add_argument("--disable-gpu")  # Applicable to windows os only

    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()
