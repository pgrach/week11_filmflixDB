"""Print all records in  tblfilms in database filmflix.db"""

from connect import * #import everything from the connect.py module

def read_data(): #The purpose of this function is to read and print all the records from the tblfilms table.

    dbCursor.execute("SELECT * FROM tblfilms") #SQL command to prepare the data for retrieval (instruct about what data we want to access)
    i = dbCursor.fetchall() #fetches all the selected records and stores them in the variable i
    for j in i:     # loop through the fetched records stored in i variable and print each in the terminal
        print(j)

if __name__ == "__main__":
    read_data()