import random
import time
from levels import level01
from board import board
from scripts import reset_pos, contain, reset_type


class ObstacleLines:
    def __init__(self, start_time, delay, width):
        self.start_time = start_time
        self.delay = delay
        self.width = width
        self.number = random.randint(0, 11 - self.width)
        self.direction = random.randint(0, 1)
        self.type = 3

    def get_number(self):
        return self.number

    def get_direction(self):
        return self.direction

    def update_obstacle(self):
        # reseting obstacle
        # vertical
        if self.get_direction() % 2 == 0:
            i = 0
            j = 0
            while j < self.width:
                while i < 11:
                    reset_pos(self.get_number() + j, i, self.type)
                    i += 1
                i = 0
                j += 1
        # horizontal
        else:
            i = 0
            j = 0
            while j < self.width:
                while i < 11:
                    reset_pos(i, self.get_number() + j, self.type)
                    i += 1
                i = 0
                j += 1
        if 0 <= (time.time() - self.start_time) < self.delay / 2:
            self.type = 3
            self.set_obstacle()
        elif self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75:
            self.type = 4
            self.set_obstacle()
        else:
            level01.obstacles.pop(0)

    def set_obstacle(self):
        # vertical
        if self.get_direction() % 2 == 0:
            i = 0
            j = 0
            while j < self.width:
                while i < 11:
                    board[self.get_number() + j][i].append(self.type)
                    i += 1
                i = 0
                j += 1
        # horizontal
        else:
            i = 0
            j = 0
            while j < self.width:
                while i < 11:
                    board[i][self.get_number() + j].append(self.type)
                    i += 1
                i = 0
                j += 1


class ObstacleSquare:
    def __init__(self, start_time, delay):
        self.start_time = start_time
        self.delay = delay
        self.row = random.randint(1, 9)
        self.col = random.randint(1, 9)
        print('row> ', self.row)
        print('col> ', self.col)
        self.type = 3

    def get_pos(self):
        return self.row, self.col

    def update_obstacle(self):
        if self.type == 3:
            reset_pos(self.get_pos()[0], self.get_pos()[1], self.type)
        elif self.type == 4:
            i = -1
            j = -1
            while i < 2:
                while j < 2:
                    reset_pos(self.get_pos()[0] + i, self.get_pos()[1] + j, self.type)
                    j += 1
                j = -1
                i += 1
        if 0 <= (time.time() - self.start_time) < self.delay / 2:
            self.type = 3
            self.set_obstacle()
        elif self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75:
            self.type = 4
            self.set_obstacle()
        else:
            level01.obstacles.pop(0)

    def set_obstacle(self):
        if self.type == 3:
            board[self.get_pos()[0]][self.get_pos()[1]].append(self.type)
        elif self.type == 4:
            i = -1
            j = -1
            while i < 2:
                while j < 2:
                    board[self.get_pos()[0] + i][self.get_pos()[1] + j].append(self.type)
                    j += 1
                j = -1
                i += 1


class ObstacleCross:
    def __init__(self, start_time, delay):
        self.start_time = start_time
        self.delay = delay
        self.row = random.randint(1, 9)
        self.col = random.randint(1, 9)
        self.type = 3

    def get_pos(self):
        return self.row, self.col

    def update_obstacle(self):
        if self.type == 3:
            reset_pos(self.get_pos()[0], self.get_pos()[1], self.type)
        elif self.type == 4:
            reset_pos(self.get_pos()[0], self.get_pos()[1], self.type)
            reset_pos(self.get_pos()[0], self.get_pos()[1] - 1, self.type)
            reset_pos(self.get_pos()[0], self.get_pos()[1] + 1, self.type)
            reset_pos(self.get_pos()[0] - 1, self.get_pos()[1], self.type)
            reset_pos(self.get_pos()[0] + 1, self.get_pos()[1], self.type)
        if 0 <= (time.time() - self.start_time) < self.delay / 2:
            self.type = 3
            self.set_obstacle()
        elif self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75:
            self.type = 4
            self.set_obstacle()
        else:
            level01.obstacles.pop(0)

    def set_obstacle(self):
        if self.type == 3:
            board[self.get_pos()[0]][self.get_pos()[1]].append(self.type)
        elif self.type == 4:
            board[self.get_pos()[0]][self.get_pos()[1]].append(self.type)
            board[self.get_pos()[0]][self.get_pos()[1] - 1].append(self.type)
            board[self.get_pos()[0]][self.get_pos()[1] + 1].append(self.type)
            board[self.get_pos()[0] - 1][self.get_pos()[1]].append(self.type)
            board[self.get_pos()[0] + 1][self.get_pos()[1]].append(self.type)


