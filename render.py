from banner import *
from player import *
from tiles import *

board = pygame.display.set_mode((640, 392))


def render(dave, tiles, gems, doors, curr_score):
    board.fill(BG)
    current_time = pygame.time.get_ticks()
    for tile in tiles.sprites():
        board.blit(tile.image, tile.rect)
    for door in doors.sprites():
        board.blit(door.image, door.rect)
    for gem in gems.sprites():
        if gem.gem_type == "trophy":
            board.blit(*gem.get_image())
        else:
            board.blit(gem.image, gems.unpad(gem.rect))
    if current_time - dave.last_update > dave.speed:
        dave.move()
        dave.last_update = current_time
    board.blit(dave.current_display(), dave.position())
    if dave.has_key:
        board.blit(go_thru(), (180, 358))
    blit_border(board, curr_score)
    pygame.display.flip()
