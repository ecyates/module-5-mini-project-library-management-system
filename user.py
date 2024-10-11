from book import Book
from connect_mysql import connect_database
from mysql.connector import Error
from datetime import date, timedelta

class User:
    '''Creating the User class, which takes the user's name and unique library ID  (LIB######). 
    The class has the functionality to add a borrowed book to the borrowed book list, 
    remove a borrowed book from the list, and display the user's information in a user-friendly way.'''
    def __init__(self, name, library_id):
        self.name = name # User's first and last name
        self.library_id = self.validate_id(library_id) # LIB######

    def validate_id(self, library_id):
        # Split string into LIB and the digits
        lib, num = library_id[:3], library_id[3:]
        if isinstance(library_id, str) and lib == "LIB" and num.isdigit() and len(num) == 6:
            return library_id
        else:
            raise ValueError("Library ID must be 'LIB' plus exactly 6 digits.")

    def display_user(self, borrowed_books):
        '''This function takes the use and a list of borrowed books and Displays user in a user-friend format, as follows: 
        LIB######: User Name
            No Books Checked Out.
        OR
            Books Checked Out:
            - Book Title by Book Author'''
        print(f"\n{self.library_id}: \033[1m{self.name}\033[0m")
        if borrowed_books == []:
            print("    No Books Checked Out.")
        else:
            print("  Books Checked Out:")
            for book in borrowed_books:
                print(f"     - '{book[0]}', Due Date: {book[1]}")

    def save_user(self):
        '''This function saves the user in the users database with its name and library id.'''
        # Connect to the database
        conn = connect_database()   
        cursor = conn.cursor()
        try: 
            # Query to insert new user
            query = "INSERT INTO Users (name, library_id) VALUES (%s, %s)"
            # Execute the query
            cursor.execute(query, (self.name, self.library_id))
            conn.commit()
            # Return True if successful
            return True
        # Handle any errors and return False
        except Error as e: 
            print(f"Error: {e}")
            return False
        # Disconnect from the database
        finally: 
            cursor.close()
            conn.close()

def get_user(name):
    '''This function returns the user id, the User(name, library_id) object, and borrowed books using the name.'''
    # Connect to the database
    conn = connect_database()   
    cursor = conn.cursor()
    try: 
        # Query to retrieve the user information
        query1 = "SELECT id, name, library_id FROM Users WHERE name = %s"
        # Execute query
        cursor.execute(query1, (name, ))
        # Fetch the user
        user = cursor.fetchone()
        # Query to retrieve the list of borrowed books for this user
        query2 = "SELECT book.title, bb.return_date FROM Users u, Books book, BorrowedBooks bb WHERE book.id = bb.book_id AND u.id = bb.user_id AND u.name = %s"
        # Execute query
        cursor.execute(query2, (name, ))
        # Fetch the borrowed books list
        borrowed_books = cursor.fetchall()
        if user:
            user_id = user[0]
            user = User(user[1], user[2])
            return user_id, user, borrowed_books
        else: 
            raise ValueError()
    # Handles errors and return None, None, None
    except ValueError: 
        return None, None, None
    except Error: 
        print(f"\nError: {e}")
        return None, None, None
    # Disconnect from database
    finally: 
        cursor.close()
        conn.close()

def display_all_users():
    '''This function displays all the users and their borrowed books.'''
    # Connect to database. 
    conn = connect_database()   
    cursor = conn.cursor()
    try: 
        # Query to retrieve all users in alphabetical order
        query1 = "SELECT * FROM Users ORDER BY name ASC"
        # Execute query
        cursor.execute(query1)
        # Fetch users
        all_users = cursor.fetchall()
        if all_users != []:
            # Iterate over each user
            for user in all_users:
                # Query to retrieve the borrowed books for each user
                query2 = "SELECT b.title, bb.return_date FROM Books b, BorrowedBooks bb WHERE bb.book_id = b.id AND bb.user_id = %s"
                # Execute query
                cursor.execute(query2, (user[0],))
                # Fetch borrowed books
                borrowed_books = cursor.fetchall()
                # Display user
                User(user[1], user[2]).display_user(borrowed_books)
            return True
        else:
            return False
    # Handle errors
    except Error as e: 
        print(f"\nError: {e}")
        return False
    # Disconnect from the database
    finally: 
        cursor.close()
        conn.close()
