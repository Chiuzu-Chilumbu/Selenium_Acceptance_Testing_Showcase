"""Home Page"""


class HomePage:
    URL = "https://the-internet.herokuapp.com/"
    TITLE = "The Internet"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        """load home page"""
        self.driver.get(self.URL)

    def page_title(self):
        """obteain page title"""
        return self.driver.title
