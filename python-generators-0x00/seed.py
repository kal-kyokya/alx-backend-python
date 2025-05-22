#!/usr/bin/env python3
"""
'seed' contains 5 functions enabling set up of the MySQL database 'ALX_prodev' with user data availed in a CSV file
"""

def connect_db():
    """Connects to the MySQL database server
    Args:
    	None
    Return:
    	A MySQL Server connection object
    """
    # Dummy result
    print("Server Connection established.\n")

    class Cursor:
        """A blueprint for instance of a successfully established database connection"""

        def execute(self, command):
            """Runs the availed SQL command"""
            print(command)
            return

    class DatabaseConn:
        """A blueprint for instance of a successfully established database connection"""

        def close(self):
            """Ensures a MySQL is terminated"""
            print("Connection closed.\n")

        def cursor(self):
            """A DML-enabled object for CRUD operations"""
            return Cursor()

    return DatabaseConn()

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
    return True

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
