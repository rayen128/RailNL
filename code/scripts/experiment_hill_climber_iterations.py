import csv
import time

from sys import path
from code.algorithms.hill_climber import *

path.append("code/classes")
from state import State


def experiment_hill_climber_iterations(case_name: str, state: 'State'):
    with open(f"data/experiment_hill_climber_iterations_{case_name}.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["id",
                         "start",
                         "mutation",
                         "score_list"])

        # experiment with valid start state and light mutations
        hc = Hill_climber(state)
        for i in range(1000):
            score_list = hc.run()
            writer.writerow([i, "valid", "light", score_list])
