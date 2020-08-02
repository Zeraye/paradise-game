import pygame
import os

pygame.init()
screenObject = pygame.display.Info()
# basic lengths
top_border = round((200 * screenObject.current_h) / 1080)
side_border = round((575 * screenObject.current_w) / 1920)
side_length = round((70 * screenObject.current_w) / 1920)
gap = round((64 * screenObject.current_w) / 1920)


def scale(length):
    return round((length * screenObject.current_w) / 1920)


# importing images
pygame.display.set_mode((screenObject.current_w, screenObject.current_h), pygame.FULLSCREEN)
square_img = pygame.image.load(os.path.join(os.getcwd(), './images/Square.png')).convert_alpha()
square_img = pygame.transform.scale(square_img, (side_length, side_length))
corss_img = pygame.image.load(os.path.join(os.getcwd(), './images/Cross.png')).convert_alpha()
corss_img = pygame.transform.scale(corss_img, (side_length, side_length))
bigcross_img = pygame.image.load(os.path.join(os.getcwd(), './images/BigCross.png')).convert_alpha()
bigcross_img = pygame.transform.scale(bigcross_img, (side_length, side_length))
diagonal_img = pygame.image.load(os.path.join(os.getcwd(), './images/Diagonal.png')).convert_alpha()
diagonal_img = pygame.transform.scale(diagonal_img, (side_length, side_length))

main_menu_img = pygame.image.load(os.path.join(os.getcwd(), './images/MainMenu.png'))
main_menu_img = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), './images/MainMenu.png')), (round((main_menu_img.get_width()*screenObject.current_w)/1920), round((main_menu_img.get_height()*screenObject.current_h)/1080)))
main_menu_start_img = pygame.image.load(os.path.join(os.getcwd(), './images/MainMenuStart.png'))
main_menu_start_img = pygame.transform.scale(main_menu_start_img, (round((main_menu_start_img.get_width()*screenObject.current_w)/1920), round((main_menu_start_img.get_height()*screenObject.current_h)/1080)))
main_menu_options_img = pygame.image.load(os.path.join(os.getcwd(), './images/MainMenuOptions.png'))
main_menu_options_img = pygame.transform.scale(main_menu_options_img, (round((main_menu_options_img.get_width()*screenObject.current_w)/1920), round((main_menu_options_img.get_height()*screenObject.current_h)/1080)))
main_menu_quit_img = pygame.image.load(os.path.join(os.getcwd(), './images/MainMenuQuit.png'))
main_menu_quit_img = pygame.transform.scale(main_menu_quit_img, (round((main_menu_quit_img.get_width()*screenObject.current_w)/1920), round((main_menu_quit_img.get_height()*screenObject.current_h)/1080)))
starting_menu_img = pygame.image.load(os.path.join(os.getcwd(), './images/StartingMenu.png'))
starting_menu_img = pygame.transform.scale(starting_menu_img, (round((starting_menu_img.get_width()*screenObject.current_w)/1920), round((starting_menu_img.get_height()*screenObject.current_h)/1080)))


# colors
BLUE_DARK = (0, 132, 255)
BLUE_LIGT = (68, 190, 199)
YELLOW = (255, 195, 0)
ORANGE = (255, 165, 0)
RED = (250, 60, 76)
VIOLET = (71, 39, 71)
WHITE = (255, 255, 255)
GREEN = (127, 255, 0)
BLACK = (0, 0, 0)


# gameplay settings
obstacles_list = []
obstacles_homing_list = []

homing = False
last_homing_pos = [0, 0]

delay = 2.3
death = False

death_time = start_game_time = 0

current_obstacle_number = 0


# fonts
font_size_100 = round((100 * screenObject.current_w) / 1920)
font_size_80 = round((80 * screenObject.current_w) / 1920)
font_size_60 = round((60 * screenObject.current_w) / 1920)
