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

flag_positions = [[0, 0], [3, 0]]
bomb_positions = [[[0, 1], [1, 0]], [[2, 0], [1, 3]]]
miner_positions = [[0, 0], [1, 0], [2, 0], [3, 0]]
general_maarschalk = [9, 10]
spy_verkenner = [2, 2, 1]
possible_positions = [[i, j] for i in range(4) for j in range(2)]

# for i in range(2): #two possible flag positions
#     flag = flag_positions[i]
#     setup_field[flag[0]][flag[1]] = Piece('R', [flag[0], flag[1]], 'F')
#     possible_positions.remove(flag)
#     bomb_list = bomb_positions[i] #based on the flag, two possible bomb positions
#     for j in range(2):
#         bomb = bomb_list[j]
#         setup_field[bomb[0][bomb[1]]] = Piece('R', [bomb[0], bomb[1]], 'B')
#         possible_positions.remove(bomb)
#         for miner in possible_positions and miner[0] == 0:
#             setup_field[miner[0][miner[1]]] = Piece('R', [miner[0], miner[1]], 3)
#            possible_positions.remove(miner)

i = 0 #flag
j = 0 #bomb
z = 0 #miner
y = 0 #general or maarschalk
g = 0 #verkenner, verkenner, or spy
general_placed = False
all_fields = []

while True:
    possible_positions = [[i, j] for i in range(4) for j in range(2)]
    miner_positions = [[0, 0], [1, 0], [2, 0], [3, 0]]
    general_placed = False
    g = 0

    flag = flag_positions[i]
    setup_field[flag[0]][flag[1]] = Piece('R', [flag[0], flag[1]], 'F')
    possible_positions.remove(flag)
    miner_positions.remove(flag)

    bomb_list = bomb_positions[i]  # based on the flag, two possible bomb positions
    bomb = bomb_list[j]
    setup_field[bomb[0]][bomb[1]] = Piece('R', [bomb[0], bomb[1]], 'B')
    possible_positions.remove(bomb)
    if bomb[1] == 0:
        miner_positions.remove(bomb)

    miner = miner_positions[z]
    setup_field[miner[0]][miner[1]] = Piece('R', [miner[0], miner[1]], 3)
    possible_positions.remove(miner)
    
    while True:
        p = possible_positions[0]
        if [p[0] + 2, p[1]] in possible_positions and p[1] == 1 and not general_placed:
            setup_field[p[0]][p[1]] = Piece('R', [p[0], p[1]], general_maarschalk[y])
            setup_field[p[0] + 2][p[1]] = Piece('R', [p[0] + 2, p[1]], general_maarschalk[y + 1])
            possible_positions.remove([p[0], p[1]])
            possible_positions.remove([p[0] + 2, p[1]])
            general_placed = True
        elif [p[0] - 2, p[1]] in possible_positions and p[1] == 1 and not general_placed:
            setup_field[p[0]][p[1]] = Piece('R', [p[0], p[1]], general_maarschalk[y])
            setup_field[p[0] - 2][p[1]] = Piece('R', [p[0] - 2, p[1]], general_maarschalk[y + 1])
            possible_positions.remove([p[0], p[1]])
            possible_positions.remove([p[0] - 2, p[1]])
            general_placed = True
        else: 
            if [p[0], p[1]] in possible_positions:
                setup_field[p[0]][p[1]] = Piece('R', [p[0], p[1]], spy_verkenner[g])
                possible_positions.remove(p)
                g += 1
        if not possible_positions:
            all_fields.append(setup_field)
            print("")
            Board(all_fields[0]).print_board()
            z += 1
            break
    
    if z == len(miner_positions): 
        z = 0
        j += 1
    if j == 2:
        break



# sim = Simulator(10000)
# #red_prob, blue_prob, draw_prob, average_moves, average_moves_red, average_moves_blue, spies_prob = sim.runSimulation([0, 1])
# #print(red_prob, blue_prob, draw_prob, average_moves, average_moves_red, average_moves_blue, spies_prob)
# results = {}
#
# for i in range(4):
#     print(setup_field)
#     results[(0 + i, 1)] = list(sim.runSimulation([0 + i, 1], setup_field))
#
# print(results)



