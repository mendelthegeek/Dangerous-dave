from collections import defaultdict

from PIL import Image

picture = Image.open("../mobs/spider1.png")

# Get the size of the image
width, height = picture.size

color_count = defaultdict(int)


def rgb_of_pixel(im, c, d):
    im = im.convert('RGB')
    r, g, b = im.getpixel((c, d))
    return r, g, b

for i in range(width):
    for j in range(height):
        color_count[rgb_of_pixel(picture, i, j)] += 1

print(sorted(color_count.items(), key=lambda trip: sum(trip[0])))