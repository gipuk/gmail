from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Chrome()

def after_scenario(context, scenario):
    context.browser.delete_all_cookies()

def after_all(context):
    context.browser.quit()