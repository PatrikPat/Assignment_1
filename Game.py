from Board import *
import random as random


class Game:
    def __init__(self, field):
        self.board = Board(field)

    def move(self, player):
        """Calls the possible moves for the player ('R' or 'B') and choses a random
        move.
        """
        moves = self.board.possible_moves(player)
        move = random.choice(moves)
        return move

    def play_game(self, position: [int, int]):
        """Functionality that actually runs the game. A position can be given,
        which is the starting piece. 'Random' gives a random starting piece. Function
        returns who won (either 'R', 'B' or 'draw'), the amount of moves and whether
        both spies are still in the game.
        """
        # initialize needed variables
        players = ['R', 'B']
        i = 0
        victor = 'Draw'
        draw = []
        
        # move the first piece if it is not random
        if position != 'Random':
            move = [self.board.field[position[0]][position[1]], [position[0], position[1] + 1]]
            moving_piece = move[0]
            self.board.field[moving_piece.position[0]][moving_piece.position[1]] = 'X'

            if self.board.field[move[1][0]][move[1][1]] == 'X':
                self.board.field[move[1][0]][move[1][1]] = moving_piece
                moving_piece.position = move[1]
            i += 1

        while True:
            # try whether a move is possible. If not, add player to the draw and
            # stop when both players cannot move anymore
            try:
                move = self.move(players[i % 2])
            except:
                draw.append(players[i % 2])
                if players[0] in draw and players[1] in draw:
                    break
                i += 1
                continue
              
            # get move and replace old position with 'X'
            moving_piece = move[0]
            self.board.field[moving_piece.position[0]][moving_piece.position[1]] = 'X'
            
            # move piece if there is an 'X' in front of it
            if self.board.field[move[1][0]][move[1][1]] == 'X':
                self.board.field[move[1][0]][move[1][1]] = moving_piece
                moving_piece.position = move[1]
            
            # otherwise, there is an enemy in front and you compare pieces
            else:
                result = moving_piece.compare_pieces(self.board.field[move[1][0]][move[1][1]])
                
                # check for the four different outcomes
                # remove both pieces when it's a draw
                if type(result) == list:
                    result[0].position = 'Removed'
                    result[1].position = 'Removed'
                    self.board.field[move[1][0]][move[1][1]] = 'X'
                
                # if flag is captured, result == victory and stop loop
                else:
                    if result == 'Victory':
                        victor = players[i % 2]
                        break
                    # otherwise either player or enemy has to be removed
                    else:
                        if result == 'Enemy':
                            moving_piece.position = 'Removed'
                        else:
                            moving_piece.position = move[1]
                            self.board.field[move[1][0]][move[1][1]].position = 'Removed'
                            self.board.field[move[1][0]][move[1][1]] = moving_piece
            i += 1
        
        # at the end, count whether both spies are still there
        spies = 0
        both_spies = False
        for z in range(4):
            for j in range(6):
                if self.board.field[z][j] != 'X':
                    if self.board.field[z][j].rank == 1:
                        spies += 1
        
        # return true if both spies are on the field
        if spies == 2:
            both_spies = True

        return victor, i+1, both_spies


