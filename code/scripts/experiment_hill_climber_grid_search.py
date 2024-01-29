import csv
import time

from sys import path
from code.algorithms.hill_climber import *

path.append("code/classes")
from state import State


def list_to_str(score_list):
    score_str = ""
    for index, score in enumerate(score_list):
        score_str += str(score)
        if index < len(score_list) - 1:
            score_str += "~"
    return score_str


def get_csv_row_hc(id: int, state: 'State', start: str, mutation: str, score_str: str):
    return [id,
            state.calculate_score(),
            state.fraction_used_connections,
            state.number_routes,
            state.total_minutes,
            start,
            mutation,
            score_str,
            state.show_sleeper_string()]


def experiment_hill_climber_grid_search(case_name: str, state: 'State', time_seconds: int):
    with open(f"data/hill_climber/experiment_hill_climber_grid_search_{case_name}.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["id",
                         "score",
                         "p",
                         "T",
                         "Min",
                         "start",
                         "mutation",
                         "score_list",
                         "sleeper_string"])

        counter = 0

        # experiment with valid start state and light mutations
        hc = Hill_climber(state)
        start = time.time()

        # run grid element for given amount of seconds
        while time.time() - start < time_seconds:

            # run gives a list with lists of results of each iteration
            score_list = hc.run(1000, counter)

            # write results to csv
            writer.writerow(get_csv_row_hc(counter, hc.current_state,
                            "valid", "light", list_to_str(score_list)))
            counter += 1

        # experiment with random start state and light mutations
        hc = Hill_climber(state, valid_start_state=False)
        start = time.time()

        while time.time() - start < time_seconds:
            score_list = hc.run(1000, counter)
            writer.writerow(get_csv_row_hc(counter, hc.current_state,
                            "valid", "light", list_to_str(score_list)))
            counter += 1

        # experiment with valid start state and heavy mutations
        hc = Hill_climber(state)
        start = time.time()

        while time.time() - start < time_seconds:
            score_list = hc.run(1000, counter, change_light=False)
            writer.writerow(get_csv_row_hc(counter, hc.current_state,
                            "valid", "light", list_to_str(score_list)))
            counter += 1

        # experiment with random start state and heavy mutations
        hc = Hill_climber(state, valid_start_state=False)
        start = time.time()

        while time.time() - start < time_seconds:
            score_list = hc.run(1000, counter, change_light=False)
            writer.writerow(get_csv_row_hc(counter, hc.current_state,
                            "valid", "light", list_to_str(score_list)))
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
                         "mutation"])

        counter = 0

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
                writer.writerow(iteration_result)

            counter += 1

        hcr = Hill_climber_restart(
            state, restart_number, valid_start_state=False)
        start = time.time()

        while time.time() - start < time_seconds / 4:
            csv_list = hcr.run(1000, counter)
            for iteration_result in csv_list:
                iteration_result.append("random")
                iteration_result.append("light")
                writer.writerow(iteration_result)
            counter += 1

        hcr = Hill_climber_restart(state, restart_number)
        start = time.time()

        while time.time() - start < time_seconds / 4:
            csv_list = hcr.run(1000, counter, change_light=False)
            for iteration_result in csv_list:
                iteration_result.append("valid")
                iteration_result.append("heavy")
                writer.writerow(iteration_result)
            counter += 1

        hcr = Hill_climber_restart(
            state, restart_number, valid_start_state=False)
        start = time.time()

        while time.time() - start < time_seconds / 4:
            csv_list = hcr.run(1000, counter, change_light=False)
            for iteration_result in csv_list:
                iteration_result.append("random")
                iteration_result.append("heavy")
                writer.writerow(iteration_result)
            counter += 1
