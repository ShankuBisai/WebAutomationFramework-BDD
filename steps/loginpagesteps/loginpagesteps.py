import time

from base.webdriverfactory import WebDriverFactory
from pages.actions.homepage.homepage import HomePage
from behave import given,when,then
from utilities.teststatus import TestStatus

@given('User is on HomePage')
def userGoToURL(context):
    # wb = WebDriverFactory("chrome")
    # context.driver = wb.getWebDriverInstance()
    pass



@when('User clicks on the Sign In link')
def userSignInClick(context):
    context.hp = HomePage(context.driver)
    context.lp=context.hp.clickSignInLink()



@when('User enters "{email}" as email')
def userEnterEmail(context,email):
    context.lp.enterEmail(email)



@when('User clicks Next Button')
def userClickNextButton(context):
    context.lp.clickNextButton()




@when('User enters "{password}" as password')
def userEntersPassword(context,password):
    context.lp.enterPassword(password)
    time.sleep(4)




@when('User clicks Sign In Button')
def userClickSignIn(context):
    context.chp=context.lp.clickSignInButton()
    time.sleep(5)




@then('Client Home Page is displayed')
def userClientHomePage(context):
    clientHomePageTitle=context.chp.verifyClientHomePageTitle()
    result=bool(clientHomePageTitle == "Zoho Home")
    context.ts = TestStatus(context.driver)
    context.ts.mark("userClientHomePage", result, "ClientHomePage is displayed")





@then('error message "{errorMessage}" is displayed')
def userErrorMessage(context,errorMessage):
    errorMsg = context.lp.getLoginErrorMessage()
    result = bool(errorMsg == errorMessage)
    context.ts = TestStatus(context.driver)
    context.ts.mark("userErrorMessage", result, "Error Message is Displayed")





@when('User fill the login details')
def userLoginDetails(context):
    context.execute_steps(u"""
        When User clicks on the Sign In link
        And User enters "shankubisai3333@gmail.com" as email
        And User clicks Next Button
        And User enters "shanku12345#" as password
        And User clicks Sign In Button
    """)






















