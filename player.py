import pygame

from render import SpriteSheet


class Dave(pygame.sprite.Sprite):

    def __int__(self):
        self.x, self.y = 10, 10
        self.sprite_source = r"resources\dave\Dave.png"

        self.speed = 10

        self.sprite_sheet = SpriteSheet(self.sprite_source)

        self.walk_right = []
        for i in range(4):
            self.walk_right.append(self.sprite_sheet.get_sprite(i, 24, 16, 2))

    def current_display(self):
        display_frame = self.sprite_sheet.frame//8 % 4
        return self.walk_right[display_frame]

    def position(self):
        return self.x, self.y

    def move_right(self):
        self.x += 1
        self.sprite_sheet.move_frame()
