#!/usr/bin/env python3
"""
'2-transactional' creates a decorator that manages database transactions by automatically committing or rolling back changes
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

# ---------------------------------------------------------------
# Decorator ensuring rollback on error or commmit on success
# ---------------------------------------------------------------

def transactional(func):
    """Handles rollbacks or commmits after execution of the 'decorated' function
    Args:
    	func: The function to be decorated
    Return:
    	A 'wrapper' function handling rollback or commit actions
    """

    @wraps(func)
    def wrapper(conn, *args, **kwargs):
        """A wrapper function ensuring rollback on error or commmit on success
        Args:
        	args: An arbitrary number of positional arguments.
        	kwargs: An arbitrary number of keyword arguments.
        Return:
        	None
        """

        try:
            result = func(conn, *args, **kwargs)
        except Exception as err:
            conn.rollback()
            print("DB connection to {} was rollback due to:\n {}.\n".format(DB_NAME, err))
        else:
            conn.commit()
            print("Update on {} was successful.\n".format(DB_NAME))
            return  result

    return wrapper

@with_db_connection
@transactional
def update_user_details(conn, user_id, new_email):
    """Updates a user's infos in the database
    Args:
    	conn: The DB connection object enable data manipulation
    	user_id: The ID of the sought for user
    	new_email: The replacement email
    Return:
    	A list of one element containing the user as an object
    """
    cursor = conn.cursor()

    sql_query = f"""
    	UPDATE {DB_TABLE_NAME}
    	SET email = %s
    	WHERE user_id = %s"""
    cursor.execute(sql_query, (new_email, user_id,))

    return cursor.fetchone()

# -----------------------------------------------------
# Update a user's name and email based on their ID
# -----------------------------------------------------

print(update_user_details(user_id=2,
                           new_email='dem@email.com'))
