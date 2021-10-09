#!/usr/bin/env python3

import urllib.request
from PIL import Image
from inky.inky_uc8159 import Inky

inky = Inky()
saturation = 0.6

urllib.request.urlretrieve(
  'https://i.scdn.co/image/ab67616d0000b27357751ae9890e997676b998f2',
   "cover.jpeg")

img = Image.open('cover.jpeg')
img = img.resize((448, 448), Image.ANTIALIAS)

img_resized = Image.new(img.mode, (600, 448), (255, 255, 255))  
img_resized.paste(img, (76, 0))

inky.set_image(img_resized, saturation=saturation)
inky.show()