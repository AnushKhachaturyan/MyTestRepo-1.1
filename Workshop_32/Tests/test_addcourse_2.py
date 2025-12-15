from Helper.helper_functions import Helper
from Pages.registration_page import Registration
from Pages.security_page import Security1
from Pages.login_page import Login
import config
from Pages import home_page
from Pages.addcourse_page import AddCourse
from selenium import webdriver
import TestData.testdata
import logging
import Helper.db_helper as db_helper
import pytest


def test_add_course(driver, db_cursor):

    helper_obj = Helper(driver)
    home_page_obj = home_page.Home(driver)
    login_page_obj = Login(driver)
    security_page_obj = Security1(driver)
    add_course_page_obj = AddCourse(driver)

    logging.info("test_add_course IS STARTED")
    helper_obj.open_new_page(config.url)
    security_page_obj.pass_security_page()
    helper_obj.find_element_and_click(home_page_obj.btn_login_home)

    login_page_obj.login(config.testlogin, config.testpassword)

    helper_obj.find_element_and_click(home_page_obj.btn_addcourse_home)
    new_course = add_course_page_obj.add_new_course(TestData.testdata.course_title,
                                                    TestData.testdata.course_price,
                                                    TestData.testdata.course_description)

   
    course_in_db = db_helper.select_course_by_title(db_cursor, new_course)

    assert course_in_db is not None, "Course is not added to DB"
    logging.info("test_add_course IS PASSED")