from author import Author, get_author_from_name, display_all_authors

def author_menu():
    '''At the Author Operations Menu, we present the user with the following actions: 1) Add a new author, 
    2) View author details, 3) Display all authors, 4) Back to main menu, and take the action the user selects.'''
    while True:
        action = input('''
\033[1mAuthor Operations Menu:\033[0m\n
1. Add a new author
2. View author details
3. Display all authors
4. Back to main menu
    
Enter menu item (1-4): ''')
        try:
            # 4 = Go Back to Main Menu
            if action == "4":
                break
            # 1 = Add a New Author
            elif action == "1":
                # Prompt user for author's name and biography
                author_name, biog, = input("\nAuthor's Name: "), input("Biography: ")
                # Search to make sure the author isn't already on the list
                author_id, author = get_author_from_name(author_name)
                if author is None:
                    # If it's not on the list, add author to the database
                    author = Author(author_name, biog)
                    if author.save_author():
                        print(f"\nAuthor '{author_name}' successfully added.")
                else: 
                    # If the author already exists, alert user and display author
                    print(f"\nLooks like the author '{author_name}' already exists:")
                    author.display_author()
            # 2 = View Author Details
            elif action == "2":
                # Prompt user for author to view
                author_name = input("\nAuthor to view: ")
                # Retrieve author
                author_id, author = get_author_from_name(author_name)
                # If the author exists, display author
                if author:
                    author.display_author()
                # Otherwise, alert user
                else:
                    print(f"\nAuthor '{author_name}' does not exist.")
            # 3 = Display All Authors
            elif action == "3":
                success = display_all_authors()
                if success is False:
                    print("\nThere are no authors in the database.")
            else: # Handle any other inputs
                raise ValueError()
        except ValueError:
            print(f"\nInvalid menu option: {action}. Please enter a number between 1 and 4.")            
        except Exception as e:
            print(f"\nAn error occurred: {e}")