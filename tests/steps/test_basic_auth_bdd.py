"""Basic Auth test step definitions"""

from pytest_bdd import given, when, then, scenarios
from pages.basic_auth import BasicAuth

scenarios('../features/basic_auth.feature')


@given('we are on the home page')
def home_page(driver):
    """Instantiate and return the home page object."""
    return BasicAuth(driver)

@when('we locate the basic auth button')
def locate_basic_auth_button(driver):
    """Navigate to the basic auth page."""
    home_page_obj = BasicAuth(driver)
    home_page_obj.navigate_to_basic_auth_page_and_login()

@then('we should be able to go to the basic auth page')
def go_to_basic_auth_page(driver):
    """Assert the current URL after navigating to basic auth page and loggin in."""
    home_page_obj = BasicAuth(driver)
    home_page_obj.load_basic_auth_page()
    assert home_page_obj.driver.current_url == home_page_obj.BASIC_AUTH_URL


@given('we are at the basic auth page')
def at_basic_auth_page(driver):
    """navigate to the basic auth page and login."""
    basic_auth_page = BasicAuth(driver)
    basic_auth_page.navigate_to_basic_auth_page_and_login()
    return basic_auth_page

@when('we enter the username and password to login')
def enter_credentials():
    """For Basic Auth, this step can be skipped as credentials are passed via URL."""
    pass

@then('we should login successfully and view a success message')
def verify_login_successfully(driver):
    """Assert the presence of the success message after login."""
    success_message = BasicAuth(driver).get_success_message_text()
    assert success_message == "Congratulations! You must have the proper credentials."
