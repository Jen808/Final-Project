# Team name: Korean Duo
# Resource we used: Chat GPT 4.0
import sqlite3
import spotifyApi
import db
import accesstoken
import spotifyApi
import analysis
import time
# Establish a connection to the 'spotify.db' SQLite database
conn = sqlite3.connect("spotify.db")
# Create a cursor object to interact with the database  
cur = conn.cursor()
# Call a function 'droptables' from the 'db' module to drop existing tables in the database
db.droptables(conn, cur)
# Call a function 'createtables' from the 'db' module to create new tables in the database
db.createtables(conn, cur)
# Generate headers by calling the 'tokenizer' method
headers = accesstoken.tokenizer()

# Define a function named 'manual' for manual data entry
def manual():
    # Prompt the user to input an artist's name
    name = input("Add the artist you want to: ")

    # Loop as long as the input name is not empty
    while len(name)>0:
    # Get the artist's ID from Spotify API using the input name
        id = spotifyApi.getArtistId(headers, name)      
    # Retrieve artist's information using the Spotify API
        info = spotifyApi.getArtist(headers,id)
    # Insert the artist's information into the database
        db.insert_artist(conn, cur, info)
    # Retrieve the tracks of the artist using the Spotify API
        info = spotifyApi.getTrack(headers, id)
    # Insert the track information into the database
        db.insert_track(conn, cur, info)
    # Prompt for the next artist's name
        name = input("Add the artist you want to: ")

 # Define a function named 'automatic' for automatic data entry       
def automatic():
    # List of predefined artist names
    names = ["New Janes", "Travis Scott", "Taylor swift", "BTS", "Drake", "FKJ","Future", "Migos", "Jay Park", "IU", "Highvyn"]
# Iterate through each artist in the list
    for name in names:
# Get the artist's ID from Spotify API using the artist's name
        id = spotifyApi.getArtistId(headers, name)
# Pause execution for 0.1 seconds to avoid hitting API rate limits
        time.sleep(0.1)
# Retrieve artist's information using the Spotify API
        info = spotifyApi.getArtist(headers,id)
# Insert the artist's information into the database
        db.insert_artist(conn, cur, info)
# Retrieve the tracks of the artist using the Spotify API 
        info = spotifyApi.getTrack(headers, id)
 # Insert the track information into the database
        db.insert_track(conn, cur, info)
# Pause execution for 0.1 seconds to avoid hitting API rate limits
        time.sleep(0.1)

# Prompt the user to choose between Automatic and Manual modes
user_in = input("A for Automatic, M for Manual")

# Execute the 'automatic' function if the user inputs 'A', otherwise execute the 'manual' function
if user_in == "A":
    automatic()
else:
    manual()

# Call a function 'max_min_popularity' from the 'analysis' module to analyze maximum and minimum popularity
analysis.max_min_popularity(conn, cur)

# Call a function 'followers' from the 'analysis' module to analyze followers data
analysis.followers(conn, cur)