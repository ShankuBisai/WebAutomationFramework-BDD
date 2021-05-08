from pages.locators.loginpagelocators.loginpagelocators import LoginPageLocator as locator
from pages.actions.clienthomepage.clienthomepage import ClientHomePage
from base.basepage import BasePage
from utilities import custom_logger as cl
import logging


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enterEmail(self,username):
        self.sendKeys(username, locator.email)

    def clickNextButton(self):
        self.elementClick(locator.nextButton)

    def enterPassword(self,password):
        self.sendKeys(password,locator.password)

    def clickSignInButton(self):
        self.elementClick(locator.signInButton)
        return ClientHomePage(self.driver)

    # def login(self, username, password):
    #     self.enterEmail(username)
    #     self.clickNextButton()
    #     self.enterPassword(password)
    #     self.clickSignInButton()
    #     return ClientHomePage(self.driver)

    def getErrorSignText(self):
        return self.verifyPageText(locator.ErrorText)


    def verifyEmailIDTextBox(self):
        return self.isElementPresent(locator.emailIDTextBox)


    def verifyLoginPageTitle(self,):
        return self.verifyPageTitle()


    def getSignInText(self):
        return self.verifyPageText(locator.signInText)


    def getLoginErrorMessage(self):
        return self.getText(locator.loginErrorMessage)
















