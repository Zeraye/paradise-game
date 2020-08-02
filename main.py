import pygame
import menus.starting_screen

pygame.init()

pygame.mouse.set_visible(False)

screenObject = pygame.display.Info()
WIDTH = screenObject.current_w
HEIGHT = screenObject.current_h
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Paradise')

if __name__ == '__main__':
    menus.starting_screen.starting_menu_func(WIN)
