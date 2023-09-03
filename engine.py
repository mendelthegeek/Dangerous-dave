from physics import *
from levels import *
import sys

from render import *


class Game:

    def __init__(self, lvl=1, testing=False):
        self.board = pygame.display.set_mode((640, 432))
        self.score = 0
        self.dave = None
        self.level = None
        self.lives = 3
        self.lvl = lvl

        self.testing = testing

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
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_RALT or event.key == pygame.K_LALT):
                    if self.dave.jetpack > 0:
                        self.dave.flying = not self.dave.flying
                        self.dave.jump_height = 0

            self.dave.x_speed = 0
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                if self.dave.on_surface and self.dave.jump_height == 0:
                    self.dave.jump_height += 94
                if self.testing or self.dave.flying:
                    self.dave.jump_height = 31
            if pressed[pygame.K_RIGHT]:
                self.dave.x_speed += 1
            if pressed[pygame.K_LEFT]:
                self.dave.x_speed -= 1
            if pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]:
                if self.dave.has_gun and not self.dave.bullet:
                    self.dave.shoot()
            if game.dave.bullet:
                game.dave.bullet.move()
                bullet_collision(game)

            if True in pressed:
                self.dave.moved = True

            if not self.testing:
                check_collision(self.dave, self.level.tiles)
            if self.testing or self.dave.flying:
                self.dave.on_surface = True
                if pressed[pygame.K_DOWN]:
                    self.dave.on_surface = False
            self.score += check_obtained(self.dave, self.level.gems)
            if check_door(self.dave, self.level.doors):
                self.next_level()
            if check_death(self.dave, self.level.hazards) and not self.testing:
                running = False
                self.restart_level()
            if game.dave.bullet:
                bullet_hit(self)

            if self.dave.x >= 18.25 * 32 and self.dave.x_speed == 1:
                slide_over(self, -1)
            elif self.dave.x <= 1.75 * 32 and self.dave.x_speed == -1:
                slide_over(self, 1)

    def restart_level(self):
        self.dave.die(self)
        if self.lives == 0:
            sys.exit()
        self.lives -= 1
        obtained = self.dave.obtained()
        self.dave = Dave(self.level.dave_pos)
        self.dave.reset_obtained(obtained)
        offset = self.level.door_start[0] * 32 - self.level.doors.sprites()[0].rect.left
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

    def next_level(self):
        self.score += 2000
        self.lvl += 1

        self.level = NextLevel()
        self.dave = Dave(self.level.dave_pos)
        self.render()

        self.start()


game = Game(3)
game.start()
