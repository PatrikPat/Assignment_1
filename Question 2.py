from Simulator import *
from Board import *
import time
start_time = time.time()

sim = Simulator(100000)

field = sim.readFile("Initial_setup.txt")


for i in range(4):
    print("Start position", [0 + i, 1])
    red_prob, blue_prob, draw_prob, average_moves, average_moves_red, average_moves_blue, spies_prob = sim.runSimulation([0 + i, 1], field)

    print("Probability that red wins: %s." % round(red_prob[1], 4), "Confidence interval: %s - %s." % (round(red_prob[0], 4), round(red_prob[2], 4))) 
    print("Probability that blue wins: %s." % round(blue_prob[1], 4), "Confidence interval: %s - %s." % (round(blue_prob[0], 4), round(blue_prob[2], 4))) 
    print("Probability of a draw: %s." % round(draw_prob[1], 4), "Confidence interval: %s - %s." % (round(draw_prob[0], 4), round(draw_prob[2], 4))) 
    print("Average moves: %s." % round(average_moves[1], 4), "Confidence interval: %s - %s." % (round(average_moves[0], 4), round(average_moves[2], 4))) 
    print("Average moves given red wins: %s." % round(average_moves_red[1], 4), "Confidence interval: %s - %s." % (round(average_moves_red[0], 4), round(average_moves_red[2], 4))) 
    print("Average moves given blue wins: %s." % round(average_moves_blue[1], 4), "Confidence interval: %s - %s." % (round(average_moves_blue[0], 4), round(average_moves_blue[2], 4))) 
    print("Probability that both spies live: %s." % round(spies_prob[1], 4), "Confidence interval: %s - %s." % (round(spies_prob[0], 3), round(spies_prob[2], 4))) 
    print("")
    
print("--- %s seconds ---" % (time.time() - start_time))