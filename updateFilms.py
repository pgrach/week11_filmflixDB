"""Allows users to update records in  tblfilms in database filmflix.db (CRUD)"""

from connect import *

# create a function 
def update_data():
    ALLOWED_FIELDS = ["title", "yearReleased", "rating", "duration", "genre"]
    idField = input("Enter the filmID of the record to be updated: ") #use primary key to update a record 

    #field to be updated: title, yearReleased, rating, duration, genre
    fieldName = ""
    while fieldName not in ALLOWED_FIELDS:
        fieldName = input("Enter one of field names (title, yearReleased, rating, duration, genre): ")
        if fieldName not in ALLOWED_FIELDS:
            print("Invalid field name. Please select from the allowed options.")

    # field Value: ask user for the value for the field to be updated
    fieldValue = input(f"Enter the value for {fieldName} field: ") # potentially can expand this with while Ttru to handle data type validation

    print(fieldValue)

    # using parameterized queries to prevent SQL injection
    dbCursor.execute(f"UPDATE tblfilms SET {fieldName} = ? WHERE filmID = ?", (fieldValue, idField))
    dbCon.commit()
    print(f"Record {idField} updated in the tblfilms. ")

if __name__ == "__main__":
    update_data()# call or invoke the subroutine or function