# -- FILE: features/login.feature
Feature: Logging in

  Scenario: The User logs in
    Given The User is on the HTML Webpage
     When The User inputs <eid> in the employeeID bar
     And The User inputs <username> in the username bar
     And  The User inputs <password> in the inputPassword bar
     And The User clicks the submit button
     Then The title of the page is now <title>

