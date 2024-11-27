# Spotify-Random-Song 🎶
Play a random song from your Spotify playlists. This Python project uses Spotify API to select a playlist and randomly choose a song to play.

## Requirements
- Python 3.x
- Spotify Developer Account (to get your API credentials)

## Setup

### 1. Clone the Repository 
```git clone https://github.com/0xWiIIiam/Spotify-Random-Song.git```

```cd spotify-random-player```

### 3. Create a .env File
In the project root directory, create a file named .env and add your Spotify credentials like so:
```SPOTIFY_CLIENT_ID=your_spotify_client_id_here```

```SPOTIFY_CLIENT_SECRET=your_spotify_client_secret_here```

```SPOTIFY_REDIRECT_URI=http://localhost:8888/callback```

### 4.Create a Spotify Developer Account
You’ll need to create a [Spotify developer account](https://developer.spotify.com/dashboard/applications) to generate your own ID and token.

### 5. Install Dependencies
```pip install -r requirements.txt```

### 6. Run
```python main.py```
