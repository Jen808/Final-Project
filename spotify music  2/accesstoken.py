import requests

# Define a function to generate the authorization headers required for Spotify API requests
def tokenizer():
    # Spotify API client ID
    client_id = 'd9cc6771d4504cb0ae4acd085c1bc13e'
    # Spotify API client secret
    client_secret = '1c6d19bbe9dd45c98a91f2d5389f518a' 

    # Obtain an access token using the client ID and client secret
    token = get_access_token(client_id, client_secret)
    # Format the headers with the obtained access token
    headers = {'Authorization': 'Bearer {}'.format(token)}
    
    # Return the headers for use in API requests
    return headers

# Define a function to get an access token from Spotify API
def get_access_token(client_id, client_secret):
        
        # Spotify API token URL
        token_url = 'https://accounts.spotify.com/api/token'
        # Authentication tuple with client ID and client secret
        auth = (client_id, client_secret)
        # Data payload with the grant type set to 'client_credentials'
        data = {'grant_type': 'client_credentials'}

        # Make a POST request to the token URL with authentication and data
        response = requests.post(token_url, auth=auth, data=data)
        # Extract the 'access_token' from the response JSON
        token = response.json().get('access_token')
        # Return the access token
        return token