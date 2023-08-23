import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, direction, creature, x=0, y=0):
        super().__init__()
        self.x = x
        self.y = y
        self.x_dir = direction
        self.last_updated = pygame.time.get_ticks()
        if creature == "dave":
            self.image = pygame.image.load("resources/dave/bullet.png")

    def move(self):
        curr_ticks = pygame.time.get_ticks()
        if curr_ticks - self.last_updated > 3:
            self.x += self.x_dir
            self.last_updated = curr_ticks

    def get_location(self):
        return self.x, self.y
