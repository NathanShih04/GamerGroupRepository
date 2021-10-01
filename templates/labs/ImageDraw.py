from PIL import Image, ImageDraw

img = Image.open("/static/MonkeyMaids.jpg")
d1 = ImageDraw.Draw("/static/MmmMonkeyMaids.jpg")
d1.text((28, 36), "Mmm Monkey", fill=(255, 0, 0))
img.show("/static/MmmMonkeyMaids.jpg")
img.save("/static/MmmMonkeyMaids.jpg")