"""Home page test steps"""

from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from pages.home_page import HomePage


GECKO_DRIVER = '/drivers/geckodriver'
SERVICE = Service(GECKO_DRIVER)


scenario('../features/home_page.feature',
         'Home page is displayed when the application is launched')
def test_home_page():
    pass

@given('the base url of the web application')
def browser():
    """Instantiate home page object"""
    driver = webdriver.Firefox(service=SERVICE)
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