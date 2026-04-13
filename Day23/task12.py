# Task 12 - Pillow
from PIL import Image, ImageFilter

img = Image.open("image.jpg")
img.show()

img = img.resize((200,200))
img.show()

img = img.convert("L")
img.show()
img = img.rotate(45)
img.show()
img = img.crop((10,10,180,180))
img.show()
img = img.filter(ImageFilter.BLUR)
img.show()

img.save("modified.png")
