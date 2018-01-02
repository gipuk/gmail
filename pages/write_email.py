from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from browser import Browser
from pages.login_page import Login

class WriteEmail(Browser):
    locator_dictionary = {
        'enter_rcvr_mail': (By.CSS_SELECTOR, '[name="to"]'),
        'enter_subject': (By.CSS_SELECTOR,'[name="subjectbox"]'),
        'enter_text': (By.CSS_SELECTOR, '[class="Am Al editable LW-avf"]'),
        'send_btn': (By.CSS_SELECTOR, '[class="T-I J-J5-Ji aoO T-I-atl L3"]'),
        'cancel_btn':(By.CSS_SELECTOR, '[class="og T-I-J3"]'),
        'attach_btn':(By.CSS_SELECTOR, '[command="Files"]'),
        'sent_tab': (By.CSS_SELECTOR, '[title="Sent Mail"]'),
        'search_field': (By.CSS_SELECTOR, '[id="gbqfq"]'),
        'search_btn': (By.CSS_SELECTOR, '[class="gbqfi gb_cc"]'),

    }


    def enter_receiver_mail(self):
        self.enter_rcvr_mail.send_keys('yaqbeush@gmail.com')

    def enter_email_subject(self):
        self.enter_subject.send_keys('subjecttest')

    def enter_email_text(self):
        self.enter_text.send_keys('texttest')

    def click_send_btn(self):
        self.send_btn.click()

    def click_cancel_btn(self):
        self.cancel_btn.click()

    def attach_file(self):
        imagepath = os.path.abspath('testdoc.txt')
        self.attach_btn.send_keys(imagepath)

    def email_send(self):
        page = Login()
        WebDriverWait(self, 20).until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR,'[id=":7y"]'
            ))
        )
        self.sent_tab.click()
        self.search_field.send_keys('subjecttest')
        self.search_btn.click()
        WebDriverWait(self, 20).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR,'[class="zA yO"]'), 
                'subjecttest'
            )
        )
        page.click_menu_btn()

    def email_not_send(self):
        page = Login()
        WebDriverWait(self, 10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR,'[class="bofITb"]'),
                'Your message has been discarded.'
            )
        )
        page.click_menu_btn()



