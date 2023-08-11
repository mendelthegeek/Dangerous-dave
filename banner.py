import pygame

BG = (50, 50, 50)
row_height = 52

decos_source = r"resources/tileset/decorations.png"
decos = pygame.image.load(decos_source)
num_width = 8
score_width, score_height = 55, 11
score_rect = (270, 52, score_width, score_height)
number_rects = {
    1: (333, row_height, num_width, score_height),
    2: (342, row_height, num_width, score_height),
    3: (351, row_height, num_width, score_height),
    4: (360, row_height, num_width, score_height),
    5: (369, row_height, num_width, score_height),
    6: (378, row_height, num_width, score_height),
    7: (387, row_height, num_width, score_height),
    8: (396, row_height, num_width, score_height),
    9: (405, row_height, num_width, score_height),
    0: (414, row_height, num_width, score_height),
}


def score(curr_score):
    score_banner = pygame.Surface((150, score_height)).convert_alpha()
    score_banner.blit(decos, (0, 0), score_rect)
    for index, digit in enumerate(map(int, str(curr_score))):
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

def blit_border(board, curr_score):
    empty_rect = (pygame.Surface((640, 16)))
    empty_rect.fill(BG)
    board.blit(empty_rect, (0, 346))
    border = pygame.image.load(r"resources/tileset/border.png")
    border = pygame.transform.scale(border, (640, 6))
    board.blit(border, (0, 32))
    board.blit(border, (0, 349))
    board.blit(score(curr_score), (450, 6))