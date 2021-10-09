import json
import os 
import spotipy

from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

def set_secrets():
    with open('secrets.json') as secrets_file:
        data = json.load(secrets_file)
        os.environ['SPOTIPY_CLIENT_ID'] = data['spotify_client_id']
        os.environ['SPOTIPY_CLIENT_SECRET'] = data['spotify_client_secret']
        os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:8888'
    
def get_current_track_art_url():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope = "user-read-currently-playing"))
    data = sp.currently_playing()
    url = data['item']['album']['images'][0]['url']
    return url

if __name__ == "__main__":
    
    set_secrets() 
    
    ticks = 0
    prev_url = ""

    while True:
        
        url = get_current_track_art_url()
        
        if url != prev_url:
            
            if ticks % 2 == 0:
                clean_display()
            
            update_display(url)

        time.sleep(10)


