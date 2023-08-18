from physics import *
from render import *
from levels import *
import sys


class Game:
    def start(self, lvl, curr_score=0):
        pygame.init()

        self.level = eval(f"Level{lvl}()")
        dave = Dave(self.level.dave_pos)
        icon = self.level.tiles.sprite_sheet.get_sprite(5, 4, 16, 16, 2)
        pygame.display.set_caption("Dangerous Dave")
        pygame.display.set_icon(icon)
        next_lev = False

        curr_score = self.run(dave, self.level, curr_score)

        NextLevel(curr_score)

        self.start(lvl + 1, curr_score)

    def run(self, dave, level, curr_score):
        running = True
        while running:
            if curr_score >= 100000:
                curr_score = 99999

            render(dave, level, curr_score)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            dave.x_speed = 0
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                if dave.on_surface and dave.jump_height == 0:
                    dave.jump_height += 94
            if pressed[pygame.K_RIGHT]:
                dave.x_speed += 1
            if pressed[pygame.K_LEFT]:
                dave.x_speed -= 1

            if len(pressed) > 0:
                dave.moved = True

            curr_score += check_obtained(dave, level.gems)
            check_collision(dave, level.tiles)
            if check_death(dave, level.hazards):
                sys.exit()
            if check_door(dave, level.doors):
                curr_score += 2000
                return curr_score

            if dave.x == 18.5 * 32 and dave.x_speed == 1:
                slide_over(dave, level, curr_score, -1)
            elif dave.x == 1.5 * 32 and dave.x_speed == -1:
                slide_over(dave, level, curr_score, 1)

game = Game()
game.start(1)
