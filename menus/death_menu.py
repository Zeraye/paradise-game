import pygame
import variables
from menus import main_menu


def draw_texts(win):
    font = pygame.font.SysFont('lucidaconsole', variables.font_size_100, bold=True)
    textsurface = font.render("Don't touch RED square!", False, variables.RED)
    win.blit(textsurface, (round(main_menu.WIDTH - textsurface.get_width()) / 2, round((main_menu.HEIGHT - textsurface.get_height()) / 2) - 250))
    font = pygame.font.SysFont('lucidaconsole', variables.font_size_80)
    textsurface = font.render('You have lost!', False, variables.BLUE_LIGT)
    win.blit(textsurface, (round(main_menu.WIDTH - textsurface.get_width()) / 2, round((main_menu.HEIGHT - textsurface.get_height()) / 2) - 100))
    textsurface = font.render('Click ENTER to return to menus', False, variables.BLUE_LIGT)
    win.blit(textsurface, (round(main_menu.WIDTH - textsurface.get_width()) / 2, round((main_menu.HEIGHT - textsurface.get_height()) / 2) + 50))
    textsurface = font.render('Click R to restart level', False, variables.BLUE_LIGT)
    win.blit(textsurface, (round(main_menu.WIDTH - textsurface.get_width()) / 2, round((main_menu.HEIGHT - textsurface.get_height()) / 2) + 200))


def draw_menu(win):
    win.fill(variables.YELLOW)
    draw_texts(win)
    pygame.display.update()


def death_menu_func(win):
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
                    variables.death = False
                    run = False
                    main_menu.main_menu_func(win)
                # restart game
                if event.key == pygame.K_r:
                    variables.death = False
                    run = False

        draw_menu(win)
