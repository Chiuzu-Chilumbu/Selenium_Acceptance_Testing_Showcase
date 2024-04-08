"""unit test for the basic auth page object"""

from pages.basic_auth import BasicAuth

BASE_URL = "https://the-internet.herokuapp.com/basic_auth"


def test_basic_auth_initialization(driver):
    """Test that the BasicAuth page is initialized with the driver."""
    basic_auth_page = BasicAuth(driver)
    assert basic_auth_page.driver is driver


def test_basic_auth_navigation_and_login(driver):
    """Test navigation to the BasicAuth page."""
    basic_auth_page = BasicAuth(driver)
    basic_auth_page.load_basic_auth_page()
    assert driver.current_url == basic_auth_page.BASIC_AUTH_URL


def test_basic_auth_login(driver):
    """Test login on the BasicAuth page."""
    basic_auth_page = BasicAuth(driver)
    basic_auth_page.navigate_to_basic_auth_page_and_login()
    success_message = basic_auth_page.get_success_message_text()
    expected_message = "Congratulations! You must have the proper credentials."
    assert success_message == expected_message