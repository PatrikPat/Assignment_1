from Game import *
from Piece import *
from copy import *

class Simulator:
    def __init__(self, nrRuns):
        self.nrRuns = nrRuns

    def runSimulation(self, piece, input_field):
        starting_piece = piece
        red_win = 0
        blue_win = 0
        draw = 0
        total_moves = 0
        total_red_moves = 0
        total_blue_moves = 0
        total_both_spies = 0
        for i in range(self.nrRuns):
            game = Game(deepcopy(input_field))
            result_win, moves, spies = game.play_game(starting_piece)
            total_moves += moves
            total_both_spies += spies
            if result_win == 'R':
                red_win += 1
                total_red_moves += moves
            elif result_win == 'B':
                blue_win += 1
                total_blue_moves += moves
            else:
                draw += 1

        return (red_win / self.nrRuns), (blue_win / self.nrRuns), (draw / self.nrRuns), (total_moves / self.nrRuns), (total_red_moves / red_win), (total_blue_moves / blue_win), (total_both_spies / self.nrRuns)


setup_field = [['X' for i in range(6)] for i in range(4)]
setup_list = []

with open("Initial_setup.txt") as f:
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
            if j[1:] == 'F' or j[1:] == 'B':
                setup_field[i][help_list.index(j)] = Piece(j[0], [i, help_list.index(j)], j[1:])
            else:
                setup_field[i][help_list.index(j)] = Piece(j[0], [i, help_list.index(j)], int(j[1:]))

possible_positions = [[i, j] for i in range(4) for j in range(2)]

for flag in [[0, 0], [3, 0]]: #two possible flag positions
    setup_field[flag[0]][flag[1]] = Piece('R', [flag[0], flag[1]], 'F')
    possible_positions.remove(flag)
    if flag == [0, 0]:
        for bomb in [[0, 1], [1, 0]]: #based on the flag, two possible bomb positions
            setup_field[bomb[0][bomb[1]]] = Piece('R', [bomb[0], bomb[1]], 'B')
            possible_positions.remove(bomb)
            for miner in possible_positions and miner[0] == 0:
                setup_field[miner[0][miner[1]]] = Piece('R', [miner[0], miner[1]])
                possible_positions.remove(miner)

sim = Simulator(10000)
#red_prob, blue_prob, draw_prob, average_moves, average_moves_red, average_moves_blue, spies_prob = sim.runSimulation([0, 1])
#print(red_prob, blue_prob, draw_prob, average_moves, average_moves_red, average_moves_blue, spies_prob)
results = {}

for i in range(4):
    print(setup_field)
    results[(0 + i, 1)] = list(sim.runSimulation([0 + i, 1], setup_field))

print(results)



