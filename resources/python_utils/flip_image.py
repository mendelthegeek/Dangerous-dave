import time

import cv2

image = cv2.imread('../mobs/bullet.png')

flippedimage = cv2.flip(image, 1)

cv2.imwrite("../mobs/bullet.png", flippedimage)
