#!/usr/bin/env python3
"""
'3-retry_on_failure' creates a decorator that retries DB operations if they fail due to transient errors
"""
import os
from dotenv import load_dotenv
from mysql.connector import connect, Error
from functools import wraps
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

    @wraps(func)
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
            result = func(conn, *args, **kwargs)
            return result
        finally:
            conn.close()
            print("DB connection to {} successfully closed.\n".format(DB_NAME))

    return wrapper

# -------------------------------------------------------------
# Decorator retrying operations if they fail due to errors
# -------------------------------------------------------------

def retry_on_failure(retries=3, delay=2):
    """Handles retry on error during execution of the 'decorated' function
    Args:
    	retries: The amount of attempts before an error is raised
    	delay: The time lapse between two retries
    Return:
    	A 'wrapper' function handling retry of operation on error
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """A wrapper function ensuring retry of an operation on error
            	Args:
        		args: An arbitrary number of positional arguments.
        		kwargs: An arbitrary number of keyword arguments.
            Return:
        		None
            """
            attempts = 0

            while attempts < retries:
                try:
                    result = func(*args, **kwargs)
                except Exception as err:
                    attempt += 1
                    if attempts == retries:
                        print("3 attempts were made to {}:\n {}.\n".format(DB_NAME, err))
                    time.sleep(delay)
                else:
                    print("Fetch of users from {} - successful.\n".format(DB_NAME))
                    return  result
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    """Fetch all users from the database
    Args:
    	conn: The DB connection object enable data manipulation
    Return:
    	A list containing the users as an dictionary objects
    """
    cursor = conn.cursor()

    sql_query = "SELECT * FROM {} LIMIT 5".format(DB_TABLE_NAME)
    cursor.execute(sql_query)

    return cursor.fetchall()

# -----------------------------------------------------
# Fetch all users with automatic retry on failure
# -----------------------------------------------------

users = fetch_users_with_retry()

for user in users:
    print(user)
