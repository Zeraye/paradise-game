import pygame
import variables
import time
from board import board
from menus import main_menu
from scripts import contain, reformated_number
import menus.death_menu


def draw_board_squares(win):
    i = j = 0
    while i < 11:
        while j < 11:
            # type 0 -> NOTHING
            if contain(board[i][j], 0):
                pygame.draw.rect(win, variables.WHITE, (variables.side_border + i * variables.side_length, variables.top_border + j * variables.side_length, variables.side_length, variables.side_length))
            # type 2 is only for ObstacleExclusively
            # type 3 -> PHASE 1
            if contain(board[i][j], 3):
                pygame.draw.rect(win, variables.GREEN, (variables.side_border + i * variables.side_length, variables.top_border + j * variables.side_length, variables.side_length, variables.side_length))
            # type 4 -> PHASE 2 (deadly)
            if contain(board[i][j], 4):
                pygame.draw.rect(win, variables.RED, (variables.side_border + i * variables.side_length, variables.top_border + j * variables.side_length, variables.side_length, variables.side_length))
            # type 5 -> PHASE 1 (ObstacleSquare)
            if contain(board[i][j], 5):
                win.blit(variables.square_img, (variables.side_border + i * variables.side_length, variables.top_border + j * variables.side_length))
            # type 6 -> PHASE 1 (ObstacleCross)
            if contain(board[i][j], 6):
                win.blit(variables.corss_img, (variables.side_border + i * variables.side_length, variables.top_border + j * variables.side_length))
            # type 7 -> PHASE 1 (ObstacleBigCross)
            if contain(board[i][j], 7):
                win.blit(variables.bigcross_img, (variables.side_border + i * variables.side_length, variables.top_border + j * variables.side_length))
            # type 8 -> PHASE 1 (ObstacleDiagonal)
            if contain(board[i][j], 8):
                win.blit(variables.diagonal_img, (variables.side_border + i * variables.side_length, variables.top_border + j * variables.side_length))
            # type 1 -> PLAYER
            if contain(board[i][j], 1):
                pygame.draw.rect(win, variables.BLACK, (round(variables.side_border + i * variables.side_length + (variables.side_length / 4)), round(variables.top_border + j * variables.side_length + (variables.side_length / 4)), round(variables.side_length / 2), round(variables.side_length / 2)))
            j += 1
        j = 0
        i += 1


def draw_board_lines(win):
    i = j = 0
    while i <= 11:
        while j <= 11:
            pygame.draw.line(win, variables.BLACK, (variables.side_border + variables.side_length * i, variables.top_border), (variables.side_border + variables.side_length * i, variables.top_border + variables.side_length * 11))
            pygame.draw.line(win, variables.BLACK, (variables.side_border, variables.top_border + variables.side_length * j), (variables.side_border + variables.side_length * 11, variables.top_border + variables.side_length * j))
            j += 1
        j = 0
        i += 1


def draw_death_screen(win):
    font = pygame.font.SysFont('lucidaconsole', variables.font_size_80)
    game_time = round(variables.death_time - variables.start_game_time)
    textsurface = font.render('YOU HAVE LOST!', False, variables.WHITE)
    win.blit(textsurface, ((main_menu.WIDTH - textsurface.get_width()) / 2, (((main_menu.HEIGHT - textsurface.get_height()) / 2) - 100)))
    textsurface = font.render(('TIME: ' + str(game_time)), False, variables.WHITE)
    win.blit(textsurface, ((main_menu.WIDTH - textsurface.get_width()) / 2, (((main_menu.HEIGHT - textsurface.get_height()) / 2) + 0)))
    textsurface = font.render('CLICK R TO PLAY AGAIN!', False, variables.WHITE)
    win.blit(textsurface, ((main_menu.WIDTH - textsurface.get_width()) / 2, (((main_menu.HEIGHT - textsurface.get_height()) / 2) + 100)))


def draw_progress(win):
    font = pygame.font.Font('fonts/ARCADECLASSIC.TTF', 80)
    textsurface = font.render(str(reformated_number(121 - round(time.time() - variables.start_game_time))), False, variables.WHITE)
    win.blit(textsurface, (0, 0))


def draw(win):
    win.fill(variables.BLACK)
    draw_board_squares(win)
    draw_board_lines(win)
    draw_progress(win)
    if variables.death:
        menus.death_menu.death_menu_func(win)
    pygame.display.update()
