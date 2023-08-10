import pygame

row_height = 52

decos_source = r"resources/tileset/decorations.png"
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
    decos = pygame.image.load(decos_source)
    score_banner = pygame.Surface((150, score_height)).convert_alpha()
    score_banner.blit(decos, (0, 0), score_rect)
    for index, digit in enumerate(map(int, str(curr_score))):
        score_banner.blit(decos, (60+9*index, 0), number_rects[digit])
    score_banner = pygame.transform.scale(score_banner, (265, 30))
    score_banner.set_colorkey((0, 0, 0))
    return score_banner