class ObstacleBigCross:
    def __init__(self, start_time, delay):
        self.start_time = start_time
        self.delay = delay
        self.row = random.randint(1, 9)
        self.col = random.randint(1, 9)
        self.type = 3

    def get_pos(self):
        return self.row, self.col

    def update_obstacle(self):
        if self.type == 3:
            reset_pos(self.get_pos()[0], self.get_pos()[1], self.type)
        elif self.type == 4:
            i = 0
            while i < 11:
                reset_pos(self.get_pos()[0], i, self.type)
                i += 1
            i = 0
            while i < 11:
                reset_pos(i, self.get_pos()[1], self.type)
                i += 1
        if 0 <= (time.time() - self.start_time) < self.delay / 2:
            self.type = 3
            self.set_obstacle()
        elif self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75:
            self.type = 4
            self.set_obstacle()
        else:
            level01.obstacles.pop(0)

    def set_obstacle(self):
        if self.type == 3:
            board[self.get_pos()[0]][self.get_pos()[1]].append(self.type)
        elif self.type == 4:
            i = 0
            while i < 11:
                board[self.get_pos()[0]][i].append(self.type)
                i += 1
            i = 0
            while i < 11:
                board[i][self.get_pos()[1]].append(self.type)
                i += 1


class ObstacleDiagonal:
    def __init__(self, start_time, delay):
        self.start_time = start_time
        self.delay = delay
        self.row = random.randint(1, 9)
        self.col = random.randint(1, 9)
        self.type = 3

    def get_pos(self):
        return self.row, self.col

    def update_obstacle(self):
        if self.type == 3:
            reset_pos(self.get_pos()[0], self.get_pos()[1], self.type)
        elif self.type == 4:
            x, y = self.get_pos()
            while 10 >= x >= 0 and 10 >= y >= 0:
                reset_pos(x, y, self.type)
                x -= 1
                y -= 1
            x, y = self.get_pos()
            while 10 >= x >= 0 and 10 >= y >= 0:
                reset_pos(x, y, self.type)
                x += 1
                y -= 1
            x, y = self.get_pos()
            while 10 >= x >= 0 and 10 >= y >= 0:
                reset_pos(x, y, self.type)
                x -= 1
                y += 1
            x, y = self.get_pos()
            while 10 >= x >= 0 and 10 >= y >= 0:
                reset_pos(x, y, self.type)
                x += 1
                y += 1
        if 0 <= (time.time() - self.start_time) < self.delay / 2:
            self.type = 3
            self.set_obstacle()
        elif self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75:
            self.type = 4
            self.set_obstacle()
        else:
            level01.obstacles.pop(0)

    def set_obstacle(self):
        if self.type == 3:
            board[self.get_pos()[0]][self.get_pos()[1]].append(self.type)
        elif self.type == 4:
            x, y = self.get_pos()
            while 10 >= x >= 0 and 10 >= y >= 0:
                board[x][y].append(self.type)
                x -= 1
                y -= 1
            x, y = self.get_pos()
            while 10 >= x >= 0 and 10 >= y >= 0:
                board[x][y].append(self.type)
                x += 1
                y -= 1
            x, y = self.get_pos()
            while 10 >= x >= 0 and 10 >= y >= 0:
                board[x][y].append(self.type)
                x -= 1
                y += 1
            x, y = self.get_pos()
            while 10 >= x >= 0 and 10 >= y >= 0:
                board[x][y].append(self.type)
                x += 1
                y += 1


