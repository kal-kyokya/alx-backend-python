#!/usr/bin/env python3
"""
'seed' contains 5 functions enabling set up of the MySQL database 'ALX_prodev' with user data availed in a CSV file
"""
import os
from dotenv import load_dotenv
from mysql.connector import connect, Error, errorcode

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
        )

        # Check if the connection was successful
        if conn.is_connected():
            return conn
    except Error as err:
        print("MySQL server connection was not established.\n")
        print("Connection error: {}".format(err))
        return None

# -----------------------------------------
# Create database if it does not exist
# -----------------------------------------
def create_database(connection):
    """Creates the database 'DB_NAME' if it does not exist
    Args:
    	connection: A MySQL Server connection object
    Return:
    	None
    """
    # Try creating the database
    try:
        sql_query = "CREATE DATABASE IF NOT EXISTS {}".format(DB_NAME)
        cursor = connection.cursor()
        cursor.execute(sql_query)

        print("Database created successfully.\n")
    except Error as err:
        print("Database was not created.\n")
        print("Creation error: {}".format(err))
    finally:
        cursor.close()
# -----------------------------------------
# Establish a connection to a Database
# -----------------------------------------
def connect_to_prodev():
    """Connects to the DB_NAME database in MySQL
    Args:
    	None
    Return:
    	A MySQL Database connection object
    """
    # Try establishing a connection the MySQL Database
    try:
        conn = connect(
            user=DB_USER
            host=DB_HOST
            password=DB_PASSWORD
            database=DB_NAME
        )

        # Check if the connection was successful
        if conn.is_connected():
            print("Database connection established.\n")
            return conn
    except Error as err:
        print("Database connection was not established.")
        print("Connection to {} error: {}".format(DB_NAME, err))
        return None

def create_table(connection):
    """Creates a table 'user_data' if it does not exist
    Args:
    	connection: A MySQL Database connection object
    Return:
        None
    """
    sql_query = """
    CREATE TABLE IF NOT EXISTS user_data(
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NULL,
    age DECIMAL(10, 3) NOT NULL
    )
    """

    connection.cursor().execute(sql_query)
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
    sql_query = """
    LOAD DATA LOCAL INFILE %s
    INTO TABLE user_data
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    """

    connection.cursor().execute(sql_query, (data,))

    print("Data successfully inserted in the table.\n")
    return
