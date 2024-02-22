"""Home page test steps"""

from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage

# Note: Removed GECKO_DRIVER and SERVICE constant since webdriver_manager
# will handle it

scenario('../features/home_page.feature',
         'Home page is displayed when the application is launched')


def test_home_page():
    pass


@given('the base url of the web application')
def browser():
    """Instantiate home page object"""
    # Use webdriver_manager to handle ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    home_page = HomePage(driver)
    return home_page


@when('the browser is directed to the base url')
def open_base_url(browser):
    """Open home page by loading browser"""
    browser.load()

@then('the home page should be displayed')
def home_page_displayed(browser):
    """Assert Home page title matches title on browser"""
    assert browser.page_title() == HomePage.TITLE
