#!/usr/bin/env python3
"""
'0-databaseconnection' creates a class based context mananger that handles opening and closing database connections automatically
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


class DatabaseConnection:
    """Handles opening and closing of database connections
    Args:
    	None
    """

    def __init__(self):
        """Initializes the class instance
        Args:
        	self: An internal representation of the class' instantiation
        """
        pass

    def __enter__(self):
        """Gets executed upon class instantiation and sets up the DB connection
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
            print("DB connection to {} - established successfully\n".format(DB_NAME))
            return conn
        except Error as err:
            print("Connection to {} failed".format(DB_NAME))
            raise err

    def __exit__(self, exc_type, exc_value, exc_tb):
        """Gets executed upon termination of the 'with' context and closes the DB connection
        Args:
        	self: An internal representation of the class' instantiation
        """

        try:
            self.conn.close()
            print("DB connection to {} - closed successfully\n".format(DB_NAME))
        except Error as err:
            print("Closing the DB connection for {} failed".format(DB_NAME))
            raise err


if __name__ == "__main__":

    # ---------------------------------------
    # Run a test SQL query on the class
    # ---------------------------------------
    print("Before the class based Context manager\n")

    with DatabaseConnection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        cursor.execute("SELECT name, email FROM {} LIMIT 5".format(DB_TABLE_NAME))

        for user in cursor.fetchall():
            print(user)
        print("")

    print("After the class based Context manager\n")
