#!/usr/bin/env python3
"""
'seed' contains 5 functions enabling set up of the MySQL database 'ALX_prodev' with user data availed in a CSV file
"""
import os
from dotenv import load_dotenv
from mysql.connector import connect, Error, errorcode
import csv

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
            user=DB_USER,
            host=DB_HOST,
            password=DB_PASSWORD,
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

# ----------------------------
# Create a Database Table
# ----------------------------
def create_table(connection):
    """Creates a table 'user_data' if it does not exist
    Args:
    	connection: A MySQL Database connection object
    Return:
        None
    """
    sql_query = f"""
    CREATE TABLE IF NOT EXISTS {DB_TABLE_NAME} (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        INDEX(user_id),
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50) NULL,
        age DECIMAL(10, 3) NOT NULL
    )
    """
    cursor = connection.cursor()

    try:
        cursor.execute(sql_query)
        connection.commit()
        print("Database table {} successfully created.\n".format(DB_TABLE_NAME))
        return
    except Error as err:
        print("Database table was not created.")
        print("Creation of {} error: {}".format(DB_TABLE_NAME, err))
    finally:
        cursor.close()

# ---------------------------------------
# Insert user's data in the database
# ---------------------------------------
def insert_data(connection, data):
    """Inserts data in the database if it does exist
    Args:
    	connection: A MySQL Database connection object
    	data: A CSV file contain the required values
    Return:
    	None
    """
    cursor = connection.cursor()

    try:
        with open(data, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for record in reader:
                name = record['name']
                email = record['age']
                age = float(record['age'])

                sql_select = "SELECT email FROM {} WHERE email = %s".format(DB_TABLE_NAME)
                # Ensure that the user does not exist in the database
                cursor.execute(sql_select, (email,))
                if cursor.fetchone():
                    continue

                sql_insert = f"""
                INSERT INTO {DB_TABLE_NAME} (name, email, age)
                VALUES (%s, %s, %s)"""

                cursor.execute(sql_insert, (name, email, age))

            connection.commit()
            print("Data successfully inserted in the table.\n")
    except Error as err:
        print("Data insertion was not completed.")
        print("Insertion of {} error: {}".format(data, err))
        connection.rollback()
    finally:
        cursor.close()

# -----------------------------------
# Generator: Stream rows lazily
# -----------------------------------
def stream_user_data(connection):
    """Sequentially send single row upon 'next()' calls
    Args:
    	connection: A MySQL Database connection object
    Return:
    	A 'yielded' table record
    """
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM {}".format(DB_TABLE_NAME))

    for row in cursor:
        yield row

    cursor.close()
