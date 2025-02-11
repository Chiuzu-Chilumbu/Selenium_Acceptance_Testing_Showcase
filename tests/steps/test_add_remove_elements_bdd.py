"""Add/Remove step definitions"""

from pytest_bdd import scenario, given, when, then
from pages.add_remove_elements import AddRemoveElementsPage

@scenario('../features/add_remove_elements.feature', 'Having moved to the Add/Remove elements web page, we should see and Add Element button')
def test_add_remove_elements():
    """BDD scenario for adding and removing elements"""
    pass


@given('the "Add/Remove" Elements page is loaded')
def add_remove_page(driver):
    """Instantiate Add/Remove Elements page object and load it"""
    page = AddRemoveElementsPage(driver)
    page.load()
    return page


@when('the "Add element" is clicked three times')
def click_add_element(add_remove_page):
    """Click 'Add Element' button three times"""
    for _ in range(3):
        add_remove_page.add_element()


@then('three "Delete" buttons should be displayed')
def verify_three_delete_buttons(add_remove_page):
    """verify three 'Delete ' buttons are displayed"""
    assert len(add_remove_page.get_delete_buttons()) == 3


@when('one "Delete" button is clicked')
def click_delete_button(add_remove_page):
    """click one 'Delete' button"""
    add_remove_page.delete_element()



@then('two "Delete" buttons should remain')
def verify_two_delete_buttons(add_remove_page):
    """verigy two 'Delete' buttons are displayed"""
    assert len(add_remove_page.get_delete_buttons()) == 2