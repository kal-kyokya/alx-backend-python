#!/usr/bin/env python3
"""
'4-cache_query' creates a decorator that caches the results of a database queries in order to avoid redundant calls
"""
import os
from dotenv import load_dotenv
from mysql.connector import connect, Error
from functools import wraps
import time
import hashlib


load_dotenv()
dummy_cache = {}
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
# Decorator caching query results to avoid redundant calls
# -------------------------------------------------------------

def cache_query(func):
    """Handles cache of query result of the 'decorated' function
    Args:
    	func: The function to be decorated
    Return:
    	A 'wrapper' function handling caching
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """A wrapper function ensuring caching of the query
            Args:
        	args: An arbitrary number of positional arguments.
        	kwargs: An arbitrary number of keyword arguments.
            Return:
		None
        """
        query = kwargs['query']
        cache_key = hashlib.sha256(query.encode()).hexdigest()

        if cache_key in dummy_cache.keys():
            print("Returning from cache\n")
            return dummy_cache[cache_key]
        else:
            try:
                result = func(*args, **kwargs)
            except Exception as err:
                print("Caching of query to {} failed:\n {}.\n".format(DB_NAME, err))
            else:
                dummy_cache[cache_key] = result
                print("Caching for query on {} - successful.\n".format(DB_NAME))

                for cache in dummy_cache:
                    print(cache)
                print()

                return  result

    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    """Fetch all users from the database while caching query
    Args:
    	conn: The DB connection object enable data manipulation
    	query: The SQL query to be executed by the cursor
    Return:
    	A list containing the users as an dictionary objects
    """
    cursor = conn.cursor()

    cursor.execute(query)

    return cursor.fetchall()

# -----------------------------------------------------
# Fetch all users with automatic retry on failure
# -----------------------------------------------------

sql_query1 = "SELECT * FROM {} LIMIT 3".format(DB_TABLE_NAME)
sql_query2 = "SELECT * FROM {} LIMIT 5".format(DB_TABLE_NAME)
sql_query3 = "SELECT * FROM {} LIMIT 3".format(DB_TABLE_NAME)

users1 = fetch_users_with_cache(query=sql_query1)
users2 = fetch_users_with_cache(query=sql_query2)
users3 = fetch_users_with_cache(query=sql_query3)

for user in users1:
    print(user)
print("--")
for user in users2:
    print(user)
print("--")
for user in users3:
    print(user)
