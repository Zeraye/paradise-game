import pygame
import draw
import time
import random
from player import Player
from menu.death_menu import death_menu
from scripts import check_border, reset_board, check_death
from obstacles import ObstacleLines, ObstacleSquare, ObstacleCross, ObstacleBigCross, ObstacleDiagonal,\
                      ObstacleExclusively, ObstacleBoard1, ObstacleBoard2, ObstacleRandomSafe, ObstacleRandomDanger,\
                      ObstacleHoming

pygame.init()

reset_board()
p = Player(5, 5)
p.p_update_pos(5, 5)
death = homing = False
curr_time = last_obstacle_time = start_game_time = death_time = time.time()
delay = 1.5
max_width = 1
time_between_obstacles = 1.5
obstacles = []
last_homing_pos = [0, 0]


def main(win):
    global death, curr_time, delay, obstacles, last_obstacle_time, death_time, start_game_time, max_width,\
           time_between_obstacles, homing
    run = True
    while run:
        curr_time = time.time()
        pygame.time.Clock().tick(60)
        # max_width = min(((round(time.time() - start_game_time)) // 15) + 3, 6)
        # time_between_obstacles = max(float(1.5 - (0.1 * ((round(time.time() - start_game_time)) // 15))), 0.5)
        # if not homing:
        #     new_obstacle = ObstacleHoming(curr_time, delay, p.p_get_pos())
        #     new_obstacle.set_obstacle()
        #     obstacles.append(new_obstacle)
        #     homing = True
        # if curr_time - last_obstacle_time > time_between_obstacles and not death:
        #     last_obstacle_time = time.time()
        #     new_obstacle = ObstacleBigCross(curr_time, delay)
        #     new_obstacle.set_obstacle()
        #     obstacles.append(new_obstacle)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            # keyboard handling
            if event.type == pygame.KEYDOWN:
                # normal moving
                if not death and not pygame.key.get_pressed()[pygame.K_SPACE]:
                    if event.key == pygame.K_w and check_border(p.p_get_pos()[1] - 1):
                        death = p.p_update_pos(p.p_get_pos()[0], p.p_get_pos()[1] - 1)
                    elif event.key == pygame.K_s and check_border(p.p_get_pos()[1] + 1):
                        death = p.p_update_pos(p.p_get_pos()[0], p.p_get_pos()[1] + 1)
                    elif event.key == pygame.K_a and check_border(p.p_get_pos()[0] - 1):
                        death = p.p_update_pos(p.p_get_pos()[0] - 1, p.p_get_pos()[1])
                    elif event.key == pygame.K_d and check_border(p.p_get_pos()[0] + 1):
                        death = p.p_update_pos(p.p_get_pos()[0] + 1, p.p_get_pos()[1])
                # moving with space (longer distance)
                if not death and pygame.key.get_pressed()[pygame.K_SPACE]:
                    if event.key == pygame.K_w and check_border(p.p_get_pos()[1] - 3):
                        death = p.p_update_pos(p.p_get_pos()[0], p.p_get_pos()[1] - 3)
                    elif event.key == pygame.K_s and check_border(p.p_get_pos()[1] + 3):
                        death = p.p_update_pos(p.p_get_pos()[0], p.p_get_pos()[1] + 3)
                    elif event.key == pygame.K_a and check_border(p.p_get_pos()[0] - 3):
                        death = p.p_update_pos(p.p_get_pos()[0] - 3, p.p_get_pos()[1])
                    elif event.key == pygame.K_d and check_border(p.p_get_pos()[0] + 3):
                        death = p.p_update_pos(p.p_get_pos()[0] + 3, p.p_get_pos()[1])

        # checking if player died
        if check_death(p.p_get_pos()[0], p.p_get_pos()[1]):
            pygame.time.wait(1000)
            curr_time = last_obstacle_time = start_game_time = death_time = time.time()
            obstacles = []
            reset_board()
            p.p_update_pos(5, 5)
            death_menu(win)

        # updaing obstacles
        for _ in obstacles:
            _.update_obstacle()

        # drawing window
        draw.draw(win)
