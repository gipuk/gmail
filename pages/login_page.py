from selenium.webdriver.common.by import By

from browser import Browser

class Login(Browser):
    locator_dictionary = {
        'email_input': (By.CSS_SELECTOR, '#identifierId'),
        'next_btn': (By.CSS_SELECTOR, '#identifierNext'),
        'input_password': (By.CSS_SELECTOR, '[type="password"]'),
        'next_btn_pass': (By.CSS_SELECTOR, '#passwordNext'),
        'menu_btn': ( By.CSS_SELECTOR, '[class="gb_ab gbii"]'),
        'signout_btn':(
            By.CSS_SELECTOR,
            '[class="gb_Ea gb_Pf gb_Wf gb_De gb_Db"]'
        ),


    }

    def enter_email(self):
        self.email_input.send_keys('iokipearsontest@gmail.com')
        self.next_btn.click()

    def enter_password(self, variant):
        if variant == "proper":
            self.input_password.send_keys('ioki12qw')
        else:
            self.input_password.send_keys('blablabla')

    def click_menu_btn(self):
        self.menu_btn.click()
        self.signout_btn.click()
