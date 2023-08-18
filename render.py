from banner import *
from player import *
from tiles import *

board = pygame.display.set_mode((640, 392))


def edge_check(tiles, direction):
    if direction == 1:
        return min(tile.rect.left for tile in tiles) < 0
    else:
        return max(tile.rect.right for tile in tiles)/32 > 20


def slide_over(dave, level, curr_score, direction):
    sprite_groups = [level.tiles, level.doors, level.gems, level.hazards]
    counter = 0
    while edge_check(level.tiles, direction) and counter < 16:
        pygame.time.delay(10)
        counter += 1
        board.fill(BG)
        for sprite_group in sprite_groups:
            move_over(sprite_group, direction)
        blit_border(board, curr_score, dave.has_key)
        render_level(level)
        pygame.display.flip()
    dave.x += counter*direction*32


def move_over(sprite_group, direction):
    for sprite in sprite_group.sprites():
        sprite.rect = sprite.rect.move(direction * 32, 0)


def render(dave, level, curr_score):
    board.fill(BG)
    current_time = pygame.time.get_ticks()
    render_level(level)
    if current_time - dave.last_update > dave.speed:
        dave.move()
        dave.last_update = current_time
    board.blit(dave.current_display(), dave.position())
    blit_border(board, curr_score, dave.has_key)
    pygame.display.flip()


def render_level(level):
    sprite_groups = [level.tiles, level.doors, level.gems, level.hazards]
    for sprite_group in sprite_groups:
        for renderable in sprite_group.sprites():
            board.blit(*sprite_group.render_image(renderable))
