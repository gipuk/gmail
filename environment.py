from browser import Browser
from pages.login_page import Login
from pages.email_page import EmailPage
from pages.write_email import WriteEmail

def before_all(context):
    context.browser = Browser()
    context.login = Login()
    context.email_page = EmailPage()
    context.write_email = WriteEmail()

def after_scenario(context, scenario):
    context.browser.delete_cookies()

def after_all(context):
    context.browser.quit()