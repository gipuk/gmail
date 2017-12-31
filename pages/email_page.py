from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from browser import Browser

class EmailPage (Browser):
    locator_dictionary = {
        'apps_btn':(By.CSS_SELECTOR, '#gbwa > div.gb_Mc > a'),
        'mail_btn':(By.CSS_SELECTOR, '#gb23 > span.gb_2'),
        'compose_btn': (By.CSS_SELECTOR, '[class="T-I J-J5-Ji T-I-KE L3"]'),
    }

    def go_to_emails(self):
        self.apps_btn.click()
        self.mail_btn.click()

    def click_compose_btn(self):
        self.compose_btn.click()
        WebDriverWait(self, 10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '[class="aYF"]'),
                'New Message'
            )
        )
