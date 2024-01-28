import csv
import time

from sys import path
from code.algorithms.simulated_annealing import *

path.append("code/classes")
from state import State


def experiment_annealing_grid_search(case_name: str, state: 'State', time_seconds: int, cooling_scheme: str, temperature: int):
    with open(f"data/annealing/experiment_annealing_grid_search_{case_name}_{cooling_scheme}_{temperature}.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["unique_id",
                         "run_id",
                         "iteration",
                         "score",
                         "p",
                         "T",
                         "Min",
                         "mutated_score",
                         "heur_multiple_connections",
                         "heur_route_maximalisation",
                         "heur_difficult_connections",
                         "heur_non_valid",
                         "sleeper_string",
                         "start",
                         "mutation",
                         "temperature"
                         "cooling scheme"])

        counter = 0
        # experiment with valid start state and light mutations
        sa = Simulated_annealing(state, temperature, 1000, True)
        start = time.time()

        # run grid element for 1/4 of the time
        while time.time() - start < time_seconds / 4:

            # run gives a list with lists of results of each iteration
            csv_list = sa.run(counter, cooling_scheme, True)

            # write iterations to csv
            for iteration_result in csv_list:
                iteration_result.append("valid")
                iteration_result.append("light")
                iteration_result.append(temperature)
                iteration_result.append(cooling_scheme)
                writer.writerow(iteration_result)

            counter += 1
            print(counter)

        sa = Simulated_annealing(state, temperature, 1000, False)
        start = time.time()

        while time.time() - start < time_seconds / 4:
            csv_list = sa.run(counter, cooling_scheme, True)
            for iteration_result in csv_list:
                iteration_result.append("random")
                iteration_result.append("light")
                iteration_result.append(temperature)
                iteration_result.append(cooling_scheme)
                writer.writerow(iteration_result)
            counter += 1
            print(counter)

        sa = Simulated_annealing(state, temperature, 1000, True)
        start = time.time()

        while time.time() - start < time_seconds / 4:
            csv_list = sa.run(counter, cooling_scheme, False)
            for iteration_result in csv_list:
                iteration_result.append("valid")
                iteration_result.append("heavy")
                iteration_result.append(temperature)
                iteration_result.append(cooling_scheme)
                writer.writerow(iteration_result)
            counter += 1
            print(counter)

        sa = Simulated_annealing(state, temperature, 1000, False)
        start = time.time()

        while time.time() - start < time_seconds / 4:
            csv_list = sa.run(counter, cooling_scheme, False)
            for iteration_result in csv_list:
                iteration_result.append("random")
                iteration_result.append("heavy")
                iteration_result.append(temperature)
                iteration_result.append(cooling_scheme)
                writer.writerow(iteration_result)
            counter += 1
            print(counter)
    
