import pygame
import variables
import main
import json
import menus.main_menu
import levels.level01

with open("levels.json", "r+") as read_file:
    data = json.load(read_file)
    levels_easy = (data['levels_easy'])
    levels_med = (data['levels_med'])
    levels_hard = (data['levels_hard'])

levels_list = [
    [True, False, False, False],
    [False, False, False],
    [False, False, False, False]
]
levels_num = 0

stage_list = [True, False, False, False]
stage = 0


def set_levels():
    global levels_list, levels_num
    levels_list = clear_array(levels_list)
    if not levels_num == -1:
        x = y = 0
        if 3 >= levels_num >= 0:
            x = 0
            y = levels_num
        elif 6 >= levels_num >= 4:
            x = 1
            y = levels_num - 4
        elif 11 >= levels_num >= 7:
            x = 2
            y = levels_num - 7

        levels_list[x][y] = True


def set_stage():
    global stage_list, stage
    stage_list = clear_line(stage_list)
    stage_list[stage] = True


def find_true_in_line(array):
    for _ in array:
        if _:
            return True
    return False


def find_true_in_array(array):
    for line in array:
        for element in line:
            if element:
                return True
    return False


def clear_line(line):
    i = 0
    for element in line:
        line[i] = False
        i += 1
    return line


def clear_array(array):
    i = j = 0
    for line in array:
        for element in line:
            array[i][j] = False
            j += 1
        j = 0
        i += 1
    return array


def draw_stage(win):
    global stage
    pygame.draw.rect(win, variables.RED, (main.WIDTH * 0.25 * stage, 0, main.WIDTH * 0.25, main.HEIGHT * 0.25))


def draw_levels(win):
    global levels_num
    if not levels_num == -1:
        x = y = 0
        if 3 >= levels_num >= 0:
            x = 0
            y = levels_num
            pygame.draw.rect(win, variables.RED, (main.WIDTH * 0.25 * (y), main.HEIGHT * 0.25 * (x + 1), main.WIDTH * 0.25, main.HEIGHT * 0.25))
        elif 6 >= levels_num >= 4:
            x = 1
            y = levels_num - 4
            pygame.draw.rect(win, variables.RED, (main.WIDTH * 0.33 * (y), main.HEIGHT * 0.25 * (x + 1), main.WIDTH * 0.33, main.HEIGHT * 0.25))
        elif 11 >= levels_num >= 7:
            x = 2
            y = levels_num - 7
            pygame.draw.rect(win, variables.RED, (main.WIDTH * 0.25 * (y), main.HEIGHT * 0.25 * (x + 1), main.WIDTH * 0.25, main.HEIGHT * 0.25))


def draw_done(win):
    global levels_easy, levels_med, levels_hard
    global stage
    i = 0
    if stage == 0:
        for _ in levels_easy:
            if _:
                if 3 >= i >= 0:
                    x = 0
                    y = i
                    pygame.draw.rect(win, variables.GREEN, (main.WIDTH * 0.25 * (y), main.HEIGHT * 0.25 * (x + 1), main.WIDTH * 0.25, main.HEIGHT * 0.25))
                elif 6 >= i >= 4:
                    x = 1
                    y = i - 4
                    pygame.draw.rect(win, variables.GREEN, (main.WIDTH * 0.33 * (y), main.HEIGHT * 0.25 * (x + 1), main.WIDTH * 0.33, main.HEIGHT * 0.25))
                elif 11 >= i >= 7:
                    x = 2
                    y = i - 7
                    pygame.draw.rect(win, variables.GREEN, (main.WIDTH * 0.25 * (y), main.HEIGHT * 0.25 * (x + 1), main.WIDTH * 0.25, main.HEIGHT * 0.25))
            i += 1
    elif stage == 1:
        for _ in levels_med:
            if _:
                if 3 >= i >= 0:
                    x = 0
                    y = i
                    pygame.draw.rect(win, variables.GREEN, (main.WIDTH * 0.25 * (y), main.HEIGHT * 0.25 * (x + 1), main.WIDTH * 0.25, main.HEIGHT * 0.25))
                elif 6 >= i >= 4:
                    x = 1
                    y = i - 4
                    pygame.draw.rect(win, variables.GREEN, (main.WIDTH * 0.33 * (y), main.HEIGHT * 0.25 * (x + 1), main.WIDTH * 0.33, main.HEIGHT * 0.25))
                elif 11 >= i >= 7:
                    x = 2
                    y = i - 7
                    pygame.draw.rect(win, variables.GREEN, (main.WIDTH * 0.25 * (y), main.HEIGHT * 0.25 * (x + 1), main.WIDTH * 0.25, main.HEIGHT * 0.25))
            i += 1
    elif stage == 2:
        for _ in levels_hard:
            if _:
                if 3 >= i >= 0:
                    x = 0
                    y = i
                    pygame.draw.rect(win, variables.GREEN, (main.WIDTH * 0.25 * (y), main.HEIGHT * 0.25 * (x + 1), main.WIDTH * 0.25, main.HEIGHT * 0.25))
                elif 6 >= i >= 4:
                    x = 1
                    y = i - 4
                    pygame.draw.rect(win, variables.GREEN, (main.WIDTH * 0.33 * (y), main.HEIGHT * 0.25 * (x + 1), main.WIDTH * 0.33, main.HEIGHT * 0.25))
                elif 11 >= i >= 7:
                    x = 2
                    y = i - 7
                    pygame.draw.rect(win, variables.GREEN, (main.WIDTH * 0.25 * (y), main.HEIGHT * 0.25 * (x + 1), main.WIDTH * 0.25, main.HEIGHT * 0.25))
            i += 1


def draw_menu(win):
    win.fill(variables.BLACK)
    draw_stage(win)
    draw_done(win)
    draw_levels(win)
    win.blit(variables.levels_menu_img, (0, 0))
    pygame.display.update()


def levels_menu_func(win):
    global levels_list, stage_list, levels_num, stage, levels_easy, levels_med, levels_hard
    levels_list = [
        [True, False, False, False],
        [False, False, False],
        [False, False, False, False]
    ]
    levels_num = 0

    stage_list = [True, False, False, False]
    stage = 0
    if levels_hard[10]:
        max_stage = 3
    elif levels_med[10]:
        max_stage = 2
    elif levels_easy[10]:
        max_stage = 1
    else:
        max_stage = 0
    draw_menu(win)
    run = True
    while run:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if levels_num == -1:
                    if event.key == pygame.K_RIGHT and stage < max_stage:
                        stage += 1
                    elif event.key == pygame.K_LEFT and stage > 0:
                        stage -= 1
                    elif event.key == pygame.K_DOWN:
                        levels_num = 0
                        set_levels()
                    set_stage()
                elif not levels_num == -1:
                    if event.key == pygame.K_UP and find_true_in_line(levels_list[0]):
                        levels_num = -1
                    elif event.key == pygame.K_RIGHT and levels_num < 10:
                        levels_num += 1
                    elif event.key == pygame.K_LEFT and levels_num > 0:
                        levels_num -= 1
                    set_levels()
                if event.key == pygame.K_ESCAPE:
                    menus.main_menu.main_menu_func(win)
                if event.key == pygame.K_RETURN:
                    levels.level01.main(win)

            draw_menu(win)
