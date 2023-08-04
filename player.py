import pygame


class Dave(pygame.sprite.Sprite):

    def __int__(self):
        self.position = (0, 0)
        self.sprite_images = pygame.image.load(r"resources\dave\Dave.png")