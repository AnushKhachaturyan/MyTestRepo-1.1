import pymysql




def select_course_by_title(db_coursor, course_title):
    db_coursor.execute(
        f"SELECT * FROM courses WHERE title='{course_title}'")
    result = db_coursor.fetchone()
    return result






# def get_db_connection():
#     return pymysql.connect(host_db='qwallitydb.cvy8c6y8c0ri.eu-central-1.rds.amazonaws.com', user_db='admin',
#                            password_db='qwallity_db#',
#                            database='qwallity_db')

# class DB():
    # def __init__(self, host_db, user_db, password_db, database):
    #     self.host_db = host_db
    #     self.user_db = user_db
    #     self.password_db = password_db
    #     self.database = database
    #     self.connection = None
    #     self.cursor = None


# db_conection = DB()
# db_conection.create_connection()
# db_conection.update_data(1, 11)
# db_conection.close_connection()

# # TODO - generally correct, but would be better to use logging instead of print
# # You can also use a try/except block when calling your objects.
# #  It’s not mandatory, but it can help ensure that the connection is closed in a finally block.

# db_connection = DB()
# try:
#     db_connection.create_connection()
#     db_connection.update_data(1, 11)
# except Exception as e:
#     print(f"Error during update: {e}")
# finally:
#     db_connection.close_connection()
