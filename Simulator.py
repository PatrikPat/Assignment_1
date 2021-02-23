from Game import *
from Piece import *
from copy import *
import random as rd
import numpy as np
import math as math

class Simulator:
    def __init__(self, nrRuns):
        self.nrRuns = nrRuns
        
    def readFile(self, filename: str) -> [[]]:  
        """Returns the setup from a txt file in the form of a double list.
        """
        # initialize a field and an empty list
        setup_field = [['X' for i in range(6)] for i in range(4)]
        setup_list = []
        
        # open file and read the lines
        with open(filename) as f:
            line = f.readline()
            setup_list.append(line.rstrip('\n'))
            while line:
                line = f.readline()
                if line != '':
                    setup_list.append(line.rstrip('\n'))
        
        # get team, position and pieces from the lines and create pieces on the right square
        for i in range(4):
            line = setup_list[i]
            help_list = line.split()
            for j in help_list:
                if j != 'X':
                    # check wheter rank is a str, otherwise make it an int (for comparing purposes)
                    if j[1:] == 'F' or j[1:] == 'B':
                        setup_field[i][help_list.index(j)] = Piece(j[0], [i, help_list.index(j)], j[1:])
                    else:
                        setup_field[i][help_list.index(j)] = Piece(j[0], [i, help_list.index(j)], int(j[1:]))
    
        return setup_field
    
    def confidenceCalculator(self, vector: list) -> list:
        """Calculates the 95% confidence interval of a certain vector based
        on the number of runs of the simulator object and returns a list as [lb, value, ub]. 
        """
        value = np.mean(vector)
        deviation = np.std(vector)
        half_width = 1.96 * (deviation / math.sqrt(self.nrRuns))
        
        return [value - half_width, value, value + half_width]
        
    def runSimulation(self, piece, input_field):
        """Runs a game based on an initial setup and input piece (position of 
        the piece that has to start) or 'Random' if it does not matter. Returns for 
        each variable of interest the 95% confidence interval. 
         """
        # intialize the starting piece and empty lists
        starting_piece = piece
        red_win = []
        blue_win = []
        draw = []
        total_moves = []
        total_red_moves = []
        total_blue_moves = []
        total_both_spies = []
        
        # run the game nrRuns times
        for i in range(self.nrRuns):
            game = Game(deepcopy(input_field)) # deepcopy so input_field remains unchanged
            
            # run the game and save the results
            result_win, moves, spies = game.play_game(starting_piece)
            total_moves.append(moves)
            total_both_spies.append(spies)
            if result_win == 'R':
                red_win.append(1)
                blue_win.append(0)
                draw.append(0)
                total_red_moves.append(moves)
            elif result_win == 'B':
                blue_win.append(1)
                red_win.append(0)
                draw.append(0)
                total_blue_moves.append(moves)
            else:
                draw.append(1)
                red_win.append(0)
                blue_win.append(0)
        
        return self.confidenceCalculator(red_win), self.confidenceCalculator(blue_win), self.confidenceCalculator(draw), self.confidenceCalculator(total_moves), self.confidenceCalculator(total_red_moves), self.confidenceCalculator(total_blue_moves), self.confidenceCalculator(total_both_spies)

    def BraRoV1(self, field) -> list:
        """Run the first version of the BraRo heuristic where different combinations
        of logical start positions are tested. Returns a list of fields.
        """
        # initialize variables
        setup_field = field
        i = 0 #flag
        j = 0 #bomb
        z = 0 #miner
        a = 0 #general/maarschalk combinations
        y = 0 #general or maarschalk
        g = 0 #scout, scout, or spy
        b = 0 #which scout/spy combination
        flag_positions = [[0, 0], [3, 0]]
        bomb_positions = [[[0, 1], [1, 0]], [[2, 0], [3, 1]]]
        general_maarschalk = [9, 10]
        spy_verkenner = [[2, 2, 1], [2, 1, 2], [1, 2, 2]]
        all_fieldsV1 = []        
        
        while True:
            # initialize variables at start of loop
            possible_positions = [[i, j] for i in range(4) for j in range(2)]
            miner_positions = [[0, 0], [1, 0], [2, 0], [3, 0]]
            # make possible general/marshall combinations, e.g. [0, 1] and [3, 1]
            general_maarschalk_positions = []
            for l in range(4):
                if l + 2 < 4:
                    general_maarschalk_positions.append([[l, 1], [l + 2, 1]])
                if l + 3 < 4:
                    general_maarschalk_positions.append([[l, 1], [l + 3, 1]])
            g = 0
            
            # set flag for this iteration
            flag = flag_positions[i]
            setup_field[flag[0]][flag[1]] = Piece('R', [flag[0], flag[1]], 'F')
            possible_positions.remove(flag)
            miner_positions.remove(flag)
        
            # set bomb for this iteration and remove possible positions
            bomb_list = bomb_positions[i]  # based on the flag, two possible bomb positions
            bomb = bomb_list[j]
            setup_field[bomb[0]][bomb[1]] = Piece('R', [bomb[0], bomb[1]], 'B')
            possible_positions.remove(bomb)
            if bomb[1] == 0:
                miner_positions.remove(bomb)
            if bomb[0] == 0:
                general_maarschalk_positions.remove([[0, 1], [2, 1]])
                general_maarschalk_positions.remove([[0, 1], [3, 1]])
            if bomb[0] == 3:
                general_maarschalk_positions.remove([[0, 1], [3, 1]])
                general_maarschalk_positions.remove([[1, 1], [3, 1]])
            
            # set miner
            miner = miner_positions[z]
            setup_field[miner[0]][miner[1]] = Piece('R', [miner[0], miner[1]], 3)
            possible_positions.remove(miner)
            
            # set general and marshall as defined in the heuristic
            general_and_maarschalk = general_maarschalk_positions[a]
            p = general_and_maarschalk[0]
            p2 = general_and_maarschalk[1]
            setup_field[p[0]][p[1]] = Piece('R', [p[0], p[1]], general_maarschalk[y % 2])
            setup_field[p2[0]][p2[1]] = Piece('R', [p2[0], p2[1]], general_maarschalk[(y + 1) % 2])
            possible_positions.remove(p)
            possible_positions.remove(p2)
            
            # fill the empty spots with every possible combination of what is left
            while True:
                spy = spy_verkenner[b]
                p = possible_positions[0]
                setup_field[p[0]][p[1]] = Piece('R', [p[0], p[1]], spy[g])
                possible_positions.remove(p)
                g += 1
                if not possible_positions:
                    # add this one field
                    all_fieldsV1.append(deepcopy(setup_field))
                    b += 1 # b + 1 so next scout/spy combination is filled
                    break
            
            # if all scout combinations checked for this setup, move to changing the marshall and general around (y)
            if b == 3:
                b = 0
                y += 1
            
            if y == 2: #general and maarschalk are changed, so change their positions
                y = 0
                a += 1
            
            if a == len(general_maarschalk_positions): # all positions of general and marshall are checked, change miner
                a = 0
                z += 1
                
            if z == len(miner_positions):  # miner is checked, go to next bomb iteration
                z = 0
                j += 1
                
            if i == 1 and j == 2: #all combinations are done
                break
            
            if j == 2: #go to next flag iteration
                j = 0
                i = 1
        
        return all_fieldsV1
    
    def BraRoV2(self, field) -> list:
        """Run the second version of the BraRo heuristic where the flag, bomb,
        marshall and general are predefined, the spy differs between two positions
        and the other pieces are placed at random. Returns list of fields. 
        """
        # initialize variables
        setup_field = field 
        spy_options = [[2, 0], [2, 1]]
        scout_miner = [[2, 2, 3], [2, 3, 2], [3, 2, 2]]
        all_fieldsV2 = []
        a = 0
        while True:
            g = 0
            possible_positions = [[i, j] for i in range(4) for j in range(2)] # check which positions are empty
            
            # hardcode the different predefined pieces
            setup_field[0][0] = Piece('R', [0, 0], 'F')
            setup_field[0][1] = Piece('R', [0, 1], 'B')
            setup_field[3][0] = Piece('R', [3, 0], 9)
            setup_field[3][1] = Piece('R', [3, 1], 10)
            
            # remove placed positions from possible positions
            possible_positions.remove([0, 0])
            possible_positions.remove([0, 1])
            possible_positions.remove([3, 0])
            possible_positions.remove([3, 1])
            
            # make different fields with spy on either position
            spy_position = spy_options[a]
            setup_field[spy_position[0]][spy_position[1]] = Piece('R', spy_position, 1)
            possible_positions.remove(spy_position)
            
            # fill the empty spaces with the pieces that are lef
            while True:
                for p in range(len(possible_positions)):
                    # g here is used to ensure that all combinations are made
                    scout = scout_miner[g]
                    setup_field[possible_positions[p][0]][possible_positions[p][1]] = Piece('R', possible_positions[p], scout[p])
                    if p == len(possible_positions) - 1:
                        all_fieldsV2.append(deepcopy(setup_field))
                g += 1
                
                # all scout/miner combinations made
                if g == 3:
                    break
            
            # all possible fields made
            if a == 1:
                a = 0
                break
            a += 1
        
        return all_fieldsV2
        
