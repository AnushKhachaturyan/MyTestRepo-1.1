from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.webdriver.support.ui import Select


class Helper:

    def __init__(self, driver):
        self.driver = driver

    def open_new_page(self, url):
        try:
            self.driver.get(url)
        except Exception:
            logging.error(f"Could not open {url}")

    def find_element(self, loc, timeout=5):
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(loc[0]))
            return elem
        except Exception as e:
            logging.error(f"{loc[1]} is not found {e}")

    def find_elements(self, loc, timeout=10):
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(loc[0]))
            return elements
        except Exception as e:
            logging.error(f"{loc[1]} are not found {e}")

    def find_element_and_click(self, loc, timeout=5):

        elem = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(loc[0]))
        elem.click()

    def find_element_send_keys(self, loc, text, timeout=5):
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(loc[0]))
            elem.send_keys(text)
        except Exception as e:
            logging.error(f"{loc[1]} are not found {e}")

    def get_element_text(self, loc, timeout=5):
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(loc[0]))
            elem_text = elem.text
            return elem_text
        except Exception as e:
            logging.error(f"{loc[1]} are not found {e}")

    def wait_for_element(self, loc, sec=10):
        try:
            WebDriverWait(self.driver, sec).until(
                EC.element_to_be_clickable(loc[0]))
        except Exception as e:
            logging.error(e)

    def select_option(self, ddl_element, selected_text):
        dropdown = Select(ddl_element)
        dropdown.select_by_visible_text(selected_text)

    def find_element_get_text(self, loc):
        try:
            elem = WebDriverWait(self.driver, self.wait_time).until(
                EC.visibility_of_element_located(loc[0])
            )
            return elem.text
        except Exception as e:
            logging.error(f"{loc[1]} is not found: {e}")

    def driver_close(self):
        if self.driver:
            self.driver.close()


def select_course_by_title(db_coursor, course_title):
    db_coursor.execute(
        f"SELECT * FROM courses WHERE title='{course_title}'")
    result = db_coursor.fetchone()
    return result


#     def create_connection(self,host,user,password,database):
#         try:
#             self.connection = pymysql.connect(host,user,password,database)
#             self.cursor = self.connection.cursor()
#             logging("Connection succed")
#         except Exception as e:
#             logging("Error{e}")

# #   4.	Add a new course with a unique title.
# # 5.	Connect to the database.
# # 6.	Check if the new course exists in the database.
#     def check_course_exists(self, course_title):
#         try:
#             self.cursor.execute(f"select * from courses where title='{course_title}'")
#             result = self.cursor.fetchone()
#             return result 
#         except Exception as e:
#             logging.error(f"Error checking course existence: {e}")

    

#     def close_connection(self):
#         try:
#             if self.connection:
#                 self.connection.close()
#                 logging.info("DB connection closed")    
#         except Exception as e:
#             logging.error(f"Error closing connection: {e}")




    


  
# #   def update_data(self, myrole_id, myuser_id):
# #     try:
# #       self.cursor.execute(f"update users set role_id = {myrole_id} where id={myuser_id}")
# #       if self.cursor.rowcount <= 1:
# #         self.connection.commit()
# #         print(myrole_id, myuser_id)
# #       else:
# #         self.connection.rollback()
# #         print("No succed")
# #     except Exception as e:
# #       print("Error")
     
