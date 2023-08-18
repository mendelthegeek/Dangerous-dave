import pygame

BG = (50, 50, 50)
row_height = 52

decos_source = r"resources/tileset/decorations.png"
decos = pygame.image.load(decos_source)
num_width = 8
score_width, score_height = 55, 11
score_rect = (270, 52, score_width, score_height)
number_rects = {
    i: (333 + i*9, 52, 8, 11) for i in range(1, 10)
}
number_rects[0] = (414, row_height, num_width, score_height)


def score(current_score):
    score_banner = pygame.Surface((150, score_height)).convert_alpha()
    score_banner.blit(decos, (0, 0), score_rect)
    for index, digit in enumerate(map(int, str(current_score))):
        score_banner.blit(decos, (60 + 9 * index, 0), number_rects[digit])
    score_banner = pygame.transform.scale(score_banner, (265, 20))
    score_banner.set_colorkey((0, 0, 0))
    return score_banner

def go_thru():
    go_thru_message = pygame.Surface((175, 16)).convert_alpha()
    go_thru_message.blit(decos, (0, 0), (1, 63, 172, 16))
    go_thru_message = pygame.transform.scale(go_thru_message, (280, 28))
    go_thru_message.set_colorkey((0, 0, 0))
    return go_thru_message


def lives(lives):
    daves_rect = (144, 52, 50, 11)
    daves = pygame.Surface((100, 11)).convert_alpha()
    daves.blit(decos, (0, 0), daves_rect)
    for i in range(lives):
        daves.blit(decos, (55 + 16 * i, 0), (1, 52, 15, 11))
    daves = pygame.transform.scale(daves, (200, 20))
    daves.set_colorkey((0, 0, 0))
    return daves


def blit_border(game):
    empty_rect = (pygame.Surface((640, 16)))
    empty_rect.fill(BG)
    game.board.blit(empty_rect, (0, 346))
    border = pygame.image.load(r"resources/tileset/border.png")
    border = pygame.transform.scale(border, (640, 6))
    game.board.blit(border, (0, 32))
    game.board.blit(border, (0, 349))
    game.board.blit(score(game.score), (450, 6))
    game.board.blit(lives(game.lives), (20, 6))
    if game.dave.has_key:
        game.board.blit(go_thru(), (180, 358))
