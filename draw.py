import pygame
from board import board
from menu import main_menu
from levels import level01
from scripts import contain
import menu.death_menu


# colors
BLUE_DARK = (0, 132, 255)
BLUE_LIGT = (68, 190, 199)
YELLOW = (255, 195, 0)
ORANGE = (255, 165, 0)
RED = (250, 60, 76)
VIOLET = (71, 39, 71)
WHITE = (255, 255, 255)
GREEN = (127, 255, 0)

# basic lengths
top_border = 200
side_border = 575
side_length = 70


def draw_board_squares(win):
    global top_border, side_border, side_length
    i = j = 0
    while i < 11:
        while j < 11:
            # type 0 -> NOTHING
            if contain(board[i][j], 0):
                pygame.draw.rect(win, BLUE_LIGT, (side_border + i * side_length, top_border + j * side_length, side_length, side_length))
            # type 2 is only for ObstacleExclusively
            # type 3 -> PHASE 1
            if contain(board[i][j], 3):
                pygame.draw.rect(win, GREEN, (side_border + i * side_length, top_border + j * side_length, side_length, side_length))
            # type 4 -> PHASE 2 (deadly)
            if contain(board[i][j], 4):
                pygame.draw.rect(win, RED, (side_border + i * side_length, top_border + j * side_length, side_length, side_length))
            # type 1 -> PLAYER
            if contain(board[i][j], 1):
                pygame.draw.rect(win, BLUE_DARK, (side_border + i * side_length + (side_length / 4), top_border + j * side_length + (side_length / 4), side_length / 2, side_length / 2))
            j += 1
        j = 0
        i += 1


def draw_board_lines(win):
    global top_border, side_border, side_length
    i = j = 0
    while i <= 11:
        while j <= 11:
            pygame.draw.line(win, WHITE, (side_border + side_length * i, top_border), (side_border + side_length * i, top_border + side_length * 11))
            pygame.draw.line(win, WHITE, (side_border, top_border + side_length * j), (side_border + side_length * 11, top_border + side_length * j))
            j += 1
        j = 0
        i += 1


def draw_death_screen(win):
    font = pygame.font.SysFont('lucidaconsole', 80)
    game_time = round(level01.death_time - level01.start_game_time)
    textsurface = font.render('YOU HAVE LOST!', False, WHITE)
    win.blit(textsurface, ((main_menu.WIDTH - textsurface.get_width()) / 2, (((main_menu.HEIGHT - textsurface.get_height()) / 2) - 100)))
    textsurface = font.render(('TIME: ' + str(game_time)), False, WHITE)
    win.blit(textsurface, ((main_menu.WIDTH - textsurface.get_width()) / 2, (((main_menu.HEIGHT - textsurface.get_height()) / 2) + 0)))
    textsurface = font.render('CLICK R TO PLAY AGAIN!', False, WHITE)
    win.blit(textsurface, ((main_menu.WIDTH - textsurface.get_width()) / 2, (((main_menu.HEIGHT - textsurface.get_height()) / 2) + 100)))


def draw(win):
    win.fill(YELLOW)
    draw_board_squares(win)
    draw_board_lines(win)
    if level01.death:
        menu.death_menu.death_menu(win)
    pygame.display.update()
