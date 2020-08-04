import random
import time
import variables
from board import board
from scripts import reset_pos, contain, reset_type


class ObstacleLines:
    def __init__(self, start_time, delay, width, number, direction):
        self.start_time = start_time
        self.delay = delay
        self.width = width
        # random from 0-(11-self.width)
        self.number = number
        # random from 0-1
        self.direction = direction
        self.type = 3
        self.setted1 = self.setted2 = False

    def get_start_time(self):
        return self.start_time

    def update_obstacle(self):
        # reseting obstacle
        if self.type == 4:
            # vertical
            if self.direction % 2 == 0:
                i = j = 0
                while j < self.width:
                    while i < 11:
                        reset_pos(self.number + j, i, 3)
                        i += 1
                    i = 0
                    j += 1
            # horizontal
            else:
                i = j = 0
                while j < self.width:
                    while i < 11:
                        reset_pos(i, self.number + j, 3)
                        i += 1
                    i = 0
                    j += 1

        if 0 <= (time.time() - self.start_time) < self.delay / 2 and not self.setted1:
            self.set_obstacle()
        elif self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75:
            if not self.setted2:
                self.type = 4
                self.set_obstacle()
        elif (time.time() - self.start_time) > self.delay * 0.75 and self.setted2:
            # vertical
            if self.direction % 2 == 0:
                i = j = 0
                while j < self.width:
                    while i < 11:
                        reset_pos(self.number + j, i, self.type)
                        i += 1
                    i = 0
                    j += 1
            # horizontal
            else:
                i = j = 0
                while j < self.width:
                    while i < 11:
                        reset_pos(i, self.number + j, self.type)
                        i += 1
                    i = 0
                    j += 1
            for _ in variables.obstacles_list:
                if _.get_start_time() == self.start_time:
                    variables.obstacles_list.remove(_)

    def set_obstacle(self):
        if self.type == 3:
            self.setted1 = True
        elif self.type == 4:
            self.setted2 = True

        # vertical
        if self.direction % 2 == 0:
            i = j = 0
            while j < self.width:
                while i < 11:
                    board[self.number + j][i].append(self.type)
                    i += 1
                i = 0
                j += 1
        # horizontal
        else:
            i = j = 0
            while j < self.width:
                while i < 11:
                    board[i][self.number + j].append(self.type)
                    i += 1
                i = 0
                j += 1


class ObstacleSquare:
    def __init__(self, start_time, delay, row, col):
        self.start_time = start_time
        self.delay = delay
        # random from 1-9
        self.row = row
        # random from 1-9
        self.col = col
        self.type = 5
        self.setted1 = self.setted2 = False

    def get_start_time(self):
        return self.start_time

    def update_obstacle(self):
        if self.type == 4:
            reset_pos(self.row, self.col, 5)
        if 0 <= (time.time() - self.start_time) < self.delay / 2 and not self.setted1:
            self.set_obstacle()
        elif self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75:
            if not self.setted2:
                self.type = 4
                self.set_obstacle()
        elif (time.time() - self.start_time) > self.delay * 0.75 and self.setted2:
            i = j = -1
            while i < 2:
                while j < 2:
                    reset_pos(self.row + i, self.col + j, 4)
                    j += 1
                j = -1
                i += 1
            for _ in variables.obstacles_list:
                if _.get_start_time() == self.start_time:
                    variables.obstacles_list.remove(_)

    def set_obstacle(self):
        if self.type == 5:
            board[self.row][self.col].append(self.type)
            self.setted1 = True
        elif self.type == 4:
            i = j = -1
            while i < 2:
                while j < 2:
                    board[self.row + i][self.col + j].append(self.type)
                    j += 1
                j = -1
                i += 1
            self.setted2 = True


class ObstacleCross:
    def __init__(self, start_time, delay, row, col):
        self.start_time = start_time
        self.delay = delay
        # random from 1-9
        self.row = row
        # random from 1-9
        self.col = col
        self.type = 6
        self.setted1 = False
        self.setted2 = False
    def get_start_time(self):
        return self.start_time

    def update_obstacle(self):
        if self.type == 4:
            reset_pos(self.row, self.col, 6)
        if 0 <= (time.time() - self.start_time) < self.delay / 2 and not self.setted1:
            self.type = 6
            self.set_obstacle()
        elif self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75:
            if not self.setted2:
                self.type = 4
                self.set_obstacle()
        elif (time.time() - self.start_time) > self.delay * 0.75 and self.setted2:
            reset_pos(self.row, self.col, self.type)
            reset_pos(self.row, self.col - 1, self.type)
            reset_pos(self.row, self.col + 1, self.type)
            reset_pos(self.row - 1, self.col, self.type)
            reset_pos(self.row + 1, self.col, self.type)
            for _ in variables.obstacles_list:
                if _.get_start_time() == self.start_time:
                    variables.obstacles_list.remove(_)

    def set_obstacle(self):
        if self.type == 6:
            board[self.row][self.col].append(self.type)
            self.setted1 = True
        elif self.type == 4:
            board[self.row][self.col].append(self.type)
            board[self.row][self.col - 1].append(self.type)
            board[self.row][self.col + 1].append(self.type)
            board[self.row - 1][self.col].append(self.type)
            board[self.row + 1][self.col].append(self.type)
            self.setted2 = True


