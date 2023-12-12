import matplotlib.pyplot as plt
import numpy as np

# Define a function to calculate and plot the maximum and minimum popularity of tracks for each artist
def max_min_popularity(conn, cur):
    # Initialize a list to store artist names
    labels = []
    # Initialize a list to store maximum popularity values
    max_popularity = []
    # Initialize a list to store minimum popularity values
    min_popularity = []

# Execute SQL query to find the minimum track popularity for each artist
    cur.execute("SELECT track_name, name, min(track_popularity) FROM artist JOIN track USING(artist_id) group by artist_id")
# Append the artist name to labels list
    for data in cur.fetchall():
        labels.append(data[1])
        # Append the minimum popularity to the min_popularity list
        min_popularity.append(data[2])

# Execute SQL query to find the maximum track popularity for each artist
    cur.execute("SELECT track_name, name, max(track_popularity) FROM artist JOIN track USING(artist_id) group by artist_id")
# Append the maximum popularity to the max_popularity list
    for data in cur.fetchall():
        max_popularity.append(data[2])

   

    # Bar width
    bar_width = 0.35

    # Set up the figure and axes
    fig, ax = plt.subplots()

    # Create bar plots for max and min scores
    bar1 = ax.bar(labels, max_popularity, bar_width, label='Max Popularityu')
    bar2 = ax.bar(np.arange(len(labels)) + bar_width, min_popularity, bar_width, label='Min Popularity')

    # Add labels, title, and legend
    ax.set_xlabel('Artist Name')
    ax.set_ylabel('poularity')
    ax.set_title('Max and Min Popularity for each artist')
    ax.set_xticks(np.arange(len(labels)) + bar_width / 2)
    ax.set_xticklabels(labels)
    ax.legend()

    # Show the plot
    plt.show()

# Display the plot
def followers(conn, cur):
    # Execute SQL query to retrieve the name and number of followers for each artist
    cur.execute("SELECT name, followers FROM artist")

    # Initialize a list to store artist names
    artists = []
    # Initialize a list to store follower counts
    followers = []
    
# Append the artist name to the artists list
    for data in cur.fetchall():
        artists.append(data[0])
        followers.append(data[1])

    # Set up the figure and axes
    fig, ax = plt.subplots()

    # Create a bar plot for followers
    ax.bar(artists, followers, color='skyblue')

    # Add labels and title
    ax.set_xlabel('Artist')
    ax.set_ylabel('Followers')
    ax.set_title('Follower Counts for Each Artist')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Show the plot
    plt.show()