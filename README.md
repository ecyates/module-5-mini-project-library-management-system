# Module 4 - Mini-Project - Library Management System
Author: Elizabeth Yates

## Introduction

In this project, I have applied OOP principles in Python to develop an advanced Library Management System and incorporated a MySQL database. This command-line-based application is designed to streamline the management of books and resources within a library. The objective was to create a robust system that allows users to browse, borrow, return, and explore a collection of books.

## User Interface and Menus:

#### Welcome to the Library Management System!

    Main Menu:
    1. Book Operations
    2. User Operations
    3. Author Operations
    4. Quit

    (1) Book Operations:
        1. Add a new book
        2. Borrow a book
        3. Return a book
        4. Search for a book
        5. Display all books
        6. Back to main menu

    (2) User Operations:
        1. Add a new user
        2. View user details
        3. Display all users
        4. Back to main menu

    (3) Author Operations:
        1. Add a new author
        2. View author details
        3. Display all authors
        4. Back to main menu

## Class Structure: 

This library management system includes the following class structures:

- Book (book.py): A class representing individual books with attributes such as isbn (#############), title, author_id,  genre_id, publication date (YYYY-MM-DD), and availability status (0/1).This class functionality includes validating inputs, retrieving a book from the Books database, saving a book to the Books database, checking a book out (updating its availability and adding a book to the BorrowedBooks database), returning a book (updating availability and removing a book to the BorrowedBooks database), and displaying the book in a user-friendly format.
- User (user.py): A class to represent library users with attributes including name and library ID. This class functionality includes validating the library ID (LIB######), displaying the user, retrieving a user from the Users database, saving a user to the Users database, .
- Author (author.py): A class representing book authors with attributes including name and biography. This class functionality includes retrieving an author from the Authors database, saving an author to the Authors database, and displaying the author in a user-friendly format. 
- Genre (genre.py): While not a class, genre is an attribute for the Books class. This file contains functionality to retrieve a genre from the Genres database, save a genre to the Genres database, and display genres. 

## Database Structure: 

This library management system includes the following tables in the MySQL database: 

- Books table: 
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    isbn VARCHAR(13) NOT NULL,
    publication_date DATE,
    availability BOOLEAN DEFAULT 1,
	author_id INT,
    genre_id INT,
    FOREIGN KEY (author_id) REFERENCES Authors(id)
    FOREIGN KEY (genre_id) REFERENCES Genres(id)
- Users table: 
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    library_id VARCHAR(10) NOT NULL UNIQUE
- Authors table: 
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
- Genres table: 
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
- BorrowedBooks table: 
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (book_id) REFERENCES Books(id)

## Main Menu (main.py)

- Upon opening, the library management system will display the menu items (1 - Book Operations (book_ops_menu.py), 2 - User Operations (user_ops_menu.py), 3 - Author Operations (author_ops_menu.py), and 4 - Quit). For an invalid input, it will display an error and prompt the user to try again. 
- Selecting any 1-3 option will take the user to the menu selected. 
- Selecting 4 will prompt the system to quit. 

## Book Operations (book_ops_menu.py)

- This menu provides operations options for adding, borrowing, returning, and viewing books in the system. 
- Each menu option will run and then bring the user back to this menu.
- If the user provides an invalid input (any input other than a number between 1 and 6), then it will throw an error and prompt the user again. Selecting 6 will take the user back to the main menu.

### 1 - Add a book

- This menu option will prompt the user for the book details (isbn, book title, author name, publication year, and genre). 
- If the isbn is invalid (must be 13 digits) or publication year is invalid (must be 4 digits), it will alert the user. 
- If the author does not exist, it will prompt the user for the biography of the author and add it to the list as well. 
- If the genre does not exist, it will display a list of the current genres and ask the user to either select a current genre o confirm they want to add that genre to the list. 
- Then it will add the book to the Books database.

### 2 - Borrow a book

- This menu option will prompt the user for the book title they'd like to borrow and the name of the user doing the borrowing. 
- Both the user and book must exist in the Books databases, otherwise it will raise an error. 
- If they do both exist, the system will check out the book (set status to "Not Available") and add the book to the list of borrowed books by the user in the Books database.

### 3 - Return a book

- This menu option will prompt the user for the book title they'd like to return.
- The book must be set to "Not Available," otherwise it will raise an error.
- If it is, the system will return the book (set status to "Available") and remove the book from the list of borrowed books by the user in the Books database.

### 4 - Search for a book

- This menu option will prompt the user for the book title they'd like to find and will search the Books database for the book. 
- If it finds the book, it will display it in a user-friendly format, including its isbn, title, author name, publication date, genre, and availability. 
- If it did not find the book, it will inform the user, and bring the user back to the menu.

### 5 - Display all books

- This menu option will display all the books in the Books database, including their isbn, title, author name, publication date, genre, and availability. If there are no books in the Books database, it will inform the user. 

## User Operations (user_ops_menu.py)

- This menu provides options for adding and viewing users in the system. 
- Each menu option will run and then bring the user back to this menu.
- If the user provides an invalid input (any input other than a number between 1 and 4), then it will throw an error and prompt the user again. Selecting 4 will take the user back to the main menu.

### 1 - Add a user

- This menu option will prompt the user for the user name and library ID.
- If the user name already exists, it will inform the user. 
- If the library ID is not valid (must be LIB and 6 digits), it will inform the user.
- Otherwise, it will add the user to the Users database.

### 2 - View user details

- This menu option will prompt the user for the user name they'd like to view. 
- If the user does not exist, it will inform the user. 
- Otherwise, it will display the user's details, including name, library ID, and list of borrowed books. 

### 3 - Display all users

- This menu option will display all users with each user's details (name, library ID, and list of borrowed books) in a user-friendly format.

## Author Operations (author_ops_menu.py)

- This menu provides options for adding and viewing authors in the system. 
- Each menu option will run and then bring the user back to this menu.
- If the user provides an invalid input (any input other than a number between 1 and 4), then it will throw an error and prompt the user again. Selecting 4 will take the user back to the main menu.

### 1 - Add an author

- This menu option will prompt the user for the author's name and bibliography.
- If the author already exists, it will inform the user. 
- Otherwise, it will add the author to the Authors database.

### 2 - View author details

- This menu option will prompt the user for the author they'd like to view. 
- If the author does not exist, it will inform the user. 
- Otherwise, it will display the author's details, including name and bibliography. 

### 3 - Display all authors

- This menu option will display all authors with each author's details (name and bibliography) in a user-friendly format.
  
  
*This code can be found in this repository:*
*https://github.com/ecyates/module-5-mini-project-library-management-system.git*