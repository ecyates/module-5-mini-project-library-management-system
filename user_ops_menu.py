#from user import User
#from user import get_user, display_all_users
from user import User
from user import get_user
from user import display_all_users


def user_menu():
    '''At the User Operations Menu, we present the user with the following actions: 1) Add a new user, 
    2) View user details, 3) Display all users, 4) Back to main menu, and take the action the user selects.'''
    while True:
        action = input('''
\033[1mUser Operations Menu:\033[0m\n
1. Add a new user
2. View user details
3. Display all users
4. Back to main menu
    
Enter menu item (1-4): ''')
        try:
            # 4 = Go Back to Main Menu
            if action == "4":
                break
            # 1 = Add a New User
            elif action == "1":
                # Prompt user for name and library ID
                user_name, library_id, = input("\nName: "), input("Library ID (LIB######): ")
                user_id, user, borrowed_books = get_user(user_name) # Check that the user name doesn't already exist
                if user is None:
                    if User(user_name, library_id).save_user(): # Add user to database
                        print(f"\nUser '{user_name}' successfully added.") # Alert that it was successful
                # Otherwise, alert user that the user already exists
                else: 
                    print(f"\nLooks like the user '{user_name}' already exists:")
                    user.display_user(borrowed_books)
            # 2 = View User Details
            elif action == "2":
                # Prompt user for name
                user_name = input("\nUser to view: ")
                user_id, user, borrowed_books = get_user(user_name) # Retrieve the user
                if user:
                    user.display_user(borrowed_books) # If the user exists, display user
                else:
                    print(f"\nUser '{user_name}' does not exist.") # If not, alert user
            # 3 = Display All Users
            elif action == "3":
                success = display_all_users()
                if success is False: 
                    print("\nThere are no users in the database.")
            else:
                raise IndexError()
        except IndexError:
            print(f"\nInvalid menu option: {action}. Please enter a number between 1 and 4.")
        except ValueError as ve: 
            print(f"\nValue error: {ve}")            
        except Exception as e:
            print(f"\nAn error occurred: {e}")
