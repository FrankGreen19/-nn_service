import json

import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv


def get_connection():
    load_dotenv()

    connection = None
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS")
        )
        print("Connected successful")
    except Error as e:
        print(f"The error '{e}' occurred")

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
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def get_async_job(id):
    query = 'SELECT * FROM async_job WHERE id = ' + str(id)
    return execute_select_query(query)[0]

def update_async_job_status(id, status):
    query = "UPDATE async_job SET status = '" + status + "' WHERE id = " + str(id)
    execute_update_query(query)


def update_medical_test(id, fuzzyResult=False, cnnResult=False):
    query = "UPDATE medical_test SET "
    if fuzzyResult:
        query += "fuzzy_result = '" + fuzzyResult + "'"

    if fuzzyResult and cnnResult:
        query += ", "

    if cnnResult:
        query += "cnn_result = '" + cnnResult + "'"

    query += " WHERE id = " + str(id)

    execute_update_query(query)


