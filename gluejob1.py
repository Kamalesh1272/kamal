import mysql.connector
import json
def db_connection(db_config):
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as e:
        print("Error:", e)
        return None

def close_connection(connection):
    if connection:
        connection.close()

def execute_query(connection, sql_query):
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        return rows
    except mysql.connector.Error as e:
        print("Error:", e)
        return None
    finally:
        if cursor:
            cursor.close()

def get_employee_data(db_config):
    connection = db_connection(db_config)
    if connection:
        try:
            with open('k.json') as f:
                sql_query = json.load(f)
                print(sql_query)
            rows = execute_query(connection, sql_query)
            return rows
        finally:
            close_connection(connection)
    return None

