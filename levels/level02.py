import pygame
import draw
import time
import variables
import random
from player import Player
from menus.death_menu import death_menu_func
from menus.win_menu import win_menu_func
from scripts import check_border, reset_board, check_death, print_board
from obstacles import ObstacleSquare, ObstacleCross, ObstacleBigCross

pygame.init()

reset_board()
p = Player(5, 5)
p.p_update_pos(5, 5)


def main(win):
    print_board()
    reset_board()
    p.p_update_pos(5, 5)
    last_obstacle_time = variables.start_game_time = time.time()
    # max_width = 1
    time_between_obstacles = 0.8
    run = True
    while run:
        curr_time = time.time()
        pygame.time.Clock().tick(60)
        if time.time() - variables.start_game_time > 120:
            variables.start_game_time = time.time()
            win_menu_func(win)
        # max_width = min(((round(time.time() - start_game_time)) // 15) + 3, 6)
        # time_between_obstacles = max(float(1.5 - (0.1 * ((round(time.time() - start_game_time)) // 15))), 0.5)
        # if not variables.homing:
        #     new_obstacle = ObstacleHoming(curr_time, variables.delay, p.p_get_pos())
        #     new_obstacle.set_obstacle()
        #     variables.obstacles_homing_list.append(new_obstacle)
        #     variables.homing = True
        # if curr_time - last_obstacle_time > time_between_obstacles and not variables.death:
        #     last_obstacle_time = time.time()
        #     new_obstacle = ObstacleSquare(curr_time, variables.delay)
        #     new_obstacle.set_obstacle()
        #     variables.obstacles_list.append(new_obstacle)
        #     new_obstacle = ObstacleSquare(curr_time, variables.delay)
        #     new_obstacle.set_obstacle()
        #     variables.obstacles_list.append(new_obstacle)
        #     new_obstacle = ObstacleCross(curr_time, variables.delay)
        #     new_obstacle.set_obstacle()
        #     variables.obstacles_list.append(new_obstacle)
        if curr_time - last_obstacle_time > time_between_obstacles and not variables.death:
            last_obstacle_time = time.time()
            if random.randint(0, 1) % 2 == 0:
                new_obstacle = ObstacleCross(curr_time, variables.delay)
                new_obstacle.set_obstacle()
                variables.obstacles_list.append(new_obstacle)
                new_obstacle = ObstacleSquare(curr_time, variables.delay)
                new_obstacle.set_obstacle()
                variables.obstacles_list.append(new_obstacle)
            else:
                new_obstacle = ObstacleBigCross(curr_time, variables.delay)
                new_obstacle.set_obstacle()
                variables.obstacles_list.append(new_obstacle)
                new_obstacle = ObstacleSquare(curr_time, variables.delay)
                new_obstacle.set_obstacle()
                variables.obstacles_list.append(new_obstacle)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            # keyboard handling
            if event.type == pygame.KEYDOWN:
                # normal moving
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
            last_obstacle_time = variables.start_game_time = variables.death_time = time.time()
            variables.obstacles_list = []
            reset_board()
            p.p_update_pos(5, 5)
            death_menu_func(win)

        # updaing obstacles
        for _ in variables.obstacles_list:
            _.update_obstacle()

        # drawing window
        draw.draw(win)
