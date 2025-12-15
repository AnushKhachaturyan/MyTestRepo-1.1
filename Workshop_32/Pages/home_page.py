from Helper.helper_functions import Helper
from selenium.webdriver.common.by import By


class Home(Helper):

    #locators
    btn_login_home = ((By.ID, "nav_login"), "Register button")
    btn_register_home = ((By.ID, "nav_register"), "Register button")
    welcome_text_loc = ((By.ID, "welcome"), "Welcome text")

    btn_addcourse_home = ((By.ID, "add_course"), "Add Course button")