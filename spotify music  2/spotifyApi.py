import requests

# Define a function to get the Spotify artist ID given the artist's name
def getArtistId(headers, name):
# Spotify API endpoint for searching
    url = "https://api.spotify.com/v1/search"
# Parameters for the API call: search query, type of search (artist), and limit to 1 result    
    param = {
        "q" : name,
        "type" : "artist",
        "limit" : 1
    }
# Perform the API request with the given URL, headers, and parameters
    res = requests.get(url, headers = headers, params = param)
# Parse the response as JSON
    data = res.json()
# Return the ID of the first artist found
    return data['artists']['items'][0]['id']

# Define a function to get detailed information about an artist using their Spotify ID
def getArtist(headers, id):
 # Spotify API endpoint for fetching artist details, formatted with the artist's ID
    url = "https://api.spotify.com/v1/artists/{}".format(id)
   
# Perform the API request with the given URL and headers
    res = requests.get(url, headers= headers)
# Parse the response as JSON
    data = res.json()
# Extract the artist's name, follower count, popularity, and first genre
    name = data['name']
    followers = data['followers']['total']
    popularity = data['popularity']
    generes = data['genres'][0]
# Combine these details into a tuple
    info = (id, name, followers, popularity, generes)
# Return the tuple containing the artist's details
    return info

# Define a function to get the top tracks of an artist using their Spotify ID
def getTrack(headers, id):

# Spotify API endpoint for fetching top tracks of an artist, formatted with the artist's ID
    url = "https://api.spotify.com/v1/artists/{}/top-tracks".format(id)
# Parameters for the API call: specify the market
    param = {
        "market" : "ES"
    }
# Perform the API request with the given URL, headers, and parameters
    res = requests.get(url, headers= headers, params = param)
# Parse the response as JSON
    data = res.json()
# Initialize a list to store track details
    store = []
# Append a tuple with the artist ID, track name, and track popularity to the list    
    for album in data['tracks']:
        store.append((id, album['name'], album['popularity']))
# Return the list of tuples containing track details
    return store








