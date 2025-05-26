#!/usr/bin/env python3
"""
'0-stream_users' Uses a generator to fetch rows one by one from a database table
"""
import os
from seed import connect_to_prodev


# -----------------------------------
# Generator: Stream rows lazily
# -----------------------------------
def stream_users():
    """Sequentially send single row upon 'next()' calls
    Args:
    	connection: A MySQL Database connection object
    Return:
    	A 'yielded' table record
    """
    connection = connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM {}".format(DB_TABLE_NAME))

    for row in cursor:
        yield row

    cursor.close()
    connection.close()
