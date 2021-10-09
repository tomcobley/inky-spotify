#!/usr/bin/env python3

import urllib.request
from PIL import Image
from inky.inky_uc8159 import Inky
import time

inky = Inky()
saturation = 0.6


def update_display(url):

    urllib.request.urlretrieve(url,'cover.jpeg')

    img = Image.open('cover.jpeg')
    img = img.resize((448, 448), Image.ANTIALIAS)

    img_resized = Image.new(img.mode, (600, 448), (255, 255, 255))  
    img_resized.paste(img, (76, 0))

    inky.set_image(img_resized, saturation=saturation)
    inky.show()

def clean():
    for _ in range(2):
        for y in range(inky.height - 1):
            for x in range(inky.width - 1):
                inky.set_pixel(x, y, CLEAN)

        inky.show()
        time.sleep(1.0)

update_display("https://i.scdn.co/image/ab67616d0000b27357751ae9890e997676b998f2")