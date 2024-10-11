from author_ops_menu import author_menu
from book_ops_menu import book_menu
from user_ops_menu import user_menu

def main():
    '''In the main menu, we open and instantiate the library, bring in the lists of books and users from our saved databases,
    and present the menu options: 1) Book Operations, 2) User Operations, 3) Author Operations, and 4) Quit, and move to the next menu as selected. '''

    # Welcome user and present the menu options
    print("\nWelcome to the Library Management System!")

    while True:
        menu = input('''
\033[1mMain Menu:\033[0m\n
1. Book Operations
2. User Operations
3. Author Operations
4. Quit
        
Enter menu item (1-4): ''')
        try:
            # 4 = Quit
            if menu == "4":
                break
            # 1 = Go to Book Operations Menu
            elif menu == "1":
                book_menu()
            # 2 = Go to User Operations Menu
            elif menu == "2":
                user_menu()
            # 3 = Go to Author Operations Menu
            elif menu == "3":
                author_menu()
            # Else, raise error
            else:
                raise ValueError()
        except ValueError:
            print(f"\nInvalid menu option: {menu}. Please enter a number between 1 and 4.")
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
