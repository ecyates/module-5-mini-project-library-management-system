from connect_mysql import connect_database
from mysql.connector import Error

class Author:
    '''Creating the Author class, which takes the author's name and biography. 
    The class has the functionality to display the author's information, edit the name 
    and biography and to retrieve the author's name.'''
    def __init__(self, name, biog):
        self.name = name # author's first and last name
        self.biog = biog # author's biography
    
    def display_author(self):
        # Display the author with the following format:
        # author_name
        #   -  biography
        conn = connect_database()
        cursor = conn.cursor()
        print(f'\n\033[1m{self.name}\033[0m')
        print(f" - {self.biog}")
        try: 
            query = "SELECT title, availability FROM Books WHERE author_id = %s"
            author_id, author = get_author_from_name(self.name)
            cursor.execute(query, (author_id, ))
            all_books = cursor.fetchall()
            if all_books != []:
                print(" - Books by Author:")
                for book in all_books:
                    if book[1] == 1:
                        availability = "Available"
                    else:
                        availability = "Not Available"
                    print(f"                   \033[1m'{book[0]}'\033[0m: {availability}")
        except Error as e: 
            print(f"Error: {e}")

    def save_author(self):
        '''This function will save the author to the database.'''
        # Connect to the database
        conn = connect_database()
        cursor = conn.cursor()
        try: 
            # Create the query 
            query = "INSERT INTO Authors (name, biography) VALUES (%s, %s)"
            # Execute the query
            cursor.execute(query, (self.name, self.biog))
            conn.commit()
            return True # If successful, return True
        except Error as e: 
            print(f"Error: {e}")
            return False # If error, return False
        finally: 
            # Disconnect from the database
            cursor.close()
            conn.close()

def get_author_from_name(name):
    '''This function returns the Author(name, biography) from the database using the name to search.'''
    # Connect the database
    conn = connect_database()
    cursor = conn.cursor()
    try: 
        # Create the query
        query = "SELECT * FROM Authors WHERE name = %s"
        # Execute the query 
        cursor.execute(query, (name, ))
        # Fetch the first result
        author = cursor.fetchone()
        # If the author exists, return it in Author form Author(name, biography)
        if author: 
            return author[0], Author(author[1], author[2])
        else:  
            return None, None
    # If the author doesn't exist or for any other errors, return None
    except ValueError: 
        return None, None
    except Error: 
        return None, None
    # Disconnect from database
    finally: 
            cursor.close()
            conn.close()

def get_author_name_from_id(id):
    '''This function retrieves the author's name from the author's id in the database.'''
    # Connect to the database
    conn = connect_database()
    cursor = conn.cursor()
    try: 
        # Create the query
        query = "SELECT name FROM Authors WHERE id = %s"
        # Execute the query
        cursor.execute(query, (id, ))
        # Fetch the author from the database
        author = cursor.fetchone()
        # If the author exists, return just the name 
        if author:
            return author[0]
        # If the author doesn't exist or for any other error, return None
        else:
            return None
    except ValueError: 
        return None
    except Error: 
        return None
    # Disconnect from the database
    finally: 
            cursor.close()
            conn.close()

def display_all_authors():
    '''This function displays all the authors and their biographies in alphabetical order.'''
    # Connect to the database.
    conn = connect_database()
    cursor = conn.cursor()
    try: 
        # Define the query
        query = "SELECT name, biography FROM Authors ORDER BY name ASC"
        # Execute the query
        cursor.execute(query)
        # Fetch all the authors
        all_authors = cursor.fetchall()
        if all_authors != []:
            # Iterate over each author and display them.
            for author in all_authors:
                Author(author[0], author[1]).display_author()
            return True
        else: 
            return False
    # Handle any errors
    except Error as e: 
        print(f"\nError: {e}")
        return False
    # Disconnect from the database
    finally: 
        cursor.close()
        conn.close()

def confirm_author(author_name):
    '''This function takes the user-inputted author name and checks if it already exists and returns the author id 
    from the database. If it doesn't exist, it prompts the user to input a biography and saves it to the authors database, 
    and returns the author id. '''
    # Retrieves author id
    author_id, author = get_author_from_name(author_name)
    # If the author's not on the list, prompt the user for the biography and add the author
    if author_id is None:
        biog = input("\nLooks like this author isn't on our list. Could you please provide a biography below?\n\n")
        if Author(author_name, biog).save_author():
            print(f"\nThe author '{author_name}' was successfully added.")
            # Retrieves new author id
            author_id, author = get_author_from_name(author_name)
        # If it can't save the author, return None
        else: 
            return None
    # Return author id
    return author_id