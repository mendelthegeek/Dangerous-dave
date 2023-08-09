import pygame

from render import *


class Dave(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.x, self.y = 64, 282
        self.sprite_source = r"resources\dave\Dave.png"

        self.speed = 10

        self.sprite_sheet = SpriteSheet(self)
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
        self.facing = 0
        self.moved = False
        self.displayed = True
        self.on_surface = False
        self.last_blinked = pygame.time.get_ticks()
        self.rect = pygame.Rect(0,0,0,0)
        self.move()

    def current_display(self):
        if not self.moved:
            current_ticks = pygame.time.get_ticks()
            if current_ticks - self.last_blinked > 500:
                self.last_blinked = current_ticks
                self.displayed = not self.displayed
            if self.displayed:
                empty_square = (pygame.Surface((24, 16)))
                empty_square.fill(BG)
                return empty_square
            elif not self.displayed:
                return self.sprite_sheet.get_sprite(0, 6, 24, 16, 2)
        return self.display_frame

    def position(self):
        return self.x, self.y

    def move(self):
        if self.moving_right or self.moving_left or not self.velocity == 0:
            self.moved = True
        if self.moving_right:
            self.move_right()
        if self.moving_left:
            self.move_left()
        self.jump()
        self.move_rect()


    def move_right(self):
        self.sprite_sheet.move_sprite(1, 0)
        self.sprite_sheet.move_frame()
        display_frame = self.sprite_sheet.frame//8 % 4
        self.display_frame = self.walk_right[display_frame]
        self.facing = 0

    def move_left(self):
        self.sprite_sheet.move_sprite(-1, 0)
        self.sprite_sheet.move_frame()
        display_frame = self.sprite_sheet.frame//8 % 4
        self.display_frame = self.walk_left[display_frame]
        self.facing = 1

    def jump(self):
        if self.velocity > 0:
            self.velocity -= 1
            self.sprite_sheet.move_sprite(0, -1)
            self.display_frame = self.sprite_sheet.get_sprite(self.facing,5,24, 16, 2)
        if self.velocity == 0 and self.moved and not self.on_surface:
            self.sprite_sheet.move_sprite(0, 1)

    def move_rect(self):
        self.rect.update(self.x, self.y, 20, 32)
