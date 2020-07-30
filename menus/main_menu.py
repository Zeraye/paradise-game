import pygame
import variables
from menus.levels_menu import levels_menu_func

pygame.init()
screenObject = pygame.display.Info()
WIDTH = screenObject.current_w
HEIGHT = screenObject.current_h
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Paradise')


def draw_title(win):
    font = pygame.font.SysFont('lucidaconsole', variables.font_size_100, bold=True)
    textsurface = font.render("Don't touch RED square!", False, variables.RED)
    win.blit(textsurface, (round(WIDTH - textsurface.get_width()) / 2, round((HEIGHT - textsurface.get_height()) / 2) - 100))


def draw_start(win):
    font = pygame.font.SysFont('lucidaconsole', variables.font_size_80)
    textsurface = font.render("Click ENTER to start game", False, variables.BLUE_LIGT)
    win.blit(textsurface, (round(WIDTH - textsurface.get_width()) / 2, round((HEIGHT - textsurface.get_height()) / 2) + 100))


def draw_menu(win):
    win.fill(variables.YELLOW)
    draw_title(win)
    draw_start(win)
    pygame.display.update()


def main_menu_func(win):
    run = True
    while run:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    levels_menu_func(win)

                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()

        draw_menu(win)


main_menu_func(WIN)
