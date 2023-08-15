"""Allows users to delete records in  tblfilms in database filmflix.db (CRUD)"""

from connect import *

# create a function
def delete_data():
    # use primary key to delete a record 
    idField = input("Enter the filmID of the record to be deleted: ")

    #DELETE FROM tblfilms WHERE filmID = 1/2/3/4....
    dbCursor.execute(f"DELETE FROM tblfilms WHERE filmID = {idField}")
    dbCon.commit()
    print(f"Record {idField} deleted from tblfilms. ")

if __name__ == "__main__":
    delete_data()

# Could potentially expand it more with:
# Confirm with the user that they truly want to delete the specified record.
# Provide a check to ensure the entered filmID is a valid integer.
# Handle situations where the provided filmID might not exist in the database.
