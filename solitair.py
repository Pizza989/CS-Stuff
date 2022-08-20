from typing import List

global am_called
am_called = 0

DIMENSION_X = 9
DIMENSION_Y = 9
BOARD = [
    [None, None, None, True, True, True, None, None, None],
    [None, None, None, True, True, True, None, None, None],
    [None, None, None, True, True, True, None, None, None],
    [True, True, True, True, True, True, True, True, True],
    [True, True, True, True, False, True, True, True, True],
    [True, True, True, True, True, True, True, True, True],
    [None, None, None, True, True, True, None, None, None],
    [None, None, None, True, True, True, None, None, None],
    [None, None, None, True, True, True, None, None, None],
]


class Move:
    def __init__(self, start: List[int], end: List[int]):
        self.start = start
        self.between = None
        self.end = end

        # Horizontal move
        if self.start[0] - self.end[0] == 2:
            self.between = [self.start[0] - 1, self.start[1]]
        elif self.start[0] - self.end[0] == - 2:
            self.between = [self.start[0] + 1, self.start[1]]
        # Vertical move
        elif self.start[1] - self.end[1] == 2:
            self.between = [self.start[0], self.start[1] - 1]
        elif self.start[1] - self.end[1] == - 2:
            self.between = [self.start[0], self.start[1] + 1]

    def __eq__(self, other):
        return isinstance(other, self.__class__) and other.start == self.start and other.end == self.end

    def __repr__(self):
        return f"{self.start} -> {self.end}"

    def is_valid(self, board: "Board") -> bool:
        try:
            # Is there a stone and is there none at the end
            if not board[self.start[1]][self.start[0]] is True or not board[self.end[1]][self.end[0]] is False:
                return False

            # Is the move not diagonally
            if not (self.start[0] == self.end[0] or self.start[1] == self.end[1]):
                return False

            # Is there a stone in between and is the move only two steps long
            return board[self.between[1]][self.between[0]] is True

        except IndexError:
            return False


class History(list):
    def __init__(self):
        super().__init__()

    def __getitem__(self, item: int) -> List[Move]:
        return super(History, self).__getitem__(item)

    def __setitem__(self, key: int, value: Move):
        assert isinstance(value, Move)
        super(History, self).__setitem__(key, value)

    def append(self, __object: Move) -> None:
        super().append(__object) if isinstance(__object, Move) else ()


class Board(list):
    def __init__(self):
        super().__init__(BOARD)
        self.history: List[Move] = History()
        self.show = lambda: [print(each) for each in self]

    def __repr__(self):
        s = ""
        for each in self:
            s += str(each)
            s += "\n"
        return s

    @property
    def is_won(self):
        for each in self:
            if True in each:
                return False
        return True

    @property
    def possible_moves(self) -> List[Move]:
        moves = []
        for y in range(DIMENSION_Y):
            for x in range(DIMENSION_X):
                if self[y][x] is True:
                    moves.append(Move([x, y], [x + 2, y]))
                    moves.append(Move([x, y], [x - 2, y]))
                    moves.append(Move([x, y], [x, y + 2]))
                    moves.append(Move([x, y], [x, y - 2]))

        return list(filter(lambda _: _.is_valid(self), moves))

    def move(self, move: Move):
        # Validate
        if move.is_valid(self):
            # Execute
            self[move.start[1]][move.start[0]] = False
            self[move.between[1]][move.between[0]] = False
            self[move.end[1]][move.end[0]] = True
        else:
            return

        # Save
        self.history.append(move)

    def undo(self):
        try:
            self.undo_move(self.history.pop(-1))
        except IndexError:
            return

    def undo_move(self, move):
        try:
            self[move.start[1]][move.start[0]] = True
            self[move.between[1]][move.between[0]] = True
            self[move.end[1]][move.end[0]] = False
        except IndexError:
            return

    def solve(self, lvl=0):
        global am_called
        print(am_called, lvl)
        am_called += 1

        moves = self.possible_moves
        if self.is_won:
            input("Won")
            return
        for i in range(len(moves)):
            self.move(moves[i])
            self.solve(lvl + 1)
            self.undo_move(moves[i])
        return


if __name__ == '__main__':
    b = Board()
    b.solve()
    print(b)
