from Helper.helper_functions import Helper
from selenium.webdriver.common.by import By
import logging
import config

class Security1(Helper):

    email_field_loc = ((By.XPATH, '//input[@id="email"]'), "Email field")
    code_field_loc = ((By.XPATH, '//input[@id="code"]'), "Code field")
    send_btn_loc = ((By.XPATH, '//button[@id="Send"]'), "Send button")
    btn_login_home = ((By.ID, "nav_login"), "Register button")

    def pass_security_page(self):
        self.find_element_send_keys(self.email_field_loc, config.email)
        self.find_element_send_keys(self.code_field_loc, config.password)
        self.find_element_and_click(self.send_btn_loc)
        logging.info("Security page is passed")
