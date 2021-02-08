from Piece import *

class Board:
    def __init__(self, file_name):
        self.field = [['X' for i in range(6)] for i in range(4)]
        setup_list = []

        with open(file_name) as f:
            line = f.readline()
            setup_list.append(line.rstrip('\n'))
            while line:
                line = f.readline()
                if line != '':
                    setup_list.append(line.rstrip('\n'))

        random_list = []
        for i in range(4):
            line = setup_list[i]
            help_list = line.split()
            for j in help_list:
                if j != 'X':
                    self.field[i][help_list.index(j)] = Piece(j[0], [i, help_list.index(j)], j[1:])

    def print_board(self):
        for i in range(4):
            for piece in self.field[i]:
                if piece != 'X':
                    print(piece.print_piece(), end=' ')
                else:
                    print('X', end=' ')
            print('')


field = Board("Initial_setup.txt")
print(field)