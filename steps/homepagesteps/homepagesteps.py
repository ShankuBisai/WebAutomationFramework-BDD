import logging
from behave import given, then
from base.webdriverfactory import WebDriverFactory
from pages.actions.homepage.homepage import HomePage


@given('User go to the site')
def userGoToURL(context):
    # wb = WebDriverFactory("chrome")
    # context.driver=wb.getWebDriverInstance()
    pass


@then('Page title should be "{pageTitle}"')
def userHomePageTitle(context,pageTitle):
    context.hp = HomePage(context.driver)
    assert context.hp.verifyHomePageTitle() == "Zoho - Cloud Software Suite and SaaS Applications for Businesses"



@then('URL should be "{url}"')
def pageUrl(context,url):
    context.hp = HomePage(context.driver)
    assert context.hp.verifyHomePageURL() == "https://www.zoho.com/"
