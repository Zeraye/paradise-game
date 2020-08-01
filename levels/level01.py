import pygame
import draw
import time
import variables
import random
from player import Player
from menus.death_menu import death_menu_func
from menus.win_menu import win_menu_func
from scripts import check_border, reset_board, check_death, print_board, give_randon, random_array
from obstacles import ObstacleSquare, ObstacleCross, ObstacleLines, ObstacleBigCross, ObstacleHoming, ObstacleExclusively, ObstacleBoard1, ObstacleBoard2, ObstacleRandomSafe


def main(win):
    reset_board()
    p = Player(5, 5)
    p.p_update_pos(5, 5)
    last_obstacle_time = variables.start_game_time = time.time()
    time_between_obstacles = 3
    run = True
    while run:
        curr_time = time.time()
        pygame.time.Clock().tick(60)
        if time.time() - variables.start_game_time > 10:
            variables.start_game_time = time.time()
            win_menu_func(win)
        if not variables.homing:
            variables.homing = True
            time.sleep(0.001)
            new_obstacle = ObstacleHoming(time.time(), variables.delay, p.p_get_pos())
            new_obstacle.set_obstacle()
            variables.obstacles_homing_list.append(new_obstacle)
            time.sleep(0.001)
        # if curr_time - last_obstacle_time > time_between_obstacles and not variables.death:
        #     time.sleep(0.001)
        #     last_obstacle_time = time.time()
        #     new_obstacle = ObstacleBoard2(time.time(), variables.delay)
        #     variables.obstacles_list.append(new_obstacle)
        #     time.sleep(0.001)
        #     new_obstacle = ObstacleSquare(time.time(), variables.delay, give_randon(1, 9), give_randon(1, 9))
        #     variables.obstacles_list.append(new_obstacle)
        #     time.sleep(0.001)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            # keyboard handling
            if event.type == pygame.KEYDOWN:
                # only for dev
                if event.key == pygame.K_q:
                    pass
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                if not variables.death and not pygame.key.get_pressed()[pygame.K_SPACE]:
                    if event.key == pygame.K_w and check_border(p.p_get_pos()[1] - 1):
                        variables.death = p.p_update_pos(p.p_get_pos()[0], p.p_get_pos()[1] - 1)
                    elif event.key == pygame.K_s and check_border(p.p_get_pos()[1] + 1):
                        variables.death = p.p_update_pos(p.p_get_pos()[0], p.p_get_pos()[1] + 1)
                    elif event.key == pygame.K_a and check_border(p.p_get_pos()[0] - 1):
                        variables.death = p.p_update_pos(p.p_get_pos()[0] - 1, p.p_get_pos()[1])
                    elif event.key == pygame.K_d and check_border(p.p_get_pos()[0] + 1):
                        variables.death = p.p_update_pos(p.p_get_pos()[0] + 1, p.p_get_pos()[1])
                # moving with space (longer distance)
                if not variables.death and pygame.key.get_pressed()[pygame.K_SPACE]:
                    if event.key == pygame.K_w and check_border(p.p_get_pos()[1] - 2):
                        variables.death = p.p_update_pos(p.p_get_pos()[0], p.p_get_pos()[1] - 2)
                    elif event.key == pygame.K_s and check_border(p.p_get_pos()[1] + 2):
                        variables.death = p.p_update_pos(p.p_get_pos()[0], p.p_get_pos()[1] + 2)
                    elif event.key == pygame.K_a and check_border(p.p_get_pos()[0] - 2):
                        variables.death = p.p_update_pos(p.p_get_pos()[0] - 2, p.p_get_pos()[1])
                    elif event.key == pygame.K_d and check_border(p.p_get_pos()[0] + 2):
                        variables.death = p.p_update_pos(p.p_get_pos()[0] + 2, p.p_get_pos()[1])

        # checking if player died
        if check_death(p.p_get_pos()[0], p.p_get_pos()[1]):
            pygame.time.wait(1000)
            variables.current_obstacle_number = 0
            last_obstacle_time = variables.start_game_time = variables.death_time = time.time()
            variables.obstacles_list = []
            variables.homing = False
            variables.last_homing_pos = [0, 0]
            variables.obstacles_homing_list = []
            reset_board()
            p.p_update_pos(5, 5)
            death_menu_func(win)

        # updaing obstacles
        for _ in variables.obstacles_list:
            _.update_obstacle()
        for _ in variables.obstacles_homing_list:
            _.update_obstacle()

        # drawing window
        draw.draw(win)
