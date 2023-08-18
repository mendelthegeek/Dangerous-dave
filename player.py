import os

import pygame

from banner import blit_border
from render import render_level
from spritesheet import SpriteSheet


BG = (50, 50, 50)

class Dave(pygame.sprite.Sprite):

    def __init__(self, init_pos):
        super().__init__()
        self.x, self.y = init_pos
        self.sprite_source = r"resources\dave\Dave.png"

        self.speed = 8

        self.sprite_sheet = SpriteSheet(self)
        self.jump_height = 0

        self.x_speed = 0
        self.y_speed = 0
        self.facing = 0
        self.moved = False
        self.displayed = True
        self.on_surface = True
        self.last_blinked = pygame.time.get_ticks()
        self.rect = pygame.Rect(0,0,0,0)
        self.move()
        self.last_update = pygame.time.get_ticks()
        self.has_key = False

    def current_display(self):
        if not self.x_speed == 0:
            # expression maps 1 to 0 and -1 to 1, mapping movement to desired spritesheet row
            self.facing = (1 - self.x_speed)/2
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
        if self.on_surface:
            return self.sprite_sheet.get_sprite(self.facing, self.sprite_sheet.frame//8 % 4, 24, 16, 2)
        else:
            return self.sprite_sheet.get_sprite(self.facing,5,24, 16, 2)

    def position(self):
        return self.x, self.y

    def move(self):
        if not self.x_speed == 0:
            self.sprite_sheet.move_frame()
        self.jump()
        self.x += self.x_speed*1.2
        self.y = (self.y + self.y_speed) % 424
        self.move_rect()

    def jump(self):
        if self.jump_height == 0 and self.moved:
            if not self.on_surface:
                self.y_speed = 1
            else:
                self.y_speed = 0
        if self.jump_height > 0:
            self.jump_height -= 1
            if self.jump_height > 29:
                self.y_speed = -1
            else:
                self.y_speed = 0

    def move_rect(self):
        self.rect.update(self.x+8, self.y, 14, 32)

    def die(self, game):
        path = r"resources\dave\death"
        images = os.listdir(path)
        for image in images:
            game.board.fill(BG)

            render_level(game.level, game.board)

            death_frame = pygame.Surface((49, 41)).convert_alpha()
            rectangle = (0, 0, 49, 41)
            death_image = pygame.image.load(path + "\\" + image)
            death_frame.blit(death_image, (0, 0), rectangle)
            death_frame.set_colorkey((0, 0, 0))
            death_frame = pygame.transform.scale(death_frame, (35, 30))
            game.board.blit(death_frame, self.position())

            blit_border(game)
            pygame.display.flip()
            pygame.time.delay(200)