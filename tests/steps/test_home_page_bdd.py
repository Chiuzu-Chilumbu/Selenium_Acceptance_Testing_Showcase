"""Home page test step definitions"""

from pytest_bdd import scenario, given, when, then
from pages.home_page import HomePage

# Note: Removed GECKO_DRIVER and SERVICE constant because webdriver_manager
# will handle all underlying processes

scenario('../features/home_page.feature',
         'Home page is displayed when the application is launched')


def test_home_page():
    """To be run after all steps"""
    pass


@given('the base url of the web application')
def browser(driver):
    """Instantiate home page object"""
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
