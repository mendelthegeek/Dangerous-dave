from banner import *
from tiles import *


def edge_check(tiles, direction):
    if direction == 1:
        return min(tile.rect.left for tile in tiles) < 0
    else:
        return max(tile.rect.right for tile in tiles) / 32 > 20


def slide_over(game, direction):
    sprite_groups = [game.level.tiles, game.level.doors, game.level.gems, game.level.hazards]
    counter = 0
    while edge_check(game.level.tiles, direction) and counter < 16:
        pygame.time.delay(10)
        counter += 1
        game.board.fill(BG)
        for sprite_group in sprite_groups:
            move_over(sprite_group, direction)
        render_level(game.level, game.board)
        blit_border(game)
        pygame.display.flip()
    game.dave.x += counter * direction * 32


def move_over(sprite_group, direction):
    for sprite in sprite_group.sprites():
        sprite.rect = sprite.rect.move(direction * 32, 0)


def render(game):
    game.board.fill(BG)
    current_time = pygame.time.get_ticks()
    render_level(game.level, game.board)
    if current_time - game.dave.last_update > game.dave.speed:
        game.dave.move()
        game.dave.last_update = current_time
    game.board.blit(game.dave.current_display(), game.dave.position())
    blit_border(game)
    pygame.display.flip()


def render_level(level, board):
    sprite_groups = [level.tiles, level.doors, level.gems, level.hazards]
    for sprite_group in sprite_groups:
        for renderable in sprite_group.sprites():
            board.blit(*sprite_group.render_image(renderable))


def reset_position(level, offset):
    sprite_groups = [level.tiles, level.doors, level.gems, level.hazards]
    for sprite_group in sprite_groups:
        for renderable in sprite_group.sprites():
            renderable.rect = renderable.rect.move(offset, 0)
