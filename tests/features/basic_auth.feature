Feature: We should be able to locate the basic auth page and login successfully
  
  Scenario: Moving to the basic auth page
    Given we are on the home page
	When we locate the basic auth button
	Then we should be able to go to the basic auth page


  Scenario: At the basic auth page
    Given we are at the basic auth page
	When we enter the username 
	When we enter the password
	Then we should be able to login successfully
