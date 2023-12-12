import sqlite3

# Connect to the SQLite database 'spotify.db'
conn = sqlite3.connect("spotify.db")
# Create a cursor object to interact with the database
cur = conn.cursor()
# Execute an SQL query to select all records from the 'artist' table
cur.execute("SELECT * FROM artist")

# Fetch all the records from the 'artist' table and print each record
for data in cur.fetchall():
    print(data)

# Print blank lines for spacing
print()
print()
print()

# Execute an SQL query to select all records from the 'track' table
cur.execute("SELECT * FROM track")

# Fetch all the records from the 'track' table and print each record
for data in cur.fetchall():
    print(data)