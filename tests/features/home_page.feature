Feature: Confirm that the home page is the first page to be displayed when web page is opened

  Scenario: Home page is displayed when the application is launched
    Given the base url of the web application
	When the browser is directed to the base url
	Then the home page should be displayed