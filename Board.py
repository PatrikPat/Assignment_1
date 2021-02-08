from Piece import *
import Random as random

class Board:
    def __init__(self):
        self.field = [['X' for i in range(6)] for j in range(4)]
        self.pieces = [('F', 1), ('B', 1), (1, 1), (2, 2), (3, 1), (9, 1), (10, 1)]

    def __repr__(self):
        return "Board"

    def __str__(self):
        return "Board"

    def set_board(self):
        random.
        for i in self.pieces[1:]:

        self.field[0, 0] = Piece('R', [0, 0], 10)

    def print_board(self):
        for i in range(4):
            print(self.field[i])


field = Board()
field.print_board()