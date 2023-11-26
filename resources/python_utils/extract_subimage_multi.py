# Importing Image class from PIL module
import sys

from PIL import Image

for i in range(8):
    # Opens a image in RGB mode
    im = Image.open(r"extracted_images/frame"
                    f"{19+i*6:03}"
                    r".png")

    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    width, height = im.size

    # Setting the points for cropped image
    left = 296
    top = (174 + i*6)
    right = 345
    bottom = (215 + i*6)

    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))

    # Shows the image in image viewer
    im1.save(f"death/frame_{i}.png")

im1.show("TEST IMAGE")