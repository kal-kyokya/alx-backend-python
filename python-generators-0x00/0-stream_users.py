#!/usr/bin/env python3
"""
'0-stream_users' Uses a generator to fetch rows one by one from a database table
"""
import os
from mysql.connector import connect, Error
from dotenv import load_dotenv

load_dotenv()

# ------------------------------------
# MySQL and Database credentials
# ------------------------------------
DB_USER = os.getenv("MYSQL_USER")
DB_HOST = os.getenv("MYSQL_HOST")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("MYSQL_DB_NAME")
DB_TABLE_NAME = os.getenv("MYSQL_DB_TABLE_NAME")

# ---------------------------------------------
# Establish a connection with the database
# ---------------------------------------------
try:
    connection = connect(
        user=DB_USER,
        host=DB_HOST,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    if connection.is_connected():
        print("Database connection to {} successful.".format(DB_NAME))
except Error as err:
    print("Failed to connect to {}.".format(DB_NAME))
    print("Error: {}".format(err))

# -----------------------------------
# Generator: Stream rows lazily
# -----------------------------------
def stream_users():
    """Sequentially send single row upon 'next()' calls
    Args:
    	connection: A MySQL Database connection object
    Return:
    	A 'yielded' table record
    """
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM {}".format(DB_TABLE_NAME))

    for row in cursor:
        yield row

    cursor.close()