#ranks = ['B', 2, 2, 1, 10, 9, 3]


#for i in range(1000):
#    possible_positions = [[i, j] for i in range(4) for j in range(2)] 
#    flag_position = [rd.randint(0, 3), 0]
#    setup_field[flag_position[0]][flag_position[1]] = Piece('R', [flag_position[0], flag_position[1]], 'F')
#    possible_positions.remove(flag_position)
#    for rank in ranks:
#        p = rd.choice(possible_positions)
#        setup_field[p[0]][p[1]] = Piece('R', [p[0], p[1]], rank)
#        possible_positions.remove(p)
#    print(i)
#    red_prob, blue_prob, draw_prob, average_moves, average_moves_red, average_moves_blue, spies_prob = sim.runSimulation('Random', setup_field)
#    if red_prob > 0.5:
#        Board(setup_field).print_board()
#        winning_fields.append(setup_field)


#setup_field[0][0] = Piece('R', [0, 0], 'F')
#setup_field[0][1] = Piece('R', [0, 1], 'B')
#setup_field[1][0] = Piece('R', [1, 0], 3)
#setup_field[1][1] = Piece('R', [1, 1], 2)
#setup_field[2][0] = Piece('R', [2, 0], 2)
#setup_field[2][1] = Piece('R', [2, 1], 1)
#setup_field[3][0] = Piece('R', [3, 0], 9)
#setup_field[3][1] = Piece('R', [3, 1], 10)
#Board(setup_field).print_board()
#r = 0
#sim = Simulator(10000)
#field = sim.readFile("Initial_setup.txt")
##for field in ya:
#red_prob, blue_prob, draw_prob, average_moves, average_moves_red, average_moves_blue, spies_prob = sim.runSimulation('Random', field)
#print(red_prob, blue_prob, draw_prob, average_moves, average_moves_red, average_moves_blue, spies_prob)


# results = {}
#
# for i in range(4):
#     print(setup_field)
#     results[(0 + i, 1)] = list(sim.runSimulation([0 + i, 1], setup_field))
#
# print(results)



