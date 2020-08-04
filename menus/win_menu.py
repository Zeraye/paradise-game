import pygame
import variables
import main
from menus import main_menu


def draw(win):
    win.fill(variables.BLACK)
    win.blit(variables.win_screen_img, (((main.WIDTH - variables.win_screen_img.get_width()) / 2), (main.HEIGHT - variables.win_screen_img.get_height()) / 2))
    pygame.display.update()


def win_menu_func(win):
    run = True
    while run:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # keyboard handling
            if event.type == pygame.KEYDOWN:
                # return to menus
                if event.key == pygame.K_RETURN:
                    run = False
                    main_menu.main_menu_func(win)

        draw(win)
