"""Basic Auth Page"""
from pages.home_page import HomePage

class BasicAuth(HomePage):
	

	def __init__(self, driver):
		super().__init__(driver)

	def load_home_page(self):
		raise NotImplementedError
	
	def find_basic_auth_button(self):
		raise NotImplementedError

	def navigate_to_basic_auth_page(self):
		raise NotImplementedError
	

	def enter_username(self):
		raise NotImplementedError
	

	def enter_password(self):
		raise NotImplementedError
	

	def click_login(self):
		raise NotImplementedError