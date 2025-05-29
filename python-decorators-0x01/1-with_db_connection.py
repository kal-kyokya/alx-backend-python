#!/usr/bin/env python3
"""
'1-with_db_connection' creates a decorator that automatically handles opening and closing database connections
"""
import os
from dotenv import load_dotenv
from mysql.connector import connect, Error
import functools
import time


load_dotenv()

# -----------------------------------
# MySQl and Database credentials
# -----------------------------------
DB_USER = os.getenv("MYSQL_USER")
DB_HOST = os.getenv("MYSQL_HOST")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("MYSQL_DB_NAME")
DB_TABLE_NAME = os.getenv("MYSQL_DB_TABLE_NAME")

# --------------------------------------------
# Connect to the MySQL Server (no DB yet)
# --------------------------------------------
def connect_db():
    """Establishes a connection with the MySQL Server
    Args:
    	None
    Return:
    	A MySQL Server connection object
    """
    # Try establishing the connection
    try:
        conn = connect(
            user=DB_USER,
            host=DB_HOST,
            password=DB_PASSWORD,
            database=DB_NAME,
        )

        # Check if the connection was successful
        if conn.is_connected():
            print("DB connection to {} successfully established.\n".format(DB_NAME))
            return conn
    except Error as err:
        print("Database connection was not established.\n")
        print("Connection error: {}".format(err))
        return None

# ----------------------------------------------------------
# Decorator to handle opening/closing of DB connections
# ----------------------------------------------------------
def with_db_connection(func):
    """Handles opening and closing of DB connections before execution of the 'decorated' function
    Args:
    	func: The function to be decorated
    Return:
    	A 'wrapper' function adding DB connection opening/closing functionality to the decorated
    """
    def wrapper(*args, **kwargs):
        """A wrapper function adding DB connection opening/closing functionality to the decorated
        Args:
        	args: An arbitrary number of positional arguments.
        	kwargs: An arbitrary number of keyword arguments.
        Return:
        	None
        """
        try:
            conn = connect_db()
            result = func(conn, kwargs['user_id'])
            return result
        finally:
            conn.close()
            print("DB connection to {} successfully closed.\n".format(DB_NAME))

    return wrapper

@with_db_connection
def get_user_by_id(conn, user_id):
    """Retrieves a user's infos from the database
    Args:
    	conn: The DB connection object enable data manipulation
    	user_id: The ID of the sought for user
    Return:
    	A list of one element containing the user as an object
    """
    cursor = conn.cursor()

    sql_query = "SELECT * FROM {} WHERE user_id LIKE %s".format(DB_TABLE_NAME)
    cursor.execute(sql_query, (user_id,))

    return cursor.fetchone()

# ----------------------------------------------------------
# Fetch a user by ID with automatic connection handling
# ----------------------------------------------------------
user = get_user_by_id(user_id=1)
print(get_user_by_id(user_id=1))
