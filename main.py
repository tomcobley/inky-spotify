#!/usr/bin/env python3

import urllib.request
import time
import json
import os 
import spotipy

from spotipy.oauth2 import SpotifyOAuth
from PIL import Image
from inky.inky_uc8159 import Inky

inky = Inky()
SATURATION = 0.6
REFRESH_PERIOD_SECS = 5
CLEAN_PERIOD_CYCLES = 2

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

def update_display(url):
    urllib.request.urlretrieve(url, 'cover.jpeg')

    img = Image.open('cover.jpeg')
    img = img.resize((448, 448), Image.ANTIALIAS)

    img_resized = Image.new(img.mode, (600, 448), (255, 255, 255))
    img_resized.paste(img, (76, 0))

    inky.set_image(img_resized, saturation=SATURATION)
    inky.show()

def clean():
    for _ in range(2):
        for y in range(inky.height - 1):
            for x in range(inky.width - 1):
                inky.set_pixel(x, y, CLEAN)

        inky.show()
        time.sleep(1.0)

if __name__ == "__main__":
    set_secrets()
    
    ticks = 0
    prev_url = ""

    while True:
        url = get_current_track_art_url()

        if url != prev_url:
            if ticks % CLEAN_PERIOD_CYCLES == 0:
                clean()

            prev_url = url
            print ("Displaying new image: " + url)
            update_display(url)

        time.sleep(REFRESH_PERIOD_SECS)


