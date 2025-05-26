#!/usr/bin/python3
"""
'2-lazy_paginate' simulates fetching paginated data from a database using a generator to lazily load each page
"""
from seed import connect_to_prodev

# -------------------------------------------------
# Fetches a defined set of rows from a database
# -------------------------------------------------
def paginate_users(page_size, offset):
    """Retrieves records from the table 'user_data'
    Args:
    	page_size: The number of users —— each page assumed to be filled with 1 user's data
    	offset: The starting point for retrieval of subsequent reads
    Return:
    	A list of all users composing the required set
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

# ---------------------------------------------------
# Generator: Lazily loads user pages client-side
# ---------------------------------------------------
def lazy_paginate(page_size):
    """Lazily loads a number of user pages
    Args:
    	page_size: The number of pages
    Return:
    	A 'yielded' user page
    """
    offset = 0

    while True:
        page = paginate_users(page_size, offset)

        if len(page) == 0:
            break
        yield page
        offset += page_size
