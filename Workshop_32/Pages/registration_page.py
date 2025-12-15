import logging
from selenium.webdriver.common.by import By
from Helper.helper_functions import Helper


class Registration(Helper):

    name_field_loc = ((By.ID, "name"), "Name field")
    email_field_loc = ((By.ID, "email"), "Email field")
    username_field_loc = ((By.ID, "username"), "Username field")
    password_field_loc = ((By.ID, "password"), "Password field")
    confirm_password_field_loc = ((By.ID, "confirm"), "Confirm password field")
    submit_btn_loc = ((By.XPATH, '//input[@type = "submit"]'), "Submit button")
    success_popup_loc = ((By.ID, 'flashwrapper'), "Success popup")

    def registration(self, name, email, username, password):
        self.find_element_send_keys(self.name_field_loc, name)
        self.find_element_send_keys(self.email_field_loc, email)
        self.find_element_send_keys(self.username_field_loc, username)
        self.find_element_send_keys(self.password_field_loc, password)
        self.find_element_send_keys(self.confirm_password_field_loc, password)
        self.find_element_and_click(self.submit_btn_loc)
        logging.info(
            "User is registered: username{username} and password{password}")
        return username, password
