"""Basic Auth Page"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage

class BasicAuth(HomePage):
    """Basic authentication page"""
    USERNAME = 'admin'
    PASSWORD = 'admin'
    BASIC_AUTH_URL = 'https://the-internet.herokuapp.com/basic_auth' 

    def __init__(self, driver):
        super().__init__(driver)

    def load_home_page(self):
        """Load the home page."""
        self.driver.get(self.load_home_page())
        
    def load_basic_auth_page(self):
        """Load the home page."""
        self.driver.get(self.BASIC_AUTH_URL)

    def find_basic_auth_button(self):
        """Find the Basic Auth button on the home page."""
        # Replace with the actual locator for the Basic Auth button on your home page.
        return self.driver.find_element(By.LINK_TEXT, "Basic Auth")

    def navigate_to_basic_auth_page_and_login(self):
        """Navigate to the Basic Auth page and handle the auth dialog."""
        self.driver.get(self.formulate_basic_auth_url(self.USERNAME, self.PASSWORD))

    def formulate_basic_auth_url(self, username, password):
        """Return the URL with embedded credentials."""
        protocol, uri = self.BASIC_AUTH_URL.split("://")
        return f"{protocol}://{username}:{password}@{uri}"

    def click_login(self):
        """Basic Auth doesn't require login button click."""
        pass

    def get_success_message_text(self):
        """Get the success message text after logging in."""
        success_message_locator = (By.TAG_NAME, "p")
        success_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(success_message_locator)
        )
        return success_message.text
