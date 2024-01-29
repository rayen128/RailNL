import csv
import time

from sys import path
from code.algorithms.hill_climber import *

path.append("code/classes")
from state import State


def experiment_hill_climber_grid_search(case_name: str, state: 'State', time_seconds: int):
    with open(f"data/hill_climber/experiment_hill_climber_grid_search_{case_name}.csv", "w") as file:
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
                         "mutation"])

        counter = 0
        """
        # experiment with valid start state and light mutations
        hc = Hill_climber(state)
        start = time.time()

        # run grid element for 1/4 of the time
        while time.time() - start < time_seconds / 4:

            # run gives a list with lists of results of each iteration
            csv_list = hc.run(1000, counter)

            # write iterations to csv
            for iteration_result in csv_list:
                iteration_result.append("valid")
                iteration_result.append("light")
                writer.writerow(iteration_result)

            counter += 1
        """

        hc = Hill_climber(state, valid_start_state=False)
        start = time.time()

        while time.time() - start < time_seconds / 2:
            csv_list = hc.run(1000, counter)
            for iteration_result in csv_list:
                iteration_result.append("random")
                iteration_result.append("light")
                writer.writerow(iteration_result)
            counter += 1
        """
        hc = Hill_climber(state)
        start = time.time()

        while time.time() - start < time_seconds / 4:
            csv_list = hc.run(1000, counter, change_light=False)
            for iteration_result in csv_list:
                iteration_result.append("valid")
                iteration_result.append("heavy")
                writer.writerow(iteration_result)
            counter += 1
        """
        hc = Hill_climber(state, valid_start_state=False)
        start = time.time()

        while time.time() - start < time_seconds / 4:
            csv_list = hc.run(1000, counter, change_light=False)
            for iteration_result in csv_list:
                iteration_result.append("random")
                iteration_result.append("heavy")
                writer.writerow(iteration_result)
            counter += 1

def experiment_hill_climber_restart_grid_search(case_name: str, state: 'State', time_seconds: int, restart_number: int):
    with open(f"data/hill_climber_restart/experiment_hill_climber_restart_grid_search_{case_name}.csv", "w") as file:
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
                         "restart"])

        counter = 0
        """
        # experiment with valid start state and light mutations
        hcr = Hill_climber_restart(state, restart_number)
        start = time.time()

        # run grid element for 1/4 of the time
        while time.time() - start < time_seconds / 4:

            # run gives a list with lists of results of each iteration
            csv_list = hcr.run(1000, counter)

            # write iterations to csv
            for iteration_result in csv_list:
                iteration_result.append("valid")
                iteration_result.append("light")
                iteration_result.append(restart_number)
                writer.writerow(iteration_result)

            counter += 1
        """
        hcr = Hill_climber_restart(state, restart_number, valid_start_state=False)
        start = time.time()

        while time.time() - start < time_seconds / 2:
            csv_list = hcr.run(1000, counter)
            for iteration_result in csv_list:
                iteration_result.append("random")
                iteration_result.append("light")
                iteration_result.append(restart_number)
                writer.writerow(iteration_result)
            counter += 1
        """
        hcr = Hill_climber_restart(state, restart_number)
        start = time.time()

        while time.time() - start < time_seconds / 4:
            csv_list = hcr.run(1000, counter, change_light=False)
            for iteration_result in csv_list:
                iteration_result.append("valid")
                iteration_result.append("heavy")
                iteration_result.append(restart_number)
                writer.writerow(iteration_result)
            counter += 1
        """
        hcr = Hill_climber_restart(state, restart_number,  valid_start_state=False)
        start = time.time()

        while time.time() - start < time_seconds / 2:
            csv_list = hcr.run(1000, counter, change_light=False)
            for iteration_result in csv_list:
                iteration_result.append("random")
                iteration_result.append("heavy")
                iteration_result.append(restart_number)
                writer.writerow(iteration_result)
            counter += 1
