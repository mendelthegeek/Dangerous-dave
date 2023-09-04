import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, direction, creature, x=0, y=0):
        super().__init__()
        self.x = x + (direction + 1) * 10
        self.y = y + 10
        self.rect = pygame.Rect(self.x, self.y, 18, 6)
        self.x_dir = direction
        self.last_updated = pygame.time.get_ticks()
        if creature == "dave":
            self.image = pygame.image.load("resources/dave/bullet.png")
        elif creature == "mob":
            self.image = pygame.image.load("resources/mobs/bullet.png")

    def move(self):
        curr_ticks = pygame.time.get_ticks()
        if curr_ticks - self.last_updated > 3:
            self.x += self.x_dir
            self.last_updated = curr_ticks
        self.rect.update(self.x, self.y, 18, 6)

    def get_location(self):
        image = self.image
        if self.x_dir == -1:
            image = pygame.transform.flip(self.image, True, False)
        image = pygame.transform.scale(image, (2*image.get_width()//3, 6))
        image.set_colorkey((0, 0, 0))
        return image, (self.x, self.y)
