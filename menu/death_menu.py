import pygame
import levels.level01
import draw
from menu import main_menu


def draw_texts(win):
    font = pygame.font.SysFont('lucidaconsole', 100, bold=True)
    textsurface = font.render("Don't touch RED square!", False, draw.RED)
    win.blit(textsurface, (round(main_menu.WIDTH - textsurface.get_width()) / 2, round((main_menu.HEIGHT - textsurface.get_height()) / 2) - 150))
    font = pygame.font.SysFont('lucidaconsole', 80)
    textsurface = font.render('Click ENTER to return to menu', False, draw.BLUE_LIGT)
    win.blit(textsurface, (round(main_menu.WIDTH - textsurface.get_width()) / 2, round((main_menu.HEIGHT - textsurface.get_height()) / 2) + 50))
    textsurface = font.render('Click R to restart game', False, draw.BLUE_LIGT)
    win.blit(textsurface, (round(main_menu.WIDTH - textsurface.get_width()) / 2, round((main_menu.HEIGHT - textsurface.get_height()) / 2) + 250))


def draw_menu(win):
    win.fill(draw.YELLOW)
    draw_texts(win)
    pygame.display.update()


def death_menu(win):
    run = True
    while run:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # keyboard handling
            if event.type == pygame.KEYDOWN:
                # return to menu
                if event.key == pygame.K_RETURN:
                    levels.level01.death = False
                    run = False
                    main_menu.main_menu(win)
                # restart game
                if event.key == pygame.K_r:
                    levels.level01.death = False
                    run = False

        draw_menu(win)
