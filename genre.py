from mysql.connector import Error
from connect_mysql import connect_database

def get_genre_from_id(genre_id):
    '''This function returns the genre name given the genre id.'''
    # Connect to the database
    conn = connect_database()
    cursor = conn.cursor()
    try: 
        # Query to fetch the name from the genre database using the id
        query = "SELECT name FROM Genres WHERE id = %s"
        # Execute query 
        cursor.execute(query, (genre_id, ))
        # Fetch genre
        genre = cursor.fetchone()
        # If genre exists, return the genre name
        if genre:
            return genre[0]
        # If it doesn't exist or for any other errors, return None
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

def get_genre_id_from_name(genre):
    '''This function returns the genre id given the genre name.'''
    # Connect to the database
    conn = connect_database()
    cursor = conn.cursor()
    try: 
        # Query to retrieve the genre id given the name
        query = "SELECT id FROM Genres WHERE name = %s"
        # Execute the query
        cursor.execute(query, (genre, ))
        # Fetch the genre id
        genre_id = cursor.fetchone()
        # If it exists, return the genre id
        if genre_id:
            return genre_id[0]
        # If it doesn't exist or for any other errors, return None
        else: 
            return None
    except ValueError: 
        return None
    except Error: 
        return None
    # Disconnect from the databases
    finally: 
        cursor.close()
        conn.close()

def display_all_genres():
    ''''This function displays all the genres in a numbered alphabetical list and returns a dictionary 
    where the number is the key to each genre.'''
    # Connect to the database
    conn = connect_database()
    cursor = conn.cursor()
    try: 
        # Query to retrieve all the genres in alphabetical order
        query = "SELECT id, name FROM Genres ORDER BY name ASC"
        # Execute the query 
        cursor.execute(query)
        # Fetch the genres
        all_genres = cursor.fetchall()
        # Initiate the dictionary
        genre_list = {}
        if all_genres != []:
            # Iterate over the genres
            for i, genre in enumerate(all_genres):
                # Display #. Genre
                print(f"{i+1}. {genre[1]}")
                # Add where the number is the key to (genre_id, genre_name)
                genre_list[i] = (genre[0], genre[1])
            
            # Return dictionary
            return genre_list
        else:
            return None
    # Handle any errors and return None
    except Error as e: 
        print(f"\nError: {e}")
        return None
    # Disconnect from the database
    finally: 
        cursor.close()
        conn.close()

def save_genre(genre):
    '''This function saves the genre in the genres database.'''
    # Connect to the database
    conn = connect_database()
    cursor = conn.cursor()
    try:
        # Query to insert the new genre
        query = "INSERT INTO Genres (name) VALUES (%s)"
        # Execute the query
        cursor.execute(query, (genre, ))
        conn.commit()
        # Return True to show success
        return True
    # Handle any errors and return False
    except Error as e: 
        print(f"Error: {e}")
        return False
    # Disconnect from the databases
    finally: 
        cursor.close()
        conn.close()
        
def confirm_genre(genre):
    '''This function takes the genre given by the user and checks if it is already in the database. If it is in the database
    it will return the genre id. If it not in the list, the function will display all the genres and ask if the user wants 
    to use one of the provided genres. If yes, the user will pick a number that corresponds to the genre. If no, the function
    will add the genre to the list and return the new genre's id.'''
    try: 
        # Attempt to retrieve the genre id
        genre_id = get_genre_id_from_name(genre)
        # If the genre is not in the list
        if genre_id is None:
            # Prompt the user to choose one from the list (yes) or to save their genre (no)
            print(f"\nLooks like '{genre}' isn't on our list: \n")
            all_genres = display_all_genres()
            add_genre = input("\nWould you like to use a genre from the list (yes/no)? ").lower()
            # If yes, ask for the number to choose from the list
            if add_genre == "yes":
                genre_num = int(input("\nPlease type the number of the genre you'd like to use from the list: "))
                if 0 < genre_num <= len(all_genres):
                    # Retrieve the genre id
                    genre_id = all_genres[genre_num-1][0]
            # If no, save the genre provided and retrieve the new genre id
            elif add_genre == "no":
                if save_genre(genre):
                    print(f"\nGreat, you've added '{genre}' to the list.")
                    genre_id = get_genre_id_from_name(genre)
                else: 
                    raise Error()
            else: 
                raise ValueError()
        # Return the genre id
        return genre_id
    # Handle any errors and return None
    except ValueError: 
        return None
    except Error as e: 
        print(f"\nError: {e}")
        return None
