# inky-spotify
Use a Raspberry Pi to display album art for your current Spotify listens on a 7-colour ePaper display.

## Usage 
Designed for use with an [Inky Impression](https://shop.pimoroni.com/products/inky-impression) 7 colour ePaper display. The ePaper display transitions bring the album art to life, and doesn't require power to maintain the image!

1. Follow the setup instructions for Inky Impression [here](https://github.com/pimoroni/inky).

2. Connect your display to a Pi, and clone this repo on the Pi. 

3. Create a file called `auth.json` with the following structure (get this information from Spotify Developers Portal) in the root of the repo:
```
{
	"spotify_client_id":     "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
	"spotify_client_secret": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```

4. Run `main.py`:
```
./main.py
```

5. Authenticate your Spotify account (one time only).

6. Play a track on Spotify.

7. Enjoy the view. 

## Authors
@tomcobley and @bencobley
