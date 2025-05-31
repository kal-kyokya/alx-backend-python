# Context Managers and Asynchronous programming in python
By completing the listed below tasks, I gain insights of the inner workings of class based context manager for Database connection, reusable query context manager and concurrent asynchronous Database queries.

## Tasks

### Custom class based context manager for Database connection

#### Objective
Create a class based context manager to handle opening and closing database connections automatically

#### Instructions
* Write a class custom context manager ```DatabaseConnection``` using the ```__enter__``` and the ```__exit__``` methods
* Use the context manager with the ```with``` statement to be able to perform the query ```SELECT * FROM users```. Print the results from the query.
 
### Reusable Query Context Manager

#### Objective
Create a reusable context manager that takes a query as input and executes it, managing both connection and the query execution

#### Instructions
* Implement a class based custom context manager ```ExecuteQuery``` that takes the query: ```”SELECT * FROM users WHERE age > ?”``` and the parameter ```25``` and returns the result of the query
* Ensure to use the ```__enter__()``` and the ```__exit__()``` methods
 
### Concurrent Asynchronous Database Queries

#### Objective
Run multiple database queries concurrently using asyncio.gather.

#### Instructions
* Use the ```aiosqlite``` library to interact with SQLite asynchronously.
* Write two asynchronous functions: ```async_fetch_users()``` and ```async_fetch_older_users()``` that fetches all users and users older than 40 respectively.
* Use the ```asyncio.gather()``` to execute both queries concurrently.
* Use ```asyncio.run(fetch_concurrently())``` to run the concurrent fetch
