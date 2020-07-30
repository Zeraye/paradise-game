from board import board
import random


def update_pos(row, col, obstacle_type):
    board[row][col].append(obstacle_type)


def reset_pos(row, col, obstacle_type):
    if contain(board[row][col], obstacle_type):
        board[row][col].remove(obstacle_type)


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
    i = 0
    j = 0
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
    i = 0
    j = 0
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


def random_array():
    array1 = []
    array2 = []
    i = 0
    while i < 61:
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        if not contain(array1, [x, y]) and not x == y == 5:
            array1.append([x, y])
            i += 1
    i = 0
    while i < 61:
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        if not contain(array1, [x, y]) and not x == y == 5:
            array2.append([x, y])
            i += 1
    return array1, array2


def print_board():
    print('BOARD')
    i = 0
    while i < len(board):
        print(board[i])
        i += 1
