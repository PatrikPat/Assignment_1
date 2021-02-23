from Simulator import *
from Board import *

simV1 = Simulator(2000)

fields_V1 = simV1.BraRoV1(simV1.readFile("Initial_setup.txt"))
winning_fields = []

for field in fields_V1:
    red_prob, blue_prob, draw_prob, average_moves, average_moves_red, average_moves_blue, spies_prob = simV1.runSimulation('Random', field)
    if red_prob[1] > 0.5:  # we defined outperforming as at least having 0.5 winning probability
        print(red_prob, blue_prob)
        winning_fields.append(field)

print("first loop done", len(winning_fields))

sim = Simulator(100000)
for field in winning_fields:
    red_prob, blue_prob, draw_prob, average_moves, average_moves_red, average_moves_blue, spies_prob = sim.runSimulation('Random', field)    
    print("")
    Board(field).print_board()
    print(red_prob, blue_prob, draw_prob, average_moves, average_moves_red, average_moves_blue, spies_prob)
    

#simV2 = Simulator(100000)
#
#fields_V2 = simV2.BraRoV2(simV2.readFile("Initial_setup.txt"))
#
#winning_fields = []

#for field in fields_V2:
#    red_prob, blue_prob, draw_prob, average_moves, average_moves_red, average_moves_blue, spies_prob = simV2.runSimulation('Random', field)
#    if red_prob[1] > 0.5:  # we defined outperforming as at least having 0.5 winning probability
#        print('ya')
#        winning_fields.append(field)
#
