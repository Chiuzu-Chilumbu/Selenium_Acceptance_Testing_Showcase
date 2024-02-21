"""Home Page Object"""


class HomePage:
    URL = "http://the-internet.herokuapp.com/"
    TITLE = "The Internet"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        """load web page"""
        self.driver.get(self.URL)

    def page_title(self):
        return self.driver.title
