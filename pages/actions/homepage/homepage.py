import logging

from base.basepage import BasePage
from pages.actions.homepage.customerpage import CustomerPage
from pages.actions.loginpage.loginpage import LoginPage
from utilities import custom_logger as cl
from base.selenium_driver import SeleniumDriver
from pages.locators.homepagelocators.homepagelocators import HomePageLocators as locator


class HomePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    def menuLinksText(self):
        listText = []
        elements=self.getElements(locator.menulinks)
        for element in elements:
            listText.append(element.text)
        return listText

    def clickCustomersLink(self):
        SeleniumDriver(self.driver).elementClick(locator.customerLink)
        return CustomerPage(self.driver)

    def clickSignInLink(self):
        self.elementClick(locator.signInLink)
        return LoginPage(self.driver)

    def verifyHomePageTitle(self,):
        return self.verifyPageTitle()

    def verifyHomePageURL(self):
        return self.verifyPageURL()


