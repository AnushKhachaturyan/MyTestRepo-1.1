from Helper.helper_functions import Helper
from selenium.webdriver.common.by import By
import logging


class Login(Helper):

    username_loc = ((By.ID, "username"), "Username field")
    password_loc = ((By.ID, "password"), "Password field")
    login_btn_loc = ((By.ID, "submit_login_page"), "Submit button")
    success_popup_loc = ((By.ID, 'welcome_text'), "Success popup")


    def login(self, username, password):
        self.find_element_send_keys(self.username_loc, username)
        self.find_element_send_keys(self.password_loc, password)
        self.find_element_and_click(self.login_btn_loc)
        logging.info("Login successful")

    def get_welcome_text(self):
        return self.find_element_get_text(self.success_popup_loc)   
