from Piece import *


class Board:
    def __init__(self, field):
        self.field = field
        self.moves = [[i, j] for i in range(4) for j in range(6)]

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
                        if piece.rank != 'F' and piece.rank != 'B':
                            if [piece.position[0] - 1, piece.position[1]] in self.moves and [piece.position[0] - 1, piece.position[1]] not in player_pieces:
                                possible_plays.append([piece, [piece.position[0] - 1, piece.position[1]]])
                            if [piece.position[0] + 1, piece.position[1]] in self.moves and [piece.position[0] + 1, piece.position[1]] not in player_pieces:
                                possible_plays.append([piece, [piece.position[0] + 1, piece.position[1]]])
                            if piece.team == 'R':
                                if [piece.position[0], piece.position[1] + 1] in self.moves and [piece.position[0], piece.position[1] + 1] not in player_pieces:
                                    possible_plays.append([piece, [piece.position[0], piece.position[1] + 1]])
                            else:
                                if [piece.position[0], piece.position[1] - 1] in self.moves and [piece.position[0], piece.position[1] - 1] not in player_pieces:
                                    possible_plays.append([piece, [piece.position[0], piece.position[1] - 1]])
        return possible_plays

    def print_board(self):
        for i in range(4):
            for piece in self.field[i]:
                if piece != 'X':
                    print(piece.print_piece(), end=' ')
                else:
                    print('X', end=' ')
            print('')


