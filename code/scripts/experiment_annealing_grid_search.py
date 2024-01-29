import csv
import time

from sys import path
from code.algorithms.simulated_annealing import *
from .helpers import *

path.append("code/classes")
from state import State


def experiment_annealing_grid_search(case_name: str, state: 'State', time_seconds: int, cooling_scheme: str, temperature: int):
    with open(f"data/annealing/experiment_annealing_grid_search_{case_name}_{cooling_scheme}_{temperature}.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["run_id",
                         "score",
                         "p",
                         "T",
                         "Min",
                         "start",
                         "mutation",
                         "score_list",
                         "sleeper_string"])

        counter = 0

        if case_name != "netherlands":
            # experiment with valid start state and light mutations
            sa = Simulated_annealing(state, temperature, 1000, True)
            start = time.time()

            # run grid element for given amount of time
            while time.time() - start < time_seconds:

                # run gives a list with lists of results of each iteration
                score_list = sa.run(counter, cooling_scheme, True)
                writer.writerow(get_csv_row(
                    counter, sa.current_state, "valid", "light", list_to_str(score_list)))
                print(counter)
                counter += 1

            # experiment with valid start state and heavy mutations
            sa = Simulated_annealing(state, temperature, 1000, True)
            start = time.time()

            while time.time() - start < time_seconds:
                score_list = sa.run(counter, cooling_scheme, False)
                writer.writerow(get_csv_row(
                    counter, sa.current_state, "valid", "heavy", list_to_str(score_list)))
                print(counter)
                counter += 1

        # experiment with random start state and light mutations
        sa = Simulated_annealing(state, temperature, 1000, False)
        start = time.time()

        while time.time() - start < time_seconds:
            score_list = sa.run(counter, cooling_scheme, True)
            writer.writerow(get_csv_row(
                counter, sa.current_state, "random", "light", list_to_str(score_list)))
            print(counter)
            counter += 1

        # experiment with random start state and heavy mutations
        sa = Simulated_annealing(state, temperature, 1000, False)
        start = time.time()

        while time.time() - start < time_seconds:
            score_list = sa.run(counter, cooling_scheme, False)
            writer.writerow(get_csv_row(
                counter, sa.current_state, "random", "heavy", list_to_str(score_list)))
            print(counter)
            counter += 1
