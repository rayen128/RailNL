import csv
import time

from sys import path
from code.algorithms.hill_climber import *

path.append("code/classes")
from state import State


def run_single_combination(iteration_start: int, iteration_end: int, state: 'State', hill_climber: 'Hill_climber'):
    for i in range(iteration_start, iteration_end):
        return hill_climber.run()


def experiment_hill_climber_iterations(case_name: str, state: 'State', time_seconds: int):
    with open(f"data/experiment_hill_climber_iterations_{case_name}.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["id",
                         "start",
                         "mutation",
                         "score_list"])

        counter = 0

        # experiment with valid start state and light mutations
        hc = Hill_climber(state)
        start = time.time()
        while time.time() - start < time_seconds / 4:
            csv_list = hc.run()
            writer.writerow([i, "valid", "light", score_list])

        hc = Hill_climber(state, valid_start_state=False)
        for i in range(1000, 2000):
            score_list = hc.run()
            writer.writerow([i, "random", "light", score_list])
