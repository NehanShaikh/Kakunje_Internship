from PIL import Image, ImageFilter

# Task1
img = Image.open("image.jpg")
img.show()

# Task2
print(img.size)
print(img.mode)
print(img.format)

# Task3
resized = img.resize((300, 300))
resized.show()

# Task4
gray = img.convert("L")
gray.show()

# Task5
bw = img.convert("1")
bw.show()

# Task6
rotated = img.rotate(45)
rotated.show()

# Task7
cropped = img.crop((50, 50, 300, 300))
cropped.show()

# Task8
gray.save("gray_image.jpg")

# Task9
img.thumbnail((100, 100))
img.show()

# Task10
blur = img.filter(ImageFilter.BLUR)
blur.show()

# Task11
sharp = img.filter(ImageFilter.SHARPEN)
sharp.show()

# Task12
edge = img.filter(ImageFilter.FIND_EDGES)
edge.show()

# Task13
img = Image.open("image.jpg")

img = img.resize((200, 200))
img = img.convert("L")
img = img.rotate(90)

img.save("new_image.jpg")
img.show()