class ObstacleExclusively:
    def __init__(self, start_time, delay):
        self.start_time = start_time
        self.delay = delay
        self.row = random.randint(2, 8)
        self.col = random.randint(2, 8)
        self.type = 3

    def get_pos(self):
        return self.row, self.col

    def update_obstacle(self):
        if self.type == 3:
            i = j = -2
            while i < 3:
                while j < 3:
                    reset_pos(self.get_pos()[0] + i, self.get_pos()[1] + j, self.type)
                    j += 1
                j = -2
                i += 1
        elif self.type == 4:
            i = j = -2
            while i < 3:
                while j < 3:
                    board[self.get_pos()[0] + i][self.get_pos()[1] + j].append(2)
                    j += 1
                j = -2
                i += 1
            i = j = 0
            while i < 11:
                while j < 11:
                    if not contain(board[i][j], 2):
                        reset_pos(i, j, self.type)
                    j += 1
                j = 0
                i += 1
            reset_type(2)
        if 0 <= (time.time() - self.start_time) < self.delay / 2:
            self.type = 3
            self.set_obstacle()
        elif self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75:
            self.type = 4
            self.set_obstacle()
        else:
            level01.obstacles.pop(0)

    def set_obstacle(self):
        if self.type == 3:
            i = j = -2
            while i < 3:
                while j < 3:
                    board[self.get_pos()[0] + i][self.get_pos()[1] + j].append(self.type)
                    j += 1
                j = -2
                i += 1
        elif self.type == 4:
            i = j = -2
            while i < 3:
                while j < 3:
                    board[self.get_pos()[0] + i][self.get_pos()[1] + j].append(2)
                    j += 1
                j = -2
                i += 1
            i = j = 0
            while i < 11:
                while j < 11:
                    if not contain(board[i][j], 2):
                        board[i][j].append(self.type)
                    j += 1
                j = 0
                i += 1
            reset_type(2)


class ObstacleBoard1:
    def __init__(self, start_time, delay):
        self.start_time = start_time
        self.delay = delay
        self.type = 3

    def update_obstacle(self):
        if self.type == 3:
            i = j = 0
            while i < 11:
                while j < 11:
                    if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                        reset_pos(i, j, self.type)
                    j += 1
                j = 0
                i += 1
        elif self.type == 4:
            i = j = 0
            while i < 11:
                while j < 11:
                    if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                        reset_pos(i, j, self.type)
                    j += 1
                j = 0
                i += 1
        if 0 <= (time.time() - self.start_time) < self.delay / 2:
            self.type = 3
            self.set_obstacle()
        elif self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75:
            self.type = 4
            self.set_obstacle()
        else:
            level01.obstacles.pop(0)

    def set_obstacle(self):
        if self.type == 3:
            i = j = 0
            while i < 11:
                while j < 11:
                    if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                        board[i][j].append(self.type)
                    j += 1
                j = 0
                i += 1
        elif self.type == 4:
            i = j = 0
            while i < 11:
                while j < 11:
                    if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                        board[i][j].append(self.type)
                    j += 1
                j = 0
                i += 1


class ObstacleBoard2:
    def __init__(self, start_time, delay):
        self.start_time = start_time
        self.delay = delay
        self.type = 3

    def update_obstacle(self):
        if self.type == 3:
            i = j = 0
            while i < 11:
                while j < 11:
                    if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
                        reset_pos(i, j, self.type)
                    j += 1
                j = 0
                i += 1
        elif self.type == 4:
            i = j = 0
            while i < 11:
                while j < 11:
                    if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
                        reset_pos(i, j, self.type)
                    j += 1
                j = 0
                i += 1
        if 0 <= (time.time() - self.start_time) < self.delay / 2:
            self.type = 3
            self.set_obstacle()
        elif self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75:
            self.type = 4
            self.set_obstacle()
        else:
            level01.obstacles.pop(0)

    def set_obstacle(self):
        if self.type == 3:
            i = j = 0
            while i < 11:
                while j < 11:
                    if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
                        board[i][j].append(self.type)
                    j += 1
                j = 0
                i += 1
        elif self.type == 4:
            i = j = 0
            while i < 11:
                while j < 11:
                    if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
                        board[i][j].append(self.type)
                    j += 1
                j = 0
                i += 1


