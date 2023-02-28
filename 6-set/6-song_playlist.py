# Define a dictionary to store the playlists
playlists = {}

# Function to add a song to a playlist
def add_song_to_playlist(playlist_id, song_id):
    # Check if the playlist already exists in the dictionary
    if playlist_id not in playlists:
        # If not, create a new set for the playlist
        playlists[playlist_id] = set()
    # Add the song ID to the playlist's set
    playlists[playlist_id].add(song_id)

# Function to remove a song from a playlist
def remove_song_from_playlist(playlist_id, song_id):
    # Check if the playlist exists in the dictionary
    if playlist_id in playlists:
        # Remove the song ID from the playlist's set
        playlists[playlist_id].discard(song_id)

# Example usage
add_song_to_playlist(1, 100)
add_song_to_playlist(1, 200)
add_song_to_playlist(2, 100)
add_song_to_playlist(2, 300)
remove_song_from_playlist(1, 100)

# Print the playlists dictionary
print(playlists)
