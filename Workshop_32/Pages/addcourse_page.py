from Helper.helper_functions import Helper
from selenium.webdriver.common.by import By
import logging


class AddCourse(Helper):

    title_loc = ((By.ID, "title"), "Title field")
    price_loc = ((By.ID, "price"), "Price field")
    description_loc = ((By.ID, "description"), "Description field")
    btn_submit = ((By.ID, 'Submit'), "Submit button")

    def add_new_course(self, title, price, description):
        self.find_element_send_keys(self.title_loc, title)
        self.find_element_send_keys(self.price_loc, price)
        self.find_element_send_keys(self.description_loc, description)
        self.find_element_and_click(self.btn_submit)
        logging.info("Course is added successfully")
        return title
