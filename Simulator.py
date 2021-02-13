from Game import *

class Simulator:
    def __init__(self, nrRuns, filename):
        self.nrRuns = nrRuns
        self.filename = filename

    def runSimulation(self):
        red_win = 0
        blue_win = 0
        draw = 0
        total_moves = 0
        total_red_moves = 0
        total_blue_moves = 0
        total_both_spies = 0
        for i in range(self.nrRuns):
            game = Game(self.filename)
            result_win, moves, spies = game.play_game()
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

sim = Simulator(10000, "Initial_setup.txt")
red_prob, blue_prob, draw_prob, average_moves, average_moves_red, average_moves_blue, spies_prob = sim.runSimulation()
print(red_prob, blue_prob, draw_prob, average_moves, average_moves_red, average_moves_blue, spies_prob)



