import math
import sys
from collections import defaultdict

from PIL import Image
from PIL import ImageDraw


# filename = r"C:\Users\Mendel\IdeaProjects\Dangerous-dave\resources\dave\level4_mob_frame000.png"


def rgb_of_pixel(img_path, c, d):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((c, d))
    a = (r, g, b)
    return a


def overlay(picture, offset):
    # Get the size of the image
    width, height = picture.size

    new_color = (255, 255, 255)
    # Process every pixel
    for x in range(20):
        for y in range(height):
            picture.putpixel((x * 48, y), new_color)
    for x in range(width):
        for y in range(10):
            picture.putpixel((x, y * 48), new_color)
    I1 = ImageDraw.Draw(picture)
    for x in range(20):
        for y in range(10):
            I1.text(
                (x * 48 + 12, y * 48 + 12),
                f"{str(x + offset)}, {str(y)}",
                fill=(255, 255, 255)
            )

    return picture
