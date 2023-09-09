import pygame

BG = (50, 50, 50)
row_height = 52

decos_source = r"resources/tileset/decorations.png"
decos = pygame.image.load(decos_source)
num_width = 8
score_width, score_height = 55, 11
score_rect = (270, 52, score_width, score_height)
number_rects = {
    i: (324 + i * 9, 52, 8, 11) for i in range(1, 10)
}
number_rects[0] = (414, row_height, num_width, score_height)


def score(current_score):
    score_banner = pygame.Surface((150, score_height)).convert_alpha()
    score_banner.blit(decos, (0, 0), score_rect)
    for index, digit in enumerate(map(int, str(current_score))):
        score_banner.blit(decos, (55 + 9 * index, 0), number_rects[digit])
    score_banner = pygame.transform.scale(score_banner, (265, 20))
    score_banner.set_colorkey((0, 0, 0))
    return score_banner


def go_thru():
    go_thru_message = pygame.Surface((175, 16)).convert_alpha()
    go_thru_message.blit(decos, (0, 0), (1, 65, 172, 14))
    go_thru_message = pygame.transform.scale(go_thru_message, (280, 28))
    go_thru_message.set_colorkey((0, 0, 0))
    return go_thru_message


def render_lives(lives):
    daves_rect = (144, 52, 50, 11)
    daves = pygame.Surface((110, 13)).convert_alpha()
    daves.blit(decos, (0, 1), daves_rect)
    for i in range(lives):
        daves.blit(decos, (55 + 18 * i, 0), (1, 51, 15, 12))
    daves = pygame.transform.scale(daves, (200, 22))
    daves.set_colorkey((0, 0, 0))
    return daves


def render_fuelbar(jetpack, jetpack_display):
    fuelbar_rect = (178, 67, 128, 12)
    fuelbar = pygame.Surface((128, 13)).convert_alpha()
    fuelbar.blit(decos, (0, 0), fuelbar_rect)
    # fuelbar = pygame.transform.scale(fuelbar, (128, 13))
    fuelcell_rect = (309, 76, 2, 3)
    halfcell_rect = (309, 76, 1, 3)
    fuel = pygame.Surface((120, 3)).convert_alpha()
    for i in range(jetpack // 2):
        fuel.blit(decos, (2 * i, 0), fuelcell_rect)
    if jetpack % 2 == 1:
        fuel.blit(decos, (2 * (jetpack // 2), 0), halfcell_rect)
    fuel = pygame.transform.scale(fuel, (120, 4))
    fuelbar.blit(fuel, (4, 4))
    jetpack_display.blit(fuelbar, (69, 0))
    return jetpack_display


def render_jetpack(jetpack):
    jetpack_word_rect = (18, 52, 62, 11)
    jetpack_display = pygame.Surface((300, 13)).convert_alpha()
    jetpack_display.blit(decos, (0, 0), jetpack_word_rect)
    jetpack_display = render_fuelbar(jetpack, jetpack_display)
    jetpack_display = pygame.transform.scale(jetpack_display, (600, 30))
    jetpack_display.set_colorkey((0, 0, 0))
    return jetpack_display


def render_gun():
    gun_location = (81, 52, 62, 11)
    gun_display = pygame.Surface((65, 13)).convert_alpha()
    gun_display.blit(decos, (0, 0), gun_location)
    gun_display = pygame.transform.scale(gun_display, (135, 30))
    gun_display.set_colorkey((0, 0, 0))
    return gun_display


def blit_border(game):
    empty_rect = (pygame.Surface((640, 16)))
    empty_rect.fill(BG)
    game.board.blit(empty_rect, (0, 346))
    border = pygame.image.load(r"resources/tileset/border.png")
    border = pygame.transform.scale(border, (640, 6))
    game.board.blit(border, (0, 32))
    game.board.blit(border, (0, 349))
    game.board.blit(score(game.score), (465, 10))
    game.board.blit(render_lives(game.lives), (3, 10))
    if game.dave.jetpack > 0:
        game.board.blit(render_jetpack(game.dave.jetpack), (20, 395))
    if game.dave.has_gun:
        game.board.blit(render_gun(), (500, 395))
    if game.dave.has_key:
        game.board.blit(go_thru(), (180, 358))
