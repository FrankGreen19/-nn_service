import json

import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv


def get_connection():
    load_dotenv()

    connection = None
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )
    print("Connected successful")

    return connection


def execute_select_query(query):
    connection = get_connection()
    if not connection:
        return False

    connection.autocommit = True
    cursor = connection.cursor(dictionary=True)

    cursor.execute(query)
    return cursor.fetchall()


def execute_update_query(query):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    print("Query executed successfully")


def execute_insert_query(query):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    print("Query executed successfully")


def get_async_job(id):
    query = 'SELECT * FROM async_job WHERE id = ' + str(id)
    return execute_select_query(query)[0]

def update_async_job_status(id, status):
    query = "UPDATE async_job SET status = '" + status + "' WHERE id = " + str(id)
    execute_update_query(query)


def update_medical_test(id, fuzzyResults=None, cnnResults=None):
    try:
        for fuzzyResult in fuzzyResults:
            illness = execute_select_query("SELECT * FROM illness WHERE title = '" + str(fuzzyResult) + "'")[0]

            execute_insert_query("INSERT INTO fuzzy_result(illness_id, medical_test_id, value) VALUES ({}, {}, {})"
                                 .format(illness['id'], id,  format(fuzzyResults[fuzzyResult], ".2f")))

        for cnnResult in cnnResults:
            illness = execute_select_query("SELECT * FROM illness WHERE title = '" + str(cnnResult) + "'")[0]
            query = "SELECT * FROM illness_subclass WHERE alias = '{}' AND illness_id = '{}'"\
                .format(cnnResults[cnnResult], illness['id'])
            illnessSubclass = execute_select_query(query)[0]

            execute_insert_query("INSERT INTO cnn_result(illness_subclass_id, medical_test_id) VALUES ({}, {})"
                                 .format(illnessSubclass['id'], id))

            return True
    except BaseException as e:
        return False
