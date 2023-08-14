
"""Allows users to add records in  tblfilms in database filmflix.db (CRUD)"""

from connect import * # import everything from the connect.py module

# create a function 
def insert_data():
    # Note: filmID is set to autoincrement, input/data is not required
    #prompt the user to enter information about a film: Title, Year, Rating, Duration, Genre
    filmTitle = input("Enter film title: ")
    while True:
        try: # Data Type Validation
            filmYear = int(input("Enter film year (in YYYY format): "))
            break
        except ValueError:
            print("Please enter a valid year")

    ALLOWED_RATINGS = ("G", "PG", "R", "NC-17", "Not Rated")
    filmRating = ""
    while filmRating not in ALLOWED_RATINGS:
        filmRating = input("Enter film rating (G: General audiences; PG: Parental guidance; R: Restricted): ")
        if filmRating not in ALLOWED_RATINGS:
            print("Invalid rating. Please choose from the provided options.")
        
    while True:
        try:
            filmDuration = int(input("Enter film duration (in mins): "))
            break
        except ValueError:
            print("Please enter a valid number of mins")
    
    filmGenre = input("Enter film genre: ")
    
    dbCursor.execute("INSERT INTO tblfilms (title, yearReleased, rating, duration, genre) VALUES (?,?,?,?,?)", (filmTitle, filmYear, filmRating, filmDuration, filmGenre))
    dbCon.commit() # permanently saves this record to the table in the database

    print(f"{filmTitle} inserted into tblfilms") #confirmation message

if __name__ == "__main__":
    insert_data()