class ObstacleBigCross:
    def __init__(self, start_time, delay, row, col):
        self.start_time = start_time
        self.delay = delay
        # random from 1-9
        self.row = row
        # random from 1-9
        self.col = col
        self.type = 7
        self.setted1 = self.setted2 = False

    def get_start_time(self):
        return self.start_time

    def update_obstacle(self):
        if self.type == 4:
            reset_pos(self.row, self.col, 7)
        if 0 <= (time.time() - self.start_time) < self.delay / 2 and not self.setted1:
            self.set_obstacle()
        elif self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75:
            if not self.setted2:
                self.type = 4
                self.set_obstacle()
        elif (time.time() - self.start_time) > self.delay * 0.75 and self.setted2:
            i = 0
            while i < 11:
                reset_pos(self.row, i, self.type)
                i += 1
            i = 0
            while i < 11:
                reset_pos(i, self.col, self.type)
                i += 1
            for _ in variables.obstacles_list:
                if _.get_start_time() == self.start_time:
                    variables.obstacles_list.remove(_)

    def set_obstacle(self):
        if self.type == 7:
            board[self.row][self.col].append(self.type)
            self.setted1 = True
        elif self.type == 4:
            i = 0
            while i < 11:
                board[self.row][i].append(self.type)
                i += 1
            i = 0
            while i < 11:
                board[i][self.col].append(self.type)
                i += 1
            self.setted2 = True


class ObstacleDiagonal:
    def __init__(self, start_time, delay, row, col):
        self.start_time = start_time
        self.delay = delay
        # random from 1-9
        self.row = row
        # random from 1-9
        self.col = col
        self.type = 8
        self.setted1 = self.setted2 = False

    def get_start_time(self):
        return self.start_time

    def update_obstacle(self):
        if self.type == 4:
            reset_pos(self.row, self.col, 8)
        if 0 <= (time.time() - self.start_time) < self.delay / 2 and not self.setted1:
            self.set_obstacle()
        elif self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75:
            if not self.setted2:
                self.type = 4
                self.set_obstacle()
        elif (time.time() - self.start_time) > self.delay * 0.75 and self.setted2:
            x = self.row
            y = self.col
            while 10 >= x >= 0 and 10 >= y >= 0:
                reset_pos(x, y, self.type)
                x -= 1
                y -= 1
            x = self.row
            y = self.col
            while 10 >= x >= 0 and 10 >= y >= 0:
                reset_pos(x, y, self.type)
                x += 1
                y -= 1
            x = self.row
            y = self.col
            while 10 >= x >= 0 and 10 >= y >= 0:
                reset_pos(x, y, self.type)
                x -= 1
                y += 1
            x = self.row
            y = self.col
            while 10 >= x >= 0 and 10 >= y >= 0:
                reset_pos(x, y, self.type)
                x += 1
                y += 1
            for _ in variables.obstacles_list:
                if _.get_start_time() == self.start_time:
                    variables.obstacles_list.remove(_)

    def set_obstacle(self):
        if self.type == 8:
            board[self.row][self.col].append(self.type)
            self.setted1 = True
        elif self.type == 4:
            x = self.row
            y = self.col
            while 10 >= x >= 0 and 10 >= y >= 0:
                board[x][y].append(self.type)
                x -= 1
                y -= 1
            x = self.row
            y = self.col
            while 10 >= x >= 0 and 10 >= y >= 0:
                board[x][y].append(self.type)
                x += 1
                y -= 1
            x = self.row
            y = self.col
            while 10 >= x >= 0 and 10 >= y >= 0:
                board[x][y].append(self.type)
                x -= 1
                y += 1
            x = self.row
            y = self.col
            while 10 >= x >= 0 and 10 >= y >= 0:
                board[x][y].append(self.type)
                x += 1
                y += 1
            self.setted2 = True

