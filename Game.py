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
        while True:
            move = self.move(players[i % 2])
            self.board.field[][] = 'X'

            i += 1

        return victor

while not victory
    move()
    return victor

