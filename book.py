from author import Author, get_author_name_from_id
from connect_mysql import connect_database
from genre import get_genre_from_id, get_genre_id_from_name
from mysql.connector import Error
import re
from datetime import date, timedelta

class Book:
    '''Creating the Book class which takes the book's ISBN (13 digits), title, author id (int, which corresponds to the 
    id in the authors database), publication date (YYYY-MM-DD), genre id (int, which corresponds to the id in the 
    genres database), and is_available (0=False, 1=True). The class has the functionality to validate the attributes, 
    check out a book (change availability to False), return a book (change availability to True), 
    and display the book in a user-friendly format.'''
    def __init__(self, isbn, title, author_id, publication_date, genre_id, availability=1):
        self.title = title # no requirements
        self.isbn = isbn # 13 digits
        self.author_id = author_id # INT
        self.publication_date = publication_date # YYYY-MM-DD
        self.genre_id = genre_id # INT
        self.availability = availability # 0 or 1

    def display_book(self):
        ''' Display the book with the following format: 
        Title: book_title
        ISBN: isbn
        Author: author name
        Publication: publication_date
        Genre: genre
        Status: Available/Not Available'''
        # Retrieve the author's name
        author_name = get_author_name_from_id(self.author_id)
        # Retrieve the genre
        genre = get_genre_from_id(self.genre_id)
        # Display the book with it's attributes
        print(f"\n\033[1mTitle: {self.title}\033[0m")
        print(f"  ISBN: {self.isbn}\n  Author: {author_name}\n  Publication Date: {self.publication_date}\n  Genre: {genre}")
        print("  Status:", "Available" if (self.availability == 1) else "Not Available")
        
    def save_book(self):
        '''This function saves the book to the books database.'''
        # Connects to the database
        conn = connect_database()
        cursor = conn.cursor()
        try:
            # Create the query
            query = "INSERT INTO Books (title, isbn, author_id, publication_date, genre_id, availability) VALUES (%s,%s,%s,%s,%s,%s)"
            # Execute the query
            cursor.execute(query, (self.title, self.isbn, self.author_id, self.publication_date, self.genre_id, self.availability))
            conn.commit()
            return True # Returns True if successful
        except Error as e: 
            print(f"Error: {e}")
            return False # Returns False if an error occurs
        # Disconnects from the database
        finally: 
            cursor.close()
            conn.close()

def display_all_books():
    '''This function displays all the books in the database in alphabetical order by title.'''
    # Connects to the database
    conn = connect_database()
    cursor = conn.cursor()
    try: 
        # Creates the query
        query = "SELECT isbn, title, author_id, publication_date, genre_id, availability FROM Books ORDER BY title ASC"
        # Executes the query
        cursor.execute(query)
        # Fetches all the books in the database
        all_books = cursor.fetchall()
        if all_books != []:
            # Iterates over the books and displays each book
            for book in all_books:
                Book(book[0], book[1], book[2], str(book[3]), book[4], book[5]).display_book()
            return True
        else:
            return False
    # Handles any errors
    except Error as e: 
        print(f"\nError: {e}")
        return False
    # Disconnects from the database
    finally: 
        cursor.close()
        conn.close()

def get_book_from_title(title):
    '''This function returns the book id and the Book object from the database using the title to search'''
    # Connects to the database
    conn = connect_database()
    cursor = conn.cursor()
    try: 
        # Creates the query
        query = "SELECT id, isbn, title, author_id, publication_date, genre_id, availability FROM Books WHERE title = %s"
        # Executes the query
        cursor.execute(query, (title, ))
        # Fetch the first instance of the title.
        book = cursor.fetchone()
        # If the book exists, return the book id and the Book object (isbn, title, author_id, publication_date, genre_id, availability)
        if book:
            return book[0], Book(book[1], book[2], book[3], str(book[4]), book[5], book[6])
        # If the book doesn't exist or for any errors, return None, None
        else: 
            return None, None
    except ValueError: 
        return None, None
    except Error: 
        return None, None
    # Disconnect from the database
    finally: 
            cursor.close()
            conn.close()

def check_out_book(user_id, book_id):
    '''This function takes the book id of the book to be checked out and the user id of the user that is 
    checking out the book and sets the availability to the book to unavailable (0) in the database and adds a 
    new borrowed book to the database with the user id and book id. With the borrowed date set to today 
    and the return date set to two weeks from today.'''
    # Connect to the database
    conn = connect_database()
    cursor = conn.cursor()
    try:     
        # Query to set the availability to 0
        query1 = "UPDATE Books SET availability = 0 WHERE id = %s"
        # Execute the query
        cursor.execute(query1, (book_id, ))
        # Borrow date is set to today
        borrow_date = date.today()
        # Return date is set for two weeks from today
        return_date = borrow_date + timedelta(weeks=2)
        # Query to add borrowed book with user id, book id, borrow date and return date
        query2 = "INSERT INTO BorrowedBooks (user_id, book_id, borrow_date, return_date) VALUES(%s,%s,%s,%s)"
        # Execute the query
        cursor.execute(query2, (user_id, book_id, borrow_date, return_date))
        conn.commit()
        return True # Return True to show action could be done
    # Handle any errors
    except Error as e:
        print(f"Error: {e}")
        return False # Otherwise, return False
    # Disconnect from the database
    finally: 
        cursor.close()
        conn.close()

def return_book(book_id):
    '''This function takes the book idea and sets it's availability to available (1) and deletes the 
    borrowed book instance in the database.'''
    # Connect to the database
    conn = connect_database()
    cursor = conn.cursor()
    try:     
        # Query to set availability to 1
        query1 = "UPDATE Books SET availability = 1 WHERE id = %s"
        # Execute the query
        cursor.execute(query1, (book_id, ))
        # Query to delete the borrowed book instance
        query2 = "DELETE FROM BorrowedBooks WHERE book_id = %s"
        # Execute the query
        cursor.execute(query2, (book_id,))
        conn.commit()
        return True # Return True to show action could be done
    # Handle any errors
    except Error as e:
        print(f"Error: {e}")
        return False # Otherwise, return False
    # Disconnect the database
    finally: 
        cursor.close()
        conn.close()

def validate_isbn(isbn):
    # ISBN must be a string of 13 digits.
    if isinstance(isbn, str) and len(isbn) == 13 and isbn.isdigit():
        return isbn
    else:
        print(f"\nInvalid input: {isbn}. ISBN must be a string of exactly 13 digits.")
        return None

def validate_ids(id):
    # Author ids and genre ids must be an int
    if isinstance(id, int):
        return id
    else:
        print(f"\nInvalid input {id}. Author and Genre IDs must be integers.")
        return None
    
def validate_date(date):
    # Year must be in the format: YYYY-MM-DD
    if re.search(r'\d{4}-\d{2}-\d{2}', date):
        return date
    else:
        print(f"\nInvalid input {date}. Publication date must have the following format: YYYY-MM-DD.")
        return None

def validate_availability(availability):
    # availability must 0 or 1
    if availability == 0 or availability == 1:
        return availability
    else:
        print(f"\nInvalid input {availability}. Availability must be 0 or 1.")
        return None