# TODO: repair
class ObstacleExclusively:
    def __init__(self, start_time, delay, row, col):
        self.start_time = start_time
        self.delay = delay
        # random from 2-8
        self.row = row
        # random from 2-8
        self.col = col
        self.type = 3
        self.setted1 = self.setted2 = False

    def get_start_time(self):
        return self.start_time

    def update_obstacle(self):
        if self.type == 4:
            i = j = -2
            while i < 3:
                while j < 3:
                    reset_pos(self.row + i, self.col + j, 3)
                    j += 1
                j = -2
                i += 1
        if 0 <= (time.time() - self.start_time) < self.delay / 2 and not self.setted1:
            self.set_obstacle()
        elif self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75:
            if not self.setted2:
                self.type = 4
                self.set_obstacle()
        elif (time.time() - self.start_time) > self.delay * 0.75 and self.setted2:
            # TODO: setting deadly obstacles
            y = self.col - 2
            temp_array = []
            if y >= 0:
                i = j = 0
                while i < y:
                    while j < 11:
                        reset_pos(j, i, self.type)
                        temp_array.append(i)
                        j += 1
                    j = 0
                    i += 1
            y = i + 5
            while y < 11:
                i = j = 0
                while i < 11:
                    reset_pos(i, y, self.type)
                    temp_array.append(y)
                    i += 1
                i = 0
                y += 1
            x = self.row - 2
            if x >= 0:
                i = j = 0
                while i < x:
                    while j < 11:
                        if not contain(temp_array, j):
                            reset_pos(i, j, self.type)
                        j += 1
                    j = 0
                    i += 1
            x = i + 5
            while x < 11:
                i = j = 0
                while i < 11:
                    if not contain(temp_array, i):
                        reset_pos(x, i, self.type)
                    i += 1
                i = 0
                x += 1
            for _ in variables.obstacles_list:
                if _.get_start_time() == self.start_time:
                    variables.obstacles_list.remove(_)

    def set_obstacle(self):
        if self.type == 3:
            i = j = -2
            while i < 3:
                while j < 3:
                    board[self.row + i][self.col + j].append(self.type)
                    j += 1
                j = -2
                i += 1
            self.setted1 = True
        elif self.type == 4:
            # TODO: setting deadly obstacles
            y = self.col - 2
            temp_array = []
            if y > 0:
                i = j = 0
                while i < y:
                    while j < 11:
                        board[j][i].append(self.type)
                        temp_array.append(i)
                        j += 1
                    j = 0
                    i += 1
            y = i + 5
            while y < 11:
                i = j = 0
                while i < 11:
                    board[i][y].append(self.type)
                    temp_array.append(y)
                    i += 1
                i = 0
                y += 1
            x = self.row - 2
            if x > 0:
                i = j = 0
                while i < x:
                    while j < 11:
                        if not contain(temp_array, j):
                            board[i][j].append(self.type)
                        j += 1
                    j = 0
                    i += 1
            x = i + 5
            while x < 11:
                i = j = 0
                while i < 11:
                    if not contain(temp_array, i):
                        board[x][i].append(self.type)
                    i += 1
                i = 0
                x += 1
            self.setted2 = True


class ObstacleBoard1:
    def __init__(self, start_time, delay):
        self.start_time = start_time
        self.delay = delay
        self.type = 3
        self.setted1 = self.setted2 = False

    def get_start_time(self):
        return self.start_time

    def update_obstacle(self):
        if self.type == 4:
            i = j = 0
            while i < 11:
                while j < 11:
                    if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                        reset_pos(i, j, 3)
                    j += 1
                j = 0
                i += 1
        if 0 <= (time.time() - self.start_time) < self.delay / 2 and not self.setted1:
            self.set_obstacle()
        elif self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75:
            if not self.setted2:
                self.type = 4
                self.set_obstacle()
        elif (time.time() - self.start_time) > self.delay * 0.75 and self.setted2:
            i = j = 0
            while i < 11:
                while j < 11:
                    if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                        reset_pos(i, j, self.type)
                    j += 1
                j = 0
                i += 1
            for _ in variables.obstacles_list:
                if _.get_start_time() == self.start_time:
                    variables.obstacles_list.remove(_)

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
            self.setted1 = True
        elif self.type == 4:
            i = j = 0
            while i < 11:
                while j < 11:
                    if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                        board[i][j].append(self.type)
                    j += 1
                j = 0
                i += 1
            self.setted2 = True


