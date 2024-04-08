Feature: We should be able to locate the basic auth page and login successfully
  
  Scenario: Moving to the basic auth page
    Given we are on the home page
	When we locate the basic auth button
	Then we should be able to go to the basic auth page


  Scenario: At the basic auth page
    Given we are at the basic auth page
	When we enter the username and password to login
	Then we should login successfully and view a success message
