"""Basic Auth test step definitions"""

from pytest_bdd import given, when, then, scenarios
from pages.basic_auth import BasicAuth

scenarios('..features/basic_auth.feature')

def test_basic_auth():
	"""to be run after all steps"""
	pass



@given('we are on the home page')
def load_the_home_page(driver):
	home_page = BasicAuth(driver)
	return home_page



@when('we locate the basic auth button')
def locate_basic_auth(load_the_home_page):
	load_the_home_page.find_basic_auth_button()



@then('we should be able to go to the basic auth page')
def load_basic_auth_page(load_the_home_page):
	load_the_home_page.navigate_to_basic_auth_page()
	assert load_the_home_page.driver.current_url == BasicAuth.URL




@given('we are at the basic auth page')
def basic_auth_page(driver):
	basic_auth_page = BasicAuth(driver)
	return basic_auth_page
	


@when('we enter the username ')
def enter_user_name(basic_auth_page):
	basic_auth_page.enter_username()


@when('we enter the username ')
def enter_password(basic_auth_page):
	basic_auth_page.enter_password()



@then('we should be able to login successfully')
def successfully_login(basic_auth_page):
	basic_auth_page.click_login()
	# assert that login is successful
