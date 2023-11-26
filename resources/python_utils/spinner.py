# import the Python Image
# processing Library
from PIL import Image

# Giving The Original image Directory
# Specified
Original_Image = Image.open("../mobs/spinner0.png")

for i in range(20):
    # Rotate Image By 180 Degree
    rotated_image = Original_Image.rotate(i*18)

    rotated_image.save(f"../mobs/test/spinner{i+1}.png")
