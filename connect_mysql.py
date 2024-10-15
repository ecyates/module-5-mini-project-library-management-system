import mysql.connector
from mysql.connector import Error

def connect_database():
    # Database connection parameters
    db_name = "library_management_db"
    user = "root"
    password = input("Enter password: ")
    host = "localhost"
    try:
        # Attempting to establish a connection
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )
        #Check if the connection is successful
        return conn 
    except Error as e:
        # Handling any connection errors
        print(f"Error: {e}")
        return None
