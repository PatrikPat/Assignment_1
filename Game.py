from Piece import *
from Board import *
import random as random


class Game:
    def __init__(self, filename):
        self.board = Board(filename)

    def move(self, player):
        moves = self.board.possible_moves(player)
        move = random.choice(moves)
        return move

    def play_game(self):
        players = ['R', 'B']
        i = 0
        victor = 'Draw'
        while True:
            #self.board.field[0][3] = Piece('B', [0, 3], 10)
            #self.board.field[0][2] = Piece('R', [0, 2], 1)
            move = self.move(players[i % 2])
            print(move)
            #move = [self.board.field[0][2], [0, 3]]
            moving_piece = move[0]
            self.board.field[moving_piece.position[0]][moving_piece.position[1]] = 'X'
            print(self.board.field[move[1][0]][move[1][1]])
            if self.board.field[move[1][0]][move[1][1]] == 'X':
                self.board.field[move[1][0]][move[1][1]] = moving_piece
                moving_piece.position = move[1]
            else:
                result = moving_piece.compare_pieces(self.board.field[move[1][0]][move[1][1]])
                print(result)
                if type(result) == list:
                    result[0].position = 'Removed'
                    result[1].position = 'Removed'
                    self.board.field[move[1][0]][move[1][1]] = 'X'
                else:
                    if result == 'Victory':
                        victor = players[i % 2]
                        break
                    else:
                        if result == 'Enemy':
                            print("moving piece loses")
                            moving_piece.position = 'Removed'
                        else:
                            print("standing piece loses")
                            moving_piece.position = move[1]
                            self.board.field[move[1][0]][move[1][1]].position = 'Removed'
                            self.board.field[move[1][0]][move[1][1]] = moving_piece
            i += 1
            if i == 50:
                break
            self.board.print_board()
            print('')

        return victor


game = Game("Initial_setup.txt")
game.play_game()
