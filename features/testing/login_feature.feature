# Created by  at 12/09/24
Feature: Google search page testing
  # Enter feature description here

  Scenario Outline: TC_01||login to application and test the home page
    Given Open application and enter <username> with <password>
    When user clicks on login button
    Examples:
      | username | password |
      | testuser | Tanga321#|

   Scenario: TC_02||Verify the error message for invalid usnername or password
     Given Open application and enter invalid username with password
     When user clicks on login button
     Then Verify the use is not able to login