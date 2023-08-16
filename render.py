from banner import *
from player import *
from tiles import *

board = pygame.display.set_mode((640, 392))


def render(dave, level, curr_score):
    board.fill(BG)
    current_time = pygame.time.get_ticks()
    for tile in level.tiles.sprites():
        board.blit(*level.tiles.render_image(tile))
    for door in level.doors.sprites():
        board.blit(*level.doors.render_image(door))
    for gem in level.gems.sprites():
        board.blit(*level.gems.render_image(gem))
    for hazard in level.hazards.sprites():
        board.blit(*level.hazards.render_image(hazard))
    if current_time - dave.last_update > dave.speed:
        dave.move()
        dave.last_update = current_time
    board.blit(dave.current_display(), dave.position())
    blit_border(board, curr_score, dave.has_key)
    pygame.display.flip()
