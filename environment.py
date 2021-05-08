import logging
from base.webdriverfactory import WebDriverFactory
from utilities import custom_logger as cl

log = cl.customLogger(logging.DEBUG)

def before_feature(context,feature):
    print("before feature")



def after_feature(context,feature):
    print("after feature")




def before_scenario(context,scenario):
    print("before scenario")
    wb = WebDriverFactory("chrome")
    context.driver = wb.getWebDriverInstance()
    log.info("Browser Opened")




def after_scenario(context,scenario):
    print("after scenario")
    context.driver.close()
    log.info("Browser Closed")





def before_step(context,step):
    pass




def after_step(context,step):
    pass





def before_tag(context,tag):
    pass





def after_tag(context,tag):
    pass





def before_all(context):
    pass




def after_all(context):
    pass

