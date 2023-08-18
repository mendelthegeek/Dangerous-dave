# import sys

from physics import *
from levels import *
import sys

from render import *


class Game:

    def __init__(self, lvl=1):
        self.board = pygame.display.set_mode((640, 392))
        self.score = 0
        self.dave = None
        self.level = None
        self.lives = 3
        self.lvl = lvl

        self.sprite_source = r"resources/tileset/tileset.png"
        sprite_sheet = SpriteSheet(self)
        icon = sprite_sheet.get_sprite(5, 4, 16, 16, 2)
        pygame.display.set_caption("Dangerous self.dave")
        pygame.display.set_icon(icon)
        pygame.init()

    def start(self):
        self.level = eval(f"Level{self.lvl}()")
        self.dave = Dave(self.level.dave_pos)

        self.run()

    def run(self):
        running = True
        while running:
            if self.score >= 100000:
                self.score = 99999

            render(self)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.dave.x_speed = 0
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                if self.dave.on_surface and self.dave.jump_height == 0:
                    self.dave.jump_height += 94
            if pressed[pygame.K_RIGHT]:
                self.dave.x_speed += 1
            if pressed[pygame.K_LEFT]:
                self.dave.x_speed -= 1

            if True in pressed:
                self.dave.moved = True

            self.score += check_obtained(self.dave, self.level.gems)
            check_collision(self.dave, self.level.tiles)
            if check_door(self.dave, self.level.doors):
                self.score += 2000
                self.lvl += 1

                self.level = NextLevel()
                self.dave = Dave(self.level.dave_pos)
                self.render()

                self.start()
            if check_death(self.dave, self.level.hazards):
                running = False
                self.restart_level()

            if self.dave.x == 18.5 * 32 and self.dave.x_speed == 1:
                slide_over(self, -1)
            elif self.dave.x == 1.5 * 32 and self.dave.x_speed == -1:
                slide_over(self, 1)

    def restart_level(self):
        had_key = self.dave.has_key
        self.dave.die(self)
        if self.lives == 0:
            sys.exit()
        self.lives -= 1
        self.dave = Dave(self.level.dave_pos)
        self.dave.has_key = had_key
        offset = self.level.door_start[0]*32 - self.level.doors.sprites()[0].rect.left
        reset_position(self.level, offset)

        self.run()

    def render(self):
        self.dave.moved = True
        self.dave.x_speed = 1

        running = True
        while self.dave.x < 608 and running:
            render(self)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


game = Game(1)
game.start()
