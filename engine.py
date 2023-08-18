# import sys

from physics import *
from levels import *
import sys

from render import *


class Game:

    def __init__(self):
        self.score = 0
        self.dave = None
        self.level = None
        self.lives = 3

        self.sprite_source = r"resources/tileset/tileset.png"
        sprite_sheet = SpriteSheet(self)
        icon = sprite_sheet.get_sprite(5, 4, 16, 16, 2)
        pygame.display.set_caption("Dangerous self.dave")
        pygame.display.set_icon(icon)

    def start(self, lvl):
        pygame.init()
        self.level = eval(f"Level{lvl}()")
        self.dave = Dave(self.level.dave_pos)

        self.score = self.run()

        NextLevel(self.score)

        self.start(lvl + 1)

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

            if len(pressed) > 0:
                self.dave.moved = True

            self.score += check_obtained(self.dave, self.level.gems)
            check_collision(self.dave, self.level.tiles)
            if check_death(self.dave, self.level.hazards):
                sys.exit()
            if check_door(self.dave, self.level.doors):
                self.score += 2000
                return self.score

            if self.dave.x == 18.5 * 32 and self.dave.x_speed == 1:
                slide_over(self.dave, self.level, self.score, -1)
            elif self.dave.x == 1.5 * 32 and self.dave.x_speed == -1:
                slide_over(self.dave, self.level, self.score, 1)


game = Game()
game.start(1)
