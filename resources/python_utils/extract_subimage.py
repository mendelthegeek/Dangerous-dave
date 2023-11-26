# Importing Image class from PIL module
from PIL import Image

# Opens a image in RGB mode
im = Image.open(r"..\mobs\extracted_images\level5_frame045.png")

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size

# Setting the points for cropped image
left = 714
top = 145
right = left+63
bottom = top+64

# (It will not change original image)
im1 = im.crop((left, top, right, bottom))

# im1.show()

# Shows the image in image viewer
im1.save("../mobs/alien0.png")