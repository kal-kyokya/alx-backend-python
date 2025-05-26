#!/usr/bin/python3
"""
'4-stream_ages' computes a memory-efficient aggregate function
"""
from seed import connect_to_prodev

# -------------------------------------------------
# Fetches the age attributes for all users
# -------------------------------------------------
def user_ages():
    """Retrieves the age attribute from the table 'user_data'
    Args:
    	None
    Return:
    	A list consisting of all age values
    """
    connection = connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute(f"SELECT age FROM user_data")
    rows = cursor.fetchall()
    connection.close()
    return rows

# -------------------------------------------
# Generator: Yields user ages one by one
# -------------------------------------------
def stream_user_ages():
    """Yields user ages one by one
    Args:
    	None
    Return:
    	A 'yielded' user age value
    """
    for age in user_ages():
        yield age[0]

# -----------------------------------------------
# Efficiently calculate the average user age
# -----------------------------------------------
def avg_user_age():
    """Computes the average age without loading the entire dataset into memory
    Args:
    	None
    Return:
    	None
    """
    counter = 0
    total_age = 0
    for age in stream_user_ages():
        total_age += float(age)
        counter += 1

    print("Average age of users: {}".format(total_age/counter))
