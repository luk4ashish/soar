Feature:  Search Functionality

  Scenario: Search for new SSN
    Given : Navigate to Home page
    When  : Click on Employee link
    When : Enter the new SSN number into Search box field
    And   : Click on Search button
    Then  : Emloyee result should not be displayed in the Search result

#  Scenario: Search for Existing SSN
#    Given : Navigate to Home page
#    When  : Enter the valid user credentials
#    When   : Click on Employee link
#    When   : Enter the Existing SSN number into Search box field
#    And   : Click on Search button
#    Then  : Emloyee result should be displayed in the Search result
#
#
#  Scenario: Search for new Last 4 Digit of SSN and Last Name
#    Given : Navigate to Home page
#    When  : Enter the valid user credentials
#    When  : Click on Employee link
#    When  : Enter the new Last 4 Digit of SSN and Last Name into Search box field
#    And   : Click on Search button
#    Then  : Emloyee result should not be displayed in the Search result
#
#  Scenario: Search for Existing Last 4 Digit of SSN and Last Name
#    Given : Navigate to Home page
#    When  : Enter the valid user credentials
#    When  : Click on Employee link
#    When  : Enter the existing Last 4 Digit of SSN and Last Name into Search box field
#    And   : Click on Search button
#    Then  : Emloyee result should not be displayed in the Search result
#
#  Scenario: Search wihtout entering any LastName
#    Given : Navigate to Home page
#    When  : Enter the valid user credentials
#    When  : Click on Employee link
#    And   : Click on Search button
#    Then  : Emloyee result should not be displayed in the Search result
