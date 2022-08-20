import random

import numpy as np

BOARD = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


class Board(list):
    def __init__(self, difficulty):
        super().__init__(BOARD)
        self.difficulty = difficulty

    def __repr__(self):
        s = ""
        for each in self:
            s += str(each)
            s += "\n"
        return s

    def is_valid(self, row, col, num):
        valid = True

        for x in range(9):
            if self[x][col] == num:
                valid = False
        for y in range(9):
            if self[row][y] == num:
                valid = False

        row_sec = row // 3
        col_sec = col // 3
        for x in range(3):
            for y in range(3):
                if self[row_sec * 3 + x][col_sec * 3 + y] == num:
                    valid = False
        return valid

    def populate(self):
        remaining = self.difficulty - len(list(filter(lambda x: x != 0, self)))
        if remaining >= self.difficulty:  # Temporary difficulty
            return

        i = 1
        while i <= 9:
            coords = [random.randint(0, 8) for i in range(2)]
            for j in range(1, 10):
                if self.is_valid(coords[0], coords[1], j):
                    self[coords[0]][coords[1]] = j
                    break

            i += 1

    def solve(self):
        for x in range(9):
            for y in range(9):
                if self[y][x] == 0:
                    for i in range(1, 10):
                        if self.is_valid(y, x, i):
                            self[y][x] = i
                            self.solve()
                            self[y][x] = 0
                    return


if __name__ == '__main__':
    b = Board(80)
    b.populate()
    print(b)
    b.solve()
