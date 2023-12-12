
# Define a function to create database tables
def createtables(conn, cur):
    # Create the 'artist' table with artist_id as PRIMARY KEY and other fields
    cur.execute("CREATE TABLE IF NOT EXISTS artist (artist_id TEXT PRIMARY KEY, name TEXT, followers INT, popularity INT, genres TEXT)")
    # Create the 'track' table with artist_id, track_name, and track_popularity fields
    cur.execute("CREATE TABLE IF NOT EXISTS track (artist_id TEXT, track_name TEXT, track_popularity INT)")
    # Commit the changes to the database
    conn.commit()
# Define a function to drop existing database tables   
def droptables(conn, cur):

    # Drop the 'artist' table if it exists
    cur.execute("DROP TABLE IF  EXISTS artist")
    # Drop the 'track' table if it exists
    cur.execute("DROP TABLE IF  EXISTS track")
    
    # Commit the changes to the database
    conn.commit()

# Define a function to insert an artist's data into the artist table
def insert_artist(conn, cur, info):

    # Insert the artist data into the artist table, ignore if the entry already exists
    cur.execute("INSERT OR IGNORE INTO  artist VALUES(?,?,?,?,?)", info)
    # Commit the changes to the database    
    conn.commit()

# Define a function to insert track data into the track table
def insert_track(conn, cur, info):

    # Insert multiple track data entries into the track table, ignore if they already exist
    cur.executemany("INSERT OR IGNORE INTO track VALUES(?,?,?)", info)
    # Commit the changes to the database
    conn.commit()