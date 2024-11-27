import os
import random
from spotipy.oauth2 import SpotifyOAuth
import spotipy
from dotenv import load_dotenv

load_dotenv() # loads enviroment variables from .env

# spotify api stuff
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

# authenticate with spotfy
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-library-read user-read-playback-state user-modify-playback-state"
))

# function to get a random song
def GetRandomSong():
    Playlists = sp.current_user_playlists(limit=5) # retrives 5 of the users playlists
    
    if not Playlists['items']: # checks if there are playlists
        print("no playlists")
        return None
    
    Playlist = random.choice(Playlists['items']) # picks a random playlist from the 5

    playlistSongs = sp.playlist_tracks(Playlist['id'], limit=50) # picks 50 tracks from the random playlist selected
    
    if not playlistSongs['items']:
        print("no songs in the playlist")
        return None
    songToPlay = random.choice(playlistSongs['items'])['track']

    songName = songToPlay['name']
    artistName = ', '.join(artist['name'] for artist in songToPlay['artists'])

    print(f"Now playing: {songName} by {artistName}")

    return songToPlay

def PlayRandomSong():
    Devices = sp.devices() # retrives devices where playback can happen

    if not Devices['devices']: # if none returns
        print("no devices")
        return None
    
    deviceID = Devices['devices'][0]['id']

    songToPlay = GetRandomSong()

    if not songToPlay:
        return EncodingWarning
    
    sp.start_playback(device_id=deviceID, uris=[songToPlay['uri']]) # plays the chosen song by using the URI

PlayRandomSong()