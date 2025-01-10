Feature:  Empoyee Functionality

  Scenario: Search for new SSN
    Given : Navigate to Home page
    When  : Enter the valid user credentials
    When  : Click on Employee link
    When : Enter the new SSN number into Search box field
    And   : Click on Search button
    Then  : New result should not be displayed in the Search result

  Scenario: Search for Existing SSN
    Given : Navigate to Home page
    When  : Enter the valid user credentials
    When   : Click on Employee link
    When   : Enter the Existing SSN number into Search box field
    And   : Click on Search button
    Then  :  New result Employee result should be displayed in the Search result