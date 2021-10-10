#!/usr/bin/env python3

import urllib.request
import time
import json
import os
import spotipy

from spotipy.oauth2 import SpotifyOAuth
from PIL import Image

from inky.inky_uc8159 import Inky, CLEAN

inky = Inky()

SATURATION = 0.8
WIDTH = 600  # eink screen dimensions
HEIGHT = 448
VISIBLE_WIDTH = 448  # area not covered by frame
VISIBLE_HEIGHT = 448
API_CALL_INTERVAL = 5
CLEAN_INTERVAL = 3


def authenticate():
    with open("auth.json") as auth_file:
        data = json.load(auth_file)
        os.environ["SPOTIPY_CLIENT_ID"] = data["spotify_client_id"]
        os.environ["SPOTIPY_CLIENT_SECRET"] = data["spotify_client_secret"]
        os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8888"


def get_current_album_art_url():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-read-currently-playing"))
    data = sp.currently_playing()
    if data:
        return data["item"]["album"]["images"][0]["url"]
    else:
        return None


def update_eink_display(url):
    urllib.request.urlretrieve(url, "album_art.jpeg")

    img = Image.open("album_art.jpeg")
    img = img.resize((VISIBLE_WIDTH, VISIBLE_HEIGHT), Image.ANTIALIAS)

    hidden_column_width = (WIDTH - VISIBLE_WIDTH) // 2

    img_resized = Image.new(img.mode, (WIDTH, HEIGHT), (255, 255, 255))
    img_resized.paste(img, (hidden_column_width, 0))
    inky.set_image(img_resized, saturation=SATURATION)

    for y in range(HEIGHT - 1):
        for x in range(hidden_column_width - 1):
            inky.set_pixel(x, y, CLEAN)
            inky.set_pixel(600 - x - 1, y, CLEAN)
    inky.show()


def clean():

    for _ in range(2):
        for y in range(HEIGHT - 1):
            for x in range(WIDTH - 1):
                inky.set_pixel(x, y, CLEAN)

        inky.show()
        time.sleep(1)


if __name__ == "__main__":
    authenticate()

    ticks = 0
    prev_url = ""

    while True:
        url = get_current_album_art_url()

        if url != prev_url:
            if ticks % CLEAN_INTERVAL == 1:
                clean()

            prev_url = url
            if url != "":
                print("Displaying new image: " + url)
                update_eink_display(url)
                ticks += 1

        time.sleep(API_CALL_INTERVAL)

