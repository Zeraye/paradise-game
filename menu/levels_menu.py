import pygame
import levels.level01
import draw
from menu import main_menu

levels_list = [
    [True, False, False, False],
    [False, False, False, False],
    [False, False, False, False]
]


def draw_title(win):
    font = pygame.font.SysFont('lucidaconsole', 80)
    textsurface = font.render('Levels', False, draw.RED)
    win.blit(textsurface, (round((main_menu.WIDTH - textsurface.get_width()) / 2), 50))


def draw_levels(win):
    font = pygame.font.SysFont('lucidaconsole', 60)
    i = j = 0
    level = 1
    while i < 3:
        while j < 4:
            textsurface = font.render('Level ' + str(level), False, draw.WHITE)
            win.blit(textsurface, (64 + 200 + j * (400 + 64) - textsurface.get_width()/2, 153 + 122 + i * (245 + 64) - textsurface.get_height()/2))
            level += 1
            j += 1
        j = 0
        i += 1


def search_selection():
    i = j = 0
    while i < 3:
        while j < 4:
            if levels_list[i][j]:
                return i, j
            j += 1
        j = 0
        i += 1
    return -1, -1


def draw_selection(win):
    i, j = search_selection()
    if not i < 0:
        pygame.draw.rect(win, draw.RED, (64 + j * (400 + 64), 153 + i * (245 + 64), 400, 245))
        pygame.display.flip()


def levels_clear():
    i = j = 0
    while i < 3:
        while j < 4:
            levels_list[i][j] = False
            j += 1
        j = 0
        i += 1


def draw_menu(win):
    win.fill(draw.YELLOW)
    draw_selection(win)
    draw_title(win)
    draw_levels(win)
    pygame.display.update()


def levels_menu(win):
    draw_menu(win)
    run = True
    while run:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                i, j = search_selection()
                if event.key == pygame.K_RETURN:
                    level = i * 4 + j + 1
                    if level == 1:
                        levels.level01.main(win)

                if event.key == pygame.K_RIGHT and j < 3:
                    levels_clear()
                    levels_list[i][j + 1] = True
                elif event.key == pygame.K_RIGHT and j == 3 and i < 2:
                    levels_clear()
                    levels_list[i + 1][0] = True
                elif event.key == pygame.K_LEFT and j > 0:
                    levels_clear()
                    levels_list[i][j - 1] = True
                elif event.key == pygame.K_LEFT and j == 0 and i > 0:
                    levels_clear()
                    levels_list[i - 1][3] = True
                elif event.key == pygame.K_UP and i > 0:
                    levels_clear()
                    levels_list[i - 1][j] = True
                elif event.key == pygame.K_DOWN and i < 2:
                    levels_clear()
                    levels_list[i + 1][j] = True

                draw_menu(win)