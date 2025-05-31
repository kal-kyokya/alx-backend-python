#!/usr/bin/env python3
"""
'3-concurrent' runs multiple database queries concurrently using asyncio.gather
"""
import os
import asyncio
import aiosqlite
from dotenv import load_dotenv


load_dotenv()

# -----------------------------------
# MySQl and Database credentials
# -----------------------------------
DB_USER = os.getenv("MYSQL_USER")
DB_HOST = os.getenv("MYSQL_HOST")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("MYSQL_DB_NAME")
DB_TABLE_NAME = os.getenv("MYSQL_DB_TABLE_NAME")

async def async_fetch_users():
    """Fetches all users from the database
    Args:
    	None:
    Return:
    	A list of all user records as tuples
    """

    async with aisqlite.connect(DB_NAME) as db:
        cursor = await db.execute(f"SELECT * FROM {DB_TABLE_NAME}")
        users = await cursor.fetchall()
        await cursor.close()
        return users

async def async_fetch_older_users():
    """Fetches users older than 40 from the database
    Args:
    	None
    Return:
    	A list of user records where age > 40
    """

    async with aisqlite.connect(DB_NAME) as db:
        cursor = await db.execute(f"SELECT * FROM {DB_TABLE_NAME} WHERE age >40")
        older_users = await cursor.fetchall()
        await cursor.close()
        return older_users

async def fetch_concurrently():
    """Fetches all users and users older than 40 concurrently
    Args:
    	None
    Return:
    	A tuple of two lists:
    		- All users
    		- Users older than 40
    """

    return await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

if __name__ == "__main__":
    all_users, older_users = asyncio.run(fetch_concurrently())
    print("All users:")
    for user in all_users:
        print(user)
    print("")

    print("Older users:")
    for older_user in older_users:
        print(older_user)
    print("")
