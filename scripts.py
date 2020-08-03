import random
import numbers_list
import variables
from board import board


def update_pos(row, col, obstacle_type):
    board[row][col].append(obstacle_type)


def reset_pos(row, col, obstacle_type):
    i = 0
    for _ in board[row][col]:
        if board[row][col][i] == obstacle_type:
            board[row][col].pop(i)
            return
        else:
            i += 1


def reset_type(obstacle_type):
    i = j = 0
    while i < 11:
        while j < 11:
            if contain(board[i][j], obstacle_type):
                reset_pos(i, j, obstacle_type)
            j += 1
        j = 0
        i += 1


def reset_board():
    i = j = 0
    while i < 11:
        while j < 11:
            board[i][j] = [0]
            j += 1
        j = 0
        i += 1


def contain(array, obstacle_type):
    for _ in array:
        if _ == obstacle_type:
            return True
    return False


def search_by_type(obstacle_type):
    i = j = 0
    arr = []
    while i < 11:
        while j < 11:
            if board[j][j] == int(obstacle_type):
                arr.append([i, j])
            j += 1
        j = 0
        i += 1
    return arr


def search_by_pos(row, col):
    return board[row][col]


def check_border(number):
    return 0 <= number <= 10


def check_death(row, col):
    return contain(board[row][col], 4)


def reformated_number(number):
    number = str(number)
    if int(number) < 10:
        return '0' + '0' + number
    elif 10 <= int(number) < 100:
        return '0' + number
    else:
        return number


def random_array():
    array1 = []
    array2 = []
    i = 0
    while i < 60:
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        if not contain(array1, [x, y]) and not x == y == 5:
            array1.append([x, y])
            print(i)
            i += 1
    i = 0
    while i < 60:
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        if not contain(array1, [x, y]) and not contain(array2, [x, y]) and not x == y == 5:
            array2.append([x, y])
            print(i)
            i += 1
    return array1, array2


def print_board():
    print('BOARD')
    i = 0
    while i < len(board):
        print(board[i])
        i += 1


def give_randon(start, end):
    if variables.current_obstacle_number > 999:
        variables.current_obstacle_number = 0
    variables.current_obstacle_number += 1
    if start == 0:
        if end == 1:
            return numbers_list.list_01[variables.current_obstacle_number]
        elif end == 2:
            return numbers_list.list_02[variables.current_obstacle_number]
        elif end == 3:
            return numbers_list.list_03[variables.current_obstacle_number]
        elif end == 4:
            return numbers_list.list_04[variables.current_obstacle_number]
        elif end == 5:
            return numbers_list.list_05[variables.current_obstacle_number]
        elif end == 6:
            return numbers_list.list_06[variables.current_obstacle_number]
        elif end == 7:
            return numbers_list.list_07[variables.current_obstacle_number]
        elif end == 8:
            return numbers_list.list_08[variables.current_obstacle_number]
        elif end == 9:
            return numbers_list.list_09[variables.current_obstacle_number]
        elif end == 10:
            return numbers_list.list_010[variables.current_obstacle_number]
        elif end == 11:
            return numbers_list.list_011[variables.current_obstacle_number]
    elif start == 1:
        if end == 9:
            return numbers_list.list_19[variables.current_obstacle_number]
    elif start == 2:
        if end == 8:
            return numbers_list.list_28[variables.current_obstacle_number]
