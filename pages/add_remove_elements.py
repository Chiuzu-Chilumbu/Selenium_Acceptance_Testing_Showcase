""" Add/Remove Elements """
from selenium.webdriver.common.by import By

class AddRemoveElementsPage:
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"
    ADD_BUTTON = (By.XPATH, "//button[text()='Add Element']")
    DELETE_BUTTONS = (By.CLASS_NAME, "added-manually")

    def __init__(self, driver):
        self.driver = driver


    def load(self):
        """Load the Add/Remove Elements page"""
        self.driver.get(self.URL)

    
    def add_element(self):
        """Click the 'Add Element Button' button"""
        self.driver.find_element(*self.ADD_BUTTON).click()

    
    def get_delete_buttons(self):
        """Return all 'Delete' buttons"""
        return self.driver.find_elements(*self.DELETE_BUTTONS)
    
    def delete_element(self):
        """Click the first 'Delete' button, if any"""
        delete_buttons = self.get_delete_buttons()
        if delete_buttons:
            delete_buttons[0].click()