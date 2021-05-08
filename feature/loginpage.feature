Feature: LoginPage Validation

#  @smoke
#  Scenario: Verify Login with Valid Credentials
#    Given User is on HomePage
#    When User clicks on the Sign In link
#    And User enters "shankubisai3333@gmail.com" as email
#    And User clicks Next Button
#    And User enters "shanku12345#" as password
#    And User clicks Sign In Button
#    Then Client Home Page is displayed




  @regression
  Scenario Outline: Verify Login with Invalid Credentials
    Given User is on HomePage
    When User clicks on the Sign In link
    And User enters "<email>" as email
    And User clicks Next Button
    And User enters "<password>" as password
    And User clicks Sign In Button
    Then error message "This account cannot be found. Please use a different account or sign up for a new account.." is displayed

    Examples: credentials
   | email         | password |
   | shankubisai4444@gmail.com | shanku12345#      |
   | shankubisai5555@gmail.com | shanku12345#      |



#
#    @smoke @sanity
#    Scenario: Verify login with existing email and password
#      Given User is on HomePage
#      When User fill the login details
#      Then Client Home Page is displayed



#this is the command to run all the testcases of the login page thas has the tag as sanity
#behave ./feature/loginpage.feature --no-capture --tags=sanity -f allure_behave.formatter:AllureFormatter -o allureReports


#command to exclude a file from running
#behave ./feature --exclude loginpage.feature --no-capture --tags=sanity -f allure_behave.formatter:AllureFormatter -o allureReports


#command to run all the features
#behave ./feature  --no-capture -f allure_behave.formatter:AllureFormatter -o allureReports


#command to run only the failed testcases
#behave ./feature -f rerun -o failedTestcases.feature --no-capture -f allure_behave.formatter:AllureFormatter -o allureReports











