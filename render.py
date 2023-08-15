from banner import *
from player import *
from tiles import *

board = pygame.display.set_mode((640, 392))


def render(dave, tiles, hazards, gems, doors, curr_score):
    board.fill(BG)
    current_time = pygame.time.get_ticks()
    for tile in tiles.sprites():
        board.blit(*tiles.render_image(tile))
    for door in doors.sprites():
        board.blit(*doors.render_image(door))
    for gem in gems.sprites():
        board.blit(*gems.render_image(gem))
    for hazard in hazards.sprites():
        board.blit(*hazards.render_image(hazard))
    if current_time - dave.last_update > dave.speed:
        dave.move()
        dave.last_update = current_time
    board.blit(dave.current_display(), dave.position())
    blit_border(board, curr_score, dave.has_key)
    pygame.display.flip()
