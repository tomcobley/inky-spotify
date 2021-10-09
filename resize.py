from PIL import Image

img = Image.open('cover.jpg')
img = img.resize((448, 448), Image.ANTIALIAS)

img_resized = Image.new(img.mode, (600, 448), (255, 255, 255))  
img_resized.paste(img, (76, 0))
img_resized.save('display.jpg')
