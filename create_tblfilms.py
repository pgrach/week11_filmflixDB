from connect import * #importing connect.py module 

dbCursor.execute("""
CREATE TABLE "tblfilms" (
"filmID" INTEGER NOT NULL UNIQUE, 
"title" TEXT, 
"yearReleased" INTEGER,
"rating" TEXT,
"duration" INTEGER,
"genre"TEXT,
PRIMARY KEY (filmID AUTOINCREMENT)
)""")