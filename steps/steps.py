import os
from behave import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("I'm on gmail login page")
def step_impl(context):
    context.browser.get('https://accounts.google.com')

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
    context.browser.find_element_by_css_selector(
        '#identifierId'
    ).send_keys('iokipearsontest@gmail.com')
    WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, '#identifierNext'
        ))
    ).click()

@when('I enter "{type}" password')
def step_impl(context, type):
    input_password = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, '[type="password"]'
        ))
    )
    if type == "proper":
        input_password.send_keys('ioki12qw')
    else:
        input_password.send_keys('blablabla')

@when('I click next button') 
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, '#passwordNext'
        ))
    ).click()

@when('I go to e-mails')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, '#gbwa > div.gb_Mc > a'
        ))
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, '#gb23 > span.gb_2'
        ))
    ).click()

@when('I click compose button')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, '[class="T-I J-J5-Ji T-I-KE L3"]'
        ))
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '[class="aYF"]'),
            'New Message'
        )
    )

@when('I enter e-mail addres')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        '[name="to"]'
    ).send_keys('yaqbeush@gmail.com')

@when('I enter e-mail subject')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        '[name="subjectbox"]'
    ).send_keys('subjecttest')

@when('I enter text')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        '[class="Am Al editable LW-avf"]'
    ).send_keys('texttest')

@when('I click send button')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        '[class="T-I J-J5-Ji aoO T-I-atl L3"]'
    ).click()

@when('I click cancel button')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        '[class="og T-I-J3"]'
    ).click()

@when('I attach file')
def step_impl(context):
    imagepath = os.path.abspath('testdoc.txt')
    context.browser.find_element_by_css_selector(
        '[command="Files"]'
    ).send_keys('testdoc.txt')

@then('I am redirected to gmail homepage, so I can see my emails')
def step_impl(context):
    WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, '[class="gb_ab gbii"]'
        ))
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, '[class="gb_Ea gb_Pf gb_Wf gb_De gb_Db"]'
        ))
    ).click()

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
    WebDriverWait(context.browser, 20).until(
        EC.invisibility_of_element_located(
            (By.CSS_SELECTOR,'[id=":7y"]'
        ))
    )
    WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR,'[href="https://mail.google.com/mail/#sent"]'
        ))
    ).click()
    WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, '[id="gbqfq"]'
        ))
    ).send_keys('subjecttest')
    context.browser.find_element_by_css_selector('[class="gbqfi gb_cc"]'
    ).click()
    WebDriverWait(context.browser, 20).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR,'[class="zA yO"]'), 
            'subjecttest'
        )
    )
    WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, '[class="gb_ab gbii"]'
        ))
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, '[class="gb_Ea gb_Pf gb_Wf gb_De gb_Db"]'
        ))
    ).click()

@then('e-mail is not sent')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR,'[class="bofITb"]'),
            'Your message has been discarded.'
        )
    )
    WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, '[class="gb_ab gbii"]'
        ))
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, '[class="gb_Ea gb_Pf gb_Wf gb_De gb_Db"]'
        ))
    ).click()


