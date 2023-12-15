from banner import *
from tiles import *
from builtins import map
from operator import add


def edge_check(tiles, direction):
    if direction == 1:
        return min(tile.rect.left for tile in tiles) < 0
    else:
        return max(tile.rect.right for tile in tiles) / 32 > 20


def slide_over(game, direction):
    sprite_groups = [x for x in dir(game.level) if not x.__contains__('_')]
    counter = 0
    while edge_check(game.level.tiles, direction) and counter < 15:
        pygame.time.delay(10)
        counter += 1
        game.board.fill(BG)
        for sprite_group in sprite_groups:
            eval(f"move_over(game.level.{sprite_group}, direction)")
        for mob in game.level.mobs:
            mob.pos += pygame.math.Vector2(direction * 32, 0)
        render_level(game)
        blit_border(game)
        pygame.display.flip()
    game.dave.x += counter * direction * 32
    if game.dave.bullet:
        game.dave.bullet.x += counter * direction * 32
    for mob in game.level.mobs:
        if mob.bullet:
            mob.bullet.x += counter * direction * 32
    for mob in game.level.mobs:
        new_waypoints = []
        for waypoint in mob.waypoints:
            new_waypoint = tuple(map(add, waypoint, (counter * direction * 32, 0)))
            new_waypoints.append(new_waypoint)
        mob.waypoints = new_waypoints


def move_over(sprite_group, direction):
    for sprite in sprite_group.sprites():
        sprite.rect = sprite.rect.move(direction * 32, 0)


def render(game):
    game.board.fill(BG)
    render_level(game)
    game.dave.move()
    if game.dave.bullet:
        game.board.blit(*game.dave.bullet.get_location())
    for mob in game.level.mobs:
        if mob.bullet:
            game.board.blit(*mob.bullet.get_location())
    game.board.blit(game.dave.current_display(), game.dave.position())
    blit_border(game)
    curr_tick = pygame.time.get_ticks()
    if curr_tick - game.last_flip > 20:
        game.last_flip = curr_tick
        pygame.display.flip()


def render_level(game):
    sprite_groups = [x for x in dir(game.level) if not x.__contains__('_')]
    for sprite_group in sprite_groups:
        sprite_group = eval(f"game.level.{sprite_group}")
        for renderable in sprite_group.sprites():
            game.board.blit(*sprite_group.render_image(renderable))


def reset_position(level, offset):
    sprite_groups = [x for x in dir(level) if not x.__contains__('_')]
    for sprite_group in sprite_groups:
        sprite_group = eval(f"level.{sprite_group}")
        for renderable in sprite_group.sprites():
            renderable.rect = renderable.rect.move(offset, 0)
    for mob in level.mobs:
        new_waypoints = []
        for waypoint in mob.waypoints:
            new_waypoint = tuple(map(add, waypoint, (offset, 0)))
            new_waypoints.append(new_waypoint)
        mob.waypoints = new_waypoints
        mob.pos += pygame.math.Vector2(offset, 0)
