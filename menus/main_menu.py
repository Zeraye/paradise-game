import pygame
import variables
from menus.levels_menu import levels_menu_func
from menus.options_menu import options_menu_func
import main

menu = 0


def draw_main_menu(win, menu):
    if menu == 0:
        win.blit(variables.main_menu_img, ((main.WIDTH-variables.main_menu_img.get_width())/2, (main.HEIGHT-variables.main_menu_img.get_height())/2))
    elif menu == 1:
        win.blit(variables.main_menu_start_img, ((main.WIDTH-variables.main_menu_start_img.get_width())/2, (main.HEIGHT-variables.main_menu_start_img.get_height())/2))
    elif menu == 2:
        win.blit(variables.main_menu_options_img, ((main.WIDTH-variables.main_menu_options_img.get_width())/2, (main.HEIGHT-variables.main_menu_options_img.get_height())/2))
    elif menu == 3:
        win.blit(variables.main_menu_quit_img, ((main.WIDTH-variables.main_menu_quit_img.get_width())/2, (main.HEIGHT-variables.main_menu_quit_img.get_height())/2))

def draw_menu(win, menu):
    win.fill(variables.BLACK)
    draw_main_menu(win, menu)
    pygame.display.update()


def main_menu_func(win):
    global menu
    run = True
    while run:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if menu == 1:
                        menu = 0
                        levels_menu_func(win)
                    if menu == 2:
                        menu = 0
                        options_menu_func(win)
                    if menu == 3:
                        run = False
                        pygame.quit()

                elif event.key == pygame.K_UP and menu > 0:
                    menu -= 1

                elif event.key == pygame.K_DOWN and menu < 3:
                    menu += 1

        draw_menu(win, menu)
