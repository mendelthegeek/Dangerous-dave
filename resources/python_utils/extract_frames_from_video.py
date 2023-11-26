import imageio.v3 as iio
filename = "../levels/videos/level5.mp4"
for idx, frame in enumerate(iio.imiter(filename)):
    iio.imwrite(f"../mobs/extracted_images/level5_frame{idx:03d}.png", frame)