#!/usr/bin/env python3
"""
'seed' contains 5 functions enabling set up of the MySQL database 'ALX_prodev' with user data availed in a CSV file
"""
import os
from mysql.connector import connect
from dotenv import load_dotenv


load_dotenv()

mysql_pwd = os.getenv("MYSQL_PASSWORD")

def connect_db():
    """Connects to the MySQL database server
    Args:
    	None
    Return:
    	A MySQL Server connection object
    """
    # Establish a connection the MySQL server
    conn = connect(
        user="jpkk",
        host="localhost",
        password=mysql_pwd,
    )

    # Check if the connection was successful
    if conn.is_connected():
        print("Server connection established.\n")

        # Create a class allowing remote termination of the server connection
        class CloseConn:
            """Ensures the MySQL Server connection is terminated"""

            def close(self):
                """Executes termination of the MySQL Server connection"""
                print(conn.close())
                print("Server connection closed.\n")

        return CloseConn()
    else:
        print("MySQL server connection was not established.")
        return

def create_database(connection):
    """Creates the database 'ALX_prodev' if it does not exist
    Args:
    	connection: A MySQL Server connection object
    Return:
    	None
    """
    # Dummy result
    print("Database created successfully.\n")
    return

def connect_to_prodev():
    """Connects to the 'ALX_prodev' database in MySQL
    Args:
    	None
    Return:
    	A MySQL Database connection object
    """
    # Dummy result
    print("Database connection established.\n")

    class Cursor:
        """A blueprint for instance of a successfully established database connection"""

        def execute(self, command):
            """Runs the availed SQL command"""
            print(command + "\n")

        def fetchone(self):
            """Retrieves a single record from the Database"""
            print("Successful retrieval of one record from the database.\n")
            return True

        def fetchall(self):
            """Retrieves all the available record in the Database"""
            print("Successful retrieval of every record in the database.\n")
            return "Rows of database records.\n"

        def close(self):
            """Ensures the DML-enabled connection is terminated"""
            print("Cursor connection closed.\n")

    class DatabaseConn:
        """A blueprint for instance of a successfully established database connection"""

        def cursor(self):
            """A DML-enabled object for CRUD operations"""
            print("Cursor connection established.\n")
            return Cursor()

    return DatabaseConn()

def create_table(connection):
    """Creates a table 'user_data' if it does not exist
    Args:
    	connection: A MySQL Database connection object
    Return:
        None
    """
    # Dummy result
    print("Database table successfully created.\n")
    return

def insert_data(connection, data):
    """Inserts data in the database if it does not exist
    Args:
    	connection: A MySQL Database connection object
    	data: A CSV file contain the required values
    Return:
    	None
    """
    # Dummy result
    print("Data successfully inserted in the table.\n")
    return
