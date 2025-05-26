#!/usr/bin/env python3

import seed

connect = seed.connect_db()

if connect:
    seed.create_database(connect)
    connect.close()

    connection = seed.connect_to_prodev()

    if connection:
        seed.create_table(connection)
        seed.insert_data(connection, 'user_data.csv')
        cursor = connection.cursor()
        cursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'ALX_prodev';")
        result = cursor.fetchone()
        if result:
            print("Database ALX_prodev is present\n")
        cursor.execute("SELECT * FROM user_data LIMIT 5;")
        rows = cursor.fetchall()
        print(rows)
        cursor.close()

    if connection:
        print("\nLazy Evaluation with Generators\n")
        seed.create_table(connection)
        seed.insert_data(connection, 'user_data.csv')

        for row in seed.stream_user_data(connection):
            print(row)
            break

        connection.close()
