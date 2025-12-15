import pytest
from selenium import webdriver
import logging
import pymysql
import allure


@pytest.fixture
def driver():
    dr = webdriver.Chrome()
    dr.maximize_window()
    yield dr
    dr.quit()

@pytest.fixture(scope="session", autouse=True)
def db_connection():
    
    connection = pymysql.connect(host='qwallitydb.cvy8c6y8c0ri.eu-central-1.rds.amazonaws.com',
                                 user='admin', password='qwallity_db#', database='qwallity_db')
    yield connection
    connection.close()

    

@pytest.fixture(autouse=True)
def db_cursor(db_connection):
    cursor = db_connection.cursor()
    yield cursor
    cursor.close()



def pytest_configure():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        filemode='w',
        filename="pytest_log.log"
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call":
        if result.outcome == 'failed':
            allure.attach(
                item.funcargs.get("driver").get_screenshot_as_png(),
                name=f"{item.name}_screen",
                attachment_type=allure.attachment_type.PNG)