class ObstacleBoard2:
    def __init__(self, start_time, delay):
        self.start_time = start_time
        self.delay = delay
        self.type = 3
        self.setted1 = self.setted2 = False

    def get_start_time(self):
        return self.start_time

    def update_obstacle(self):
        if self.type == 4:
            i = j = 0
            while i < 11:
                while j < 11:
                    if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
                        reset_pos(i, j, 3)
                    j += 1
                j = 0
                i += 1
        if 0 <= (time.time() - self.start_time) < self.delay / 2 and not self.setted1:
            self.set_obstacle()
        elif self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75:
            if not self.setted2:
                self.type = 4
                self.set_obstacle()
        elif (time.time() - self.start_time) > self.delay * 0.75 and self.setted2:
            i = j = 0
            while i < 11:
                while j < 11:
                    if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
                        reset_pos(i, j, self.type)
                    j += 1
                j = 0
                i += 1
            for _ in variables.obstacles_list:
                if _.get_start_time() == self.start_time:
                    variables.obstacles_list.remove(_)

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
            self.setted1 = True
        elif self.type == 4:
            i = j = 0
            while i < 11:
                while j < 11:
                    if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
                        board[i][j].append(self.type)
                    j += 1
                j = 0
                i += 1
            self.setted2 = True


class ObstacleRandomSafe:
    def __init__(self, start_time, delay, array1, array2):
        self.start_time = start_time
        self.delay = delay
        self.type = 3
        self.array1 = array1
        self.array2 = array2
        self.setted1 = self.setted2 = False

    def get_start_time(self):
        return self.start_time

    def update_obstacle(self):
        if self.type == 4:
            reset_pos(5, 5, 3)
            i = 0
            while i < len(self.array1):
                reset_pos(self.array1[i][0], self.array1[i][1], 3)
                i += 1
        if 0 <= (time.time() - self.start_time) < self.delay / 2 and not self.setted1:
            self.set_obstacle()
        elif self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75:
            if not self.setted2:
                self.type = 4
                self.set_obstacle()
        elif (time.time() - self.start_time) > self.delay * 0.75 and self.setted2:
            reset_pos(5, 5, self.type)
            i = 0
            while i < len(self.array1):
                reset_pos(self.array1[i][0], self.array1[i][1], self.type)
                i += 1
            for _ in variables.obstacles_list:
                if _.get_start_time() == self.start_time:
                    variables.obstacles_list.remove(_)
            new_obstacle = ObstacleRandomDanger(time.time(), self.delay, self.array2)
            variables.obstacles_list.append(new_obstacle)

    def set_obstacle(self):
        if self.type == 3:
            board[5][5].append(self.type)
            i = 0
            while i < len(self.array1):
                board[self.array1[i][0]][self.array1[i][1]].append(self.type)
                i += 1
            self.setted1 = True
        elif self.type == 4:
            board[5][5].append(self.type)
            i = 0
            while i < len(self.array1):
                board[self.array1[i][0]][self.array1[i][1]].append(self.type)
                i += 1
            self.setted2 = True


class ObstacleRandomDanger:
    def __init__(self, start_time, delay, array):
        self.start_time = start_time
        self.delay = delay
        self.type = 3
        self.array = array
        self.setted = False

    def get_start_time(self):
        return self.start_time

    def update_obstacle(self):
        if self.delay / 2 <= (time.time() - self.start_time) <= self.delay * 0.75 and not self.setted:
            self.type = 4
            self.set_obstacle()
        elif (time.time() - self.start_time) > self.delay * 0.75 and self.setted:
            reset_pos(5, 5, self.type)
            i = 0
            while i < len(self.array):
                reset_pos(self.array[i][0], self.array[i][1], self.type)
                i += 1
            for _ in variables.obstacles_list:
                if _.get_start_time() == self.start_time:
                    variables.obstacles_list.remove(_)

    def set_obstacle(self):
        if self.type == 4:
            board[5][5].append(self.type)
            i = 0
            while i < len(self.array):
                board[self.array[i][0]][self.array[i][1]].append(self.type)
                i += 1
            self.setted = True


class ObstacleHoming:
    def __init__(self, start_time, delay, pos):
        self.start_time = start_time
        self.delay = delay
        self.type = 4
        self.p_row = pos[0]
        self.p_col = pos[1]
        self.o_row = variables.last_homing_pos[0]
        self.o_col = variables.last_homing_pos[1]
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
            reset_pos(variables.last_homing_pos[0], variables.last_homing_pos[1], 3)
            reset_pos(self.last_pos[0], self.last_pos[1], 4)
            variables.obstacles_homing_list.pop(0)
            variables.homing = False

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
        variables.last_homing_pos[0] = self.get_o_pos()[0]
        variables.last_homing_pos[1] = self.get_o_pos()[1]
