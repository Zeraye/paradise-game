import pygame
import variables
from menus.main_menu import main_menu_func
import main


def starting_menu_func(win):
    win.fill(variables.BLACK)
    win.blit(variables.starting_menu_img, ((main.WIDTH-variables.starting_menu_img.get_width())/2, (main.HEIGHT-variables.starting_menu_img.get_height())/2))
    pygame.display.update()
    pygame.time.wait(5000)
    main_menu_func(win)
