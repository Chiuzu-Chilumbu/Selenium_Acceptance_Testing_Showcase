"""unit test for the home page object"""

from pages.home_page import HomePage


def test_home_page_initialisation(driver):
    """This methods tests if the home page initialises as needed"""
    homepage = HomePage(driver)
    assert homepage.driver == driver


def test_home_page_load(driver):
    """This test loads the home page and checks if the current url matches the home page base url"""
    home_page = HomePage(driver)
    home_page.load()
    assert driver.current_url == HomePage.URL


def test_home_page_title(driver):
    """This test loads the home page and checks if the web page title in the home page matches the base url title"""
    home_page = HomePage(driver)
    home_page.load()
    assert home_page.page_title() == HomePage.TITLE
