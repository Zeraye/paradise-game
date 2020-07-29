import pygame
import draw
from menu.levels_menu import levels_menu

pygame.init()

WIDTH = 1920
HEIGHT = 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Paradise')


def draw_title(win):
    font = pygame.font.SysFont('lucidaconsole', 100, bold=True)
    textsurface = font.render("Don't touch RED square!", False, draw.RED)
    win.blit(textsurface, (round(WIDTH - textsurface.get_width()) / 2, round((HEIGHT - textsurface.get_height()) / 2) - 100))


def draw_start(win):
    font = pygame.font.SysFont('lucidaconsole', 80)
    textsurface = font.render("Click ENTER to start game", False, draw.BLUE_LIGT)
    win.blit(textsurface, (round(WIDTH - textsurface.get_width()) / 2, round((HEIGHT - textsurface.get_height()) / 2) + 100))


def draw_menu(win):
    win.fill(draw.YELLOW)
    draw_title(win)
    draw_start(win)
    pygame.display.update()


def main_menu(win):
    run = True
    while run:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    levels_menu(win)

        draw_menu(win)


main_menu(WIN)
