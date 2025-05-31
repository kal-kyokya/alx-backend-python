#!/usr/bin/env python3
"""
'1-execute' creates a reusable class based context mananger that manages database connections and query execution
"""
import os
from dotenv import load_dotenv
from mysql.connector import connect, Error


load_dotenv()

# -----------------------------------
# MySQl and Database credentials
# -----------------------------------
DB_USER = os.getenv("MYSQL_USER")
DB_HOST = os.getenv("MYSQL_HOST")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("MYSQL_DB_NAME")
DB_TABLE_NAME = os.getenv("MYSQL_DB_TABLE_NAME")


class ExecuteQuery:
    """Manages DB connections and SQL query execution
    Args:
    	None
    """

    def __init__(self, query, query_param):
        """Initializes the class instance with the SQL query
        Args:
        	self: An internal representation of the class' instantiation
        	query: The SQL command to be executed
        	query_param: The value to be passed to the SQL query
        """
        self.query = query
        self.query_param = query_param

    def __enter__(self):
        """Gets executed upon class instantiation, handles connection and query execution
        Args:
        	self: An internal representation of the class' instantiation
        """

        try:
            conn = connect(
                user=DB_USER,
                host=DB_HOST,
                password=DB_PASSWORD,
                database=DB_NAME
            )
            self.conn = conn
            print("DB connection to {} - Established successfully\n".format(DB_NAME))

            cursor = conn.cursor()
            cursor.execute(self.query, self.query_param)
            
            return cursor.fetchall()
        except Error as err:
            print("Operating on {} - Failed".format(DB_NAME))
            raise err

    def __exit__(self, exc_type, exc_value, exc_tb):
        """Gets executed upon termination of the 'with' context and closes the DB connection
        Args:
        	self: An internal representation of the class' instantiation
        """

        try:
            self.conn.close()
            print("DB connection to {} - Closed successfully\n".format(DB_NAME))
        except Error as err:
            print("Closing the DB connection for {} - Failed".format(DB_NAME))
            raise err


# ---------------------------------------
# Run a test SQL query on the class
# ---------------------------------------
print("Before the class based Context manager\n")

sql_query = "SELECT name, email, age FROM {} WHERE age < %s LIMIT 5".format(DB_TABLE_NAME)
query_param = (5,)

with ExecuteQuery(sql_query, query_param) as results:
    for user in results:
        print(user)
    print("")

print("After the class based Context manager\n")
