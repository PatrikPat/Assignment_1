from Piece import *

class Board:
    def __init__(self, file_name):
        self.field = [['X' for i in range(6)] for i in range(4)]
        self.moves = [[i,j] for i in range(4) for j in range(6)]
        setup_list = []

        with open(file_name) as f:
            line = f.readline()
            setup_list.append(line.rstrip('\n'))
            while line:
                line = f.readline()
                if line != '':
                    setup_list.append(line.rstrip('\n'))

        for i in range(4):
            line = setup_list[i]
            help_list = line.split()
            for j in help_list:
                if j != 'X':
                    self.field[i][help_list.index(j)] = Piece(j[0], [i, help_list.index(j)], j[1:])

    def possible_moves(self, player):
        player_pieces = []
        for line in self.field:
            for piece in line:
                if piece != 'X':
                    if piece.team == player:
                        player_pieces.append(piece.position)

        possible_plays = []
        for line in self.field:
            for piece in line:
                if piece != 'X':
                    if piece.team == player:
                        if piece.rank != 'F' or piece.rank != 'B':
                            if [piece.position[0] - 1, piece.position[1]] in self.moves and [piece.position[0] - 1, piece.position[1]] not in player_pieces:
                                possible_plays.append([piece.rank, [piece.position[0] - 1, piece.position[1]]])
                            if [piece.position[0] + 1, piece.position[1]] in self.moves and [piece.position[0] + 1, piece.position[1]] not in player_pieces:
                                possible_plays.append([piece.rank, [piece.position[0] + 1, piece.position[1]]])
                            if [piece.position[0], piece.position[1] + 1] in self.moves and [piece.position[0], piece.position[1] + 1] not in player_pieces:
                                possible_plays.append([piece.rank, [piece.position[0], piece.position[1] + 1]])
        return possible_plays

    def print_board(self):
        for i in range(4):
            for piece in self.field[i]:
                if piece != 'X':
                    print(piece.print_piece(), end=' ')
                else:
                    print('X', end=' ')
            print('')


field = Board("Initial_setup.txt")
# possible_plays = {}
# for lin in field.field:
#     for piece in lin:
#         if piece != 'X':
#             if piece.team == 'R':
#                 if piece.rank != 'F' or piece.rank != 'B':
#                     possible_plays[piece] = []
#                     if [piece.position[0] - 1, piece.position[0]] in field.moves:
#                         print('ya')
#                         possible_plays.get(piece).append(piece.position[0] - 1)
#                     if piece.position[0] + 1 in field.moves:
#                         possible_plays.get(piece).append(piece.position[0] + 1)
#                     if piece.position[1] + 1 in field.moves:
#                         possible_plays.get(piece).append(piece.position[1] + 1)
#
# print(possible_plays)
print(field.possible_moves('R'))