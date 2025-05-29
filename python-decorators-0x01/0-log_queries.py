#!/usr/bin/env python3
"""
'0-log_queries' creates a decorator that logs database queries executed by any function
"""
import sqlite3
import functools
import time
from datetime import datetime


# --------------------------------------------
# Decorator to log function's SQL Queries
# --------------------------------------------
def log_queries(func):
    """Logs database queries executed by the 'decorated' function
    Args:
    	func: The function to be decorated
    Return:
    	A 'wrapper' function adding logging functionality to the decorated
    """
    def wrapper(*args, **kwargs):
        """A wrapper function adding logging functionality to the decorated
        Args:
        	args: An arbitrary number of positional arguments.
        	kwargs: An arbitrary number of keyword arguments.
        Return:
        	None
        """
        print("The first query executed was: '{}'\n".format(kwargs['query1']))
        time.sleep(5)
        func(**kwargs)

    return wrapper

@log_queries
def fetch_all_users(query1, query2):
    """Simulate retrieval of user data from a database
    Args:
    	query1: The first SQL query to be executed by the cursor object
    	query2: The second SQL query to be executed by the cursor object
    Return:
    	A list of users in database
    """
    conn = "Database connection object: sqlite3.connect('players.db')"
    cursor = "SQL cursor object: conn.cursor()"

    print("cursor.execute({})\n".format(query1))
    time.sleep(8)

    results = "User list: cursor.fetchall()"
    print("conn.close()\n")

    return results

# ----------------------------------------
# Fetch users while logging the query
# ----------------------------------------
users = fetch_all_users(query1="SELECT name, jersey_no FROM players", query2="SELECT name, jersey_no FROM players")
