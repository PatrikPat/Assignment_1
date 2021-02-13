
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
        draw = []
        while True:
            try:
                move = self.move(players[i % 2])
            except:
                draw.append(players[i % 2])
                if players[0] in draw and players[1] in draw:
                    break
                i += 1
                continue
                
            moving_piece = move[0]
            self.board.field[moving_piece.position[0]][moving_piece.position[1]] = 'X'
            
            if self.board.field[move[1][0]][move[1][1]] == 'X':
                self.board.field[move[1][0]][move[1][1]] = moving_piece
                moving_piece.position = move[1]
                
            else:
                result = moving_piece.compare_pieces(self.board.field[move[1][0]][move[1][1]])
                
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
                            moving_piece.position = 'Removed'
                        else:
                            moving_piece.position = move[1]
                            self.board.field[move[1][0]][move[1][1]].position = 'Removed'
                            self.board.field[move[1][0]][move[1][1]] = moving_piece
            i += 1

        spies = 0
        both_spies = False
        for z in range(4):
            for j in range(6):
                if self.board.field[z][j] != 'X':
                    if self.board.field[z][j].rank == 1:
                        spies += 1

        if spies == 2:
            both_spies = True

        return victor, i+1, both_spies


