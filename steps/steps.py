import os
from behave import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("I'm on gmail login page")
def step_impl(context):
    context.browser.open_home_page()

@given('User is logged to gmail')
def step_impl(context):
    context.execute_steps('''
        given I'm on gmail login page
        when I enter proper email
        and I enter "proper" password
        and I click next button
        and I go to e-mails
        ''')

@when('I enter proper email')
def step_impl(context):
   context.login.enter_email()

@when('I enter "{variant}" password')
def step_impl(context, variant):
    context.login.enter_password(variant)

@when('I click next button') 
def step_impl(context):
    context.login.next_btn_pass.click()

@when('I go to e-mails')
def step_impl(context):
    context.email_page.go_to_emails()

@when('I click compose button')
def step_impl(context):
    context.email_page.click_compose_btn()

@when('I enter e-mail addres')
def step_impl(context):
    context.write_email.enter_receiver_mail()

@when('I enter e-mail subject')
def step_impl(context):
    context.write_email.enter_email_subject()

@when('I enter text')
def step_impl(context):
    context.write_email.enter_email_text()

@when('I click send button')
def step_impl(context):
    context.write_email.click_send_btn()
    
@when('I click cancel button')
def step_impl(context):
    context.write_email.click_cancel_btn()

@when('I attach file')
def step_impl(context):
    context.write_email.attach_file()

@then('I am redirected to gmail homepage, so I can see my emails')
def step_impl(context):
    context.login.click_menu_btn()

@then('user​ ​is​ informed​ ​about​ wrong​ ​credentials')
def step_impl(context):
    WebDriverWait(context.browser, 20).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#password > div.LXRPh > div.dEOOab.RxsGPe'),
            'Wrong password. Try again or click Forgot password to reset it.'
        )
    )

@then('user is asked to enter password')
def step_impl(context):
    WebDriverWait(context.browser, 20).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#password > div.LXRPh > div.dEOOab.RxsGPe'),
            'Enter a password'
        )
    )

@then('e-mail is sent')
def step_impl(context):
    context.write_email.email_send()

@then('e-mail is not sent')
def step_impl(context):
    context.write_email.email_not_send()

