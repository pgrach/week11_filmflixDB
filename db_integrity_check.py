import sqlite3

# Connect to the database
conn = sqlite3.connect("filmflix.db")
cursor = conn.cursor()

# Run the integrity check
cursor.execute("PRAGMA integrity_check;")
result = cursor.fetchone()

# Print the result
print(result[0])

# Close the connection
conn.close()