class ObstacleRandomSafe:
    def __init__(self, start_time, delay, array1, array2):
        self.start_time = start_time
        self.delay = delay
        self.type = 3
        self.array1 = array1
        self.array2 = array2

    def update_obstacle(self):
        if self.type == 3:
            reset_pos(5, 5, self.type)
            i = 0
            while i < len(self.array1):
                reset_pos(self.array1[i][0], self.array1[i][1], self.type)
                i += 1
        elif self.type == 4:
            reset_pos(5, 5, self.type)
            i = 0
            while i < len(self.array1):
                reset_pos(self.array1[i][0], self.array1[i][1], self.type)
                i += 1
        if 0 <= (time.time() - self.start_time) < self.delay / 2:
            self.type = 3
            self.set_obstacle()
        elif self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75:
            self.type = 4
            self.set_obstacle()
        else:
            level01.obstacles.pop(0)
            new_obstacle = ObstacleRandomDanger(time.time(), level01.delay, self.array2)
            new_obstacle.set_obstacle()
            level01.obstacles.append(new_obstacle)

    def set_obstacle(self):
        if self.type == 3:
            board[5][5].append(self.type)
            i = 0
            while i < len(self.array1):
                board[self.array1[i][0]][self.array1[i][1]].append(self.type)
                i += 1
        elif self.type == 4:
            board[5][5].append(self.type)
            i = 0
            while i < len(self.array1):
                board[self.array1[i][0]][self.array1[i][1]].append(self.type)
                i += 1


class ObstacleRandomDanger:
    def __init__(self, start_time, delay, array):
        self.start_time = start_time
        self.delay = delay
        self.type = 3
        self.array = array

    def update_obstacle(self):
        if self.type == 4:
            reset_pos(5, 5, self.type)
            i = 0
            while i < len(self.array):
                reset_pos(self.array[i][0], self.array[i][1], self.type)
                i += 1
        if 0 <= (time.time() - self.start_time) < self.delay / 2:
            self.type = 3
        elif self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75:
            self.type = 4
            self.set_obstacle()
        else:
            level01.obstacles.pop(0)

    def set_obstacle(self):
        if self.type == 4:
            board[5][5].append(self.type)
            i = 0
            while i < len(self.array):
                board[self.array[i][0]][self.array[i][1]].append(self.type)
                i += 1


class ObstacleHoming:
    def __init__(self, start_time, delay, pos):
        self.start_time = start_time
        self.delay = delay
        self.type = 4
        self.p_row = pos[0]
        self.p_col = pos[1]
        self.o_row = level01.last_homing_pos[0]
        self.o_col = level01.last_homing_pos[1]
        self.last_pos = [0, 0]

    def get_p_pos(self):
        return self.p_row, self.p_col

    def increase_p_pos(self, pos):
        self.p_row += pos[0]
        self.p_col += pos[1]

    def get_o_pos(self):
        return self.o_row, self.o_col

    def increase_o_pos(self, pos):
        self.o_row += pos[0]
        self.o_col += pos[1]

    def update_obstacle(self):
        if 0.5 <= (time.time() - self.start_time) <= 1:
            reset_pos(level01.last_homing_pos[0], level01.last_homing_pos[1], 3)
            reset_pos(self.last_pos[0], self.last_pos[1], 4)
            level01.obstacles.pop(0)
            level01.homing = False

    def set_obstacle(self):
        board[self.get_o_pos()[0]][self.get_o_pos()[1]].append(4)
        self.last_pos = [self.get_o_pos()[0], self.get_o_pos()[1]]
        if abs(self.get_o_pos()[0] - self.get_p_pos()[0]) > abs(self.get_o_pos()[1] - self.get_p_pos()[1]):
            if self.get_o_pos()[0] > self.get_p_pos()[0]:
                self.increase_o_pos([-1, 0])
            else:
                self.increase_o_pos([1, 0])
        else:
            if self.get_o_pos()[1] > self.get_p_pos()[1]:
                self.increase_o_pos([0, -1])
            else:
                self.increase_o_pos([0, 1])
        board[self.get_o_pos()[0]][self.get_o_pos()[1]].append(3)
        level01.last_homing_pos[0] = self.get_o_pos()[0]
        level01.last_homing_pos[1] = self.get_o_pos()[1]
