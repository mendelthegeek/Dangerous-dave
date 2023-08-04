import pygame

from render import SpriteSheet


class Dave(pygame.sprite.Sprite):

    def __int__(self):
        self.x, self.y = 10, 660
        self.sprite_source = r"resources\dave\Dave.png"

        self.speed = 10

        self.sprite_sheet = SpriteSheet(self.sprite_source)
        self.velocity = 0

        self.walk_right = []
        for i in range(4):
            self.walk_right.append(self.sprite_sheet.get_sprite(0, i, 24, 16, 2))
        self.display_frame = self.walk_right[0]
        self.walk_left = []
        for i in range(4):
            self.walk_left.append(self.sprite_sheet.get_sprite(1, i, 24, 16, 2))
        self.moving_right = False
        self.moving_left = False

    def current_display(self):
        return self.display_frame

    def position(self):
        return self.x, self.y

    def move(self):
        if self.moving_right:
            self.move_right()
        if self.moving_left:
            self.move_left()
        self.jump()

    def move_right(self):
        self.x += 1
        self.sprite_sheet.move_frame()
        display_frame = self.sprite_sheet.frame//8 % 4
        self.display_frame = self.walk_right[display_frame]

    def move_left(self):
        self.x -= 1
        self.sprite_sheet.move_frame()
        display_frame = self.sprite_sheet.frame//8 % 4
        self.display_frame = self.walk_left[display_frame]

    def jump(self):
        if self.velocity > 0:
            self.velocity -= 1
            self.y -= 1
            if self.moving_right:
                self.display_frame = self.sprite_sheet.get_sprite(0,5,24, 16, 2)
            else:
                self.display_frame = self.sprite_sheet.get_sprite(1, 5, 24, 16, 2)
