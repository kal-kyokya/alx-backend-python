import sqlite3
import functools

#### decorator to lof SQL queries

def log_queries(func):
    """Logs database queries executed by the 'decorated' function
    Args:
    	func: The function to be decorated
    Return:
    	A 'wrapper' function adding logging functionality to the decorated
    """
    def wrapper(*args, **kwargs):
        """A wrapper function adding logging functionality to the decorated
        Args:
        	args: An arbitrary number of positional arguments.
        	kwargs: An arbitrary number of keyword arguments.
        Return:
        	None
        """
        print("The first query executed was: '{}'\n".format(kwargs['query1']))
        time.sleep(5)
        func(**kwargs)

    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
