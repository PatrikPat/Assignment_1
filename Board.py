from Piece import *


class Board:
    def __init__(self, field):
        self.field = field # starting setup as 2d array with pieces and 'X'
        self.moves = [[i, j] for i in range(4) for j in range(6)] # define possible moves

    def possible_moves(self, player: str) -> list:
        """Returns of a player ('R' or 'B') the possible moves of that player as 
        a list. Example [[R10, [new_position]], [R2, [new_position]].
        """
        # make list with positions of pieces of the player, because pieces cannot 
        # move towards those places
        player_pieces = []
        for line in self.field:
            for piece in line:
                if piece != 'X':
                    if piece.team == player:
                        player_pieces.append(piece.position)
        
        # check for each piece of a player whether moves are possible and add those
        # moves to the possible_plays list
        possible_plays = []
        for line in self.field:
            for piece in line:
                if piece != 'X':
                    if piece.team == player:
                        if piece.rank != 'F' and piece.rank != 'B': # flag and bomb cannot move
                            # check the three possible moves: up, down and to 
                            # the right ('R') or left ('B') (depending on team)
                            # add to list when move is possible
                            if [piece.position[0] - 1, piece.position[1]] in self.moves and [piece.position[0] - 1, piece.position[1]] not in player_pieces:
                                possible_plays.append([piece, [piece.position[0] - 1, piece.position[1]]])
                            if [piece.position[0] + 1, piece.position[1]] in self.moves and [piece.position[0] + 1, piece.position[1]] not in player_pieces:
                                possible_plays.append([piece, [piece.position[0] + 1, piece.position[1]]])
                            
                            # check move to the rigth when player is red, otherwise to the left
                            if piece.team == 'R':
                                if [piece.position[0], piece.position[1] + 1] in self.moves and [piece.position[0], piece.position[1] + 1] not in player_pieces:
                                    possible_plays.append([piece, [piece.position[0], piece.position[1] + 1]])
                            else:
                                if [piece.position[0], piece.position[1] - 1] in self.moves and [piece.position[0], piece.position[1] - 1] not in player_pieces:
                                    possible_plays.append([piece, [piece.position[0], piece.position[1] - 1]])
        return possible_plays

    def print_board(self) -> None:
        """Prints the board in the way the assignment shows it.
        """
        for i in range(4):
            for piece in self.field[i]:
                if piece != 'X':
                    print(piece.print_piece(), end=' ')
                else:
                    print('X', end=' ')
            print('')


