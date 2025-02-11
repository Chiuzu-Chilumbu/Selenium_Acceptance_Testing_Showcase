Feature: We should be able to add elements after clicking the add element button
  
  Scenario: Having moved to the Add/Remove elements web page, we should see and Add Element button
    Given the "Add/Remove" Elements page is loaded
    When the "Add element" is clicked three times
    Then three "Delete" buttons should be displayed
    When one "Delete" button is clicked 
    Then two "Delete" buttons should remain