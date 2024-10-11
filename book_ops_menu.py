from book import Book, display_all_books, get_book_from_title, check_out_book, return_book, validate_date, validate_isbn
from author import confirm_author
from user import get_user
from genre import confirm_genre

def book_menu():
    '''At the Book Operations Menu, we present the user with the following actions: 1) Add a new book,
    2) Borrow a book, 3) Return a book, 4) Search for a book, 5) Display all authors, 6) Back to main menu,
    and take the action the user selects.'''
    while True:
        action = input('''
\033[1mBook Operations Menu:\033[0m\n
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books
6. Back to main menu

Enter menu item (1-6): ''')
        try:
            # 6 = Go Back to Main Menu
            if action == "6":
                break
            # 1 = Add a New Book
            elif action == "1":
                # Prompt the user for necessary information
                success = False
                # ISBN must have 13 digits
                isbn = validate_isbn(input("\nISBN: "))
                if isbn is not None:
                    # Book title has no requirements
                    title = input("\nBook Title: ")
                    # Publication date must be YYYY-MM-DD format
                    publication_date = validate_date(input("\nPublication Date (YYYY-MM-DD): "))
                    if publication_date is not None:
                        # Genre must be on the list or must be added to the list
                        genre = input("\nGenre: ")
                        # Retrieve genre id
                        genre_id = confirm_genre(genre)
                        if genre_id is not None:
                            # Author must be on the list or must be added to the list
                            author_name = input("\nAuthor Name: ")
                            # Retrieve author id
                            author_id = confirm_author(author_name)
                            if author_id is not None:
                                # Create book and save it in the database
                                book = Book(isbn, title, author_id, publication_date, genre_id)
                                if book.save_book():
                                    print(f"\nNew book '{title}' was successfully added!")
                                    success = True
                                else:
                                    print(f"\nThere was an issue adding {title}.")
                            else:
                                print(f"\nThere was an issue with the author '{author_name}'.")
                        else:
                            print(f"\nThere was an issue with the genre '{genre}'.")
                # For any input errors, prompt user to try again
                if success is False: 
                    print('\nPlease try again.')
            # 2 = Check Out Book
            elif action == "2":
                # Prompt the user for the book to check out
                book_title = input("\nBook title to check out: ")
                # Retrieve the book
                book_id, book = get_book_from_title(book_title)
                # If the book can't be found, alert user
                if book is None:
                    print(f"\nThe book '{book_title}' could not be found. Please try again.")
                else:
                    # Only proceed if book is available
                    if book.availability == 1:
                        # Prompt the user's name to check out the book
                        user_name = input("\nUser borrowing the book: ")
                        # Retrieve the user
                        user_id, user, borrowed_books = get_user(user_name)
                        # If the user can't be found, alert user.
                        if user is None:
                            print(f"\nUser '{user_name}' could not be found. Please try again.")
                        else:
                            # Set the book to unavailable and update borrowed books database
                            if check_out_book(user_id, book_id):
                                print(f"\nThe user '{user_name}' successfully checked out '{book_title}'.")
                            else:
                                print("\nThere was a problem check out the book, please try again.")
                    else: # Alert the user if book is unavailable
                        print(f"\nThe book '{book_title}' is not available. Please try again.")
            # 3 = Return Book
            elif action == "3":
                # Prompt user for and retrieve book title and user returning the book
                book_title = input("\nBook title to return: ")
                # Retrieve the book
                book_id, book = get_book_from_title(book_title)
                # If the book can't be found, alert user
                if book is None:
                    print(f"\nThe book '{book_title}' could not be found. Please try again.")
                else:
                    # Only proceed if book is available
                    if book.availability == 0:
                        # Return book and update borrowed books database
                        if return_book(book_id):
                            print(f"\nThe book '{book_title}' was successfully returned!")
                    else: 
                        print(f"\nThe book '{book_title}' is not currently checked out.")
            # 4 = Search For a Book
            elif action == "4":
                # Prompt user for book title
                book_title = input("\nBook title to search for: ")
                # Retrieve the book
                book_id, book = get_book_from_title(book_title)
                # If successful, display book
                if book:
                    book.display_book()
                # Otherwise, alert user
                else:
                    print(f"\nThe book '{book_title}' not found.")
            # 5 = Display all books
            elif action == "5":
                success = display_all_books()
                if success is False: 
                    print("\nThere are no books in the database.")
            else: # Handle any input errors 
                raise ValueError()
        except ValueError:
            print(f"\nInvalid input: {action}. Please enter a number between 1 and 6.")
        except Exception as e:
            print(f"\nAn error occurred: {e}")