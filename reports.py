"""This is a Reports application demonstrating 
different techniques of writing sql commands and printing reports"""

from connect import *

# create a function to read records in the tblfilms table 
def print_all():
    # select all record in the tblfilms table
    dbCursor.execute("SELECT * FROM tblfilms ORDER BY filmID DESC")

    i = dbCursor.fetchall() #fetches all the selected records and stores them in the variable i
    for j in i:     # loop through the fetched records stored in i variable and print each in the terminal
        print(j)

def search_genre():
    genreValue =  input("Enter the genre you want to search for: ").title()
    dbCursor.execute(f"SELECT * FROM tblfilms WHERE genre = '{genreValue}' ")

    i = dbCursor.fetchall()
    for j in i:
       print(j)

def search_year():
    yearValue =  input("Enter the year you want to search for: ")
    dbCursor.execute(f"SELECT * FROM tblfilms WHERE yearReleased = '{yearValue}' ")

    i = dbCursor.fetchall()
    for j in i:
       print(j)

def search_rating():
    ratingValue =  input("Enter film rating you are looking for (G: General audiences; PG: Parental guidance; R: Restricted): ")
    dbCursor.execute(f"SELECT * FROM tblfilms WHERE rating = '{ratingValue}' ")

    i = dbCursor.fetchall()
    for j in i:
       print(j)

if __name__ == "__main__":
    # reports()
    search_rating()


# injecting user inputs directly into SQL statements poses a security risk 
# due to potential SQL injection attacks. 
# In future we could use parameterized queries to ensure that the user input is handled safely.

