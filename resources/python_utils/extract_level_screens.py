import io

import imageio.v3 as iio
import numpy as np
from PIL import Image

from resources.python_utils.overlay_grid import overlay

avg = np.matrix([0, 0, 0])
index = 0
# filename = "level4_mob"
countdown = 0
for frame in iio.imiter(f"../levels/videos/level6.mp4"):
    new_avg = np.matrix(np.average(frame, axis=(0, 1)))
    if np.absolute(avg - new_avg).max() > 3:
        countdown = max(countdown - 1, 0)
        if countdown == 0:
            countdown = 20
            avg = new_avg
            picture = Image.fromarray(frame).convert('RGB')
            offset = index * 15
            if index == 6:
                offset = 80
            picture = overlay(picture, offset)
            picture.save(f"../levels/screens/level6_screen{index}.png")
            index += 1
