#!/usr/bin/env python3
"""
'1-batch_processing' creates a generator to fetch and process data in batches from a database
"""
import os
from seed import connect_to_prodev


# -----------------------------------------------
# Retrieve data from the database in batches
# -----------------------------------------------
def stream_users_in_batches(batch_size):
    """Fetches table records in batches
    Args:
    	batch_size: The length of the expected batch
    Return:
    	A list consisting of the user rows
    """
    batch = []
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        batch.append(row)

        if len(batch) == batch_size:
            yield batch

# ---------------------------------------------------
# Process data in batches and filter out results
# ---------------------------------------------------
def batch_processing(batch_size):
    """Processes each batch to filter out users over the age of 25
    Args:
    	None
    Return:
    	A list consisting of the user aged 25 and above
    """
    for batch in stream_users_in_batches(batch_size):
        filtered_batch = list(filter(lambda record: record["age"] > 25, batch))

        for row in filtered_batch:
            print(row)

    return
