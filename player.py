from scripts import check_death, update_pos, reset_pos


class Player:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def p_get_pos(self):
        return self.row, self.col

    def p_update_pos(self, row, col):
        reset_pos(self.row, self.col, 1)
        self.row = row
        self.col = col
        if check_death(row, col):
            return True
        else:
            update_pos(row, col, 1)
            return False
