from collections import defaultdict

from PIL import Image

# picture = Image.open("../mobs/spider1.png")
#
# # Get the size of the image
# width, height = picture.size


def rgb_of_pixel(img_path, c, d):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((c, d))
    a = (r, g, b)
    return a


# for i in range(1,4):
#     print(rgb_of_pixel("../mobs/spider1.png", i, 16))

new_color = (0, 0, 0)
for i in range(4):
    picture = Image.open(f"../mobs/alien{i}.png")
    counter = defaultdict(int)

    # Get the size of the image
    width, height = picture.size
    # Process every pixel
    for x in range(width):
        for y in range(height):
            current_color = picture.getpixel((x, y))
            if y == 16 and x < 25:
                print(f"pixel {x} has value {current_color}")
            if sum(current_color) < 35:
                counter[x] += 1
                picture.putpixel((x, y), new_color)

    picture.save(f"../mobs/alien{i}.png")
    # print(sorted(counter.items(), key=lambda item: -item[1]))
# print(rgb_of_pixel("../mobs/spider1_new.png", 3, 16))
