import csv
import time

from sys import path
from code.algorithms.hill_climber import *
from .helpers import *

path.append("code/classes")
from state import State


def experiment_hill_climber_grid_search(case_name: str, state: 'State', time_seconds: int):
    with open(f"data/hill_climber/experiment_hill_climber_grid_search_{case_name}.csv", "w") as file:
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
            hc = Hill_climber(state)
            start = time.time()

            # run grid element for given amount of seconds
            while time.time() - start < time_seconds:

                # run gives a list with lists of results of each iteration
                score_list = hc.run(1000, counter)

                # write results to csv
                writer.writerow(get_csv_row(counter, hc.current_state,
                                "valid", "light", list_to_str(score_list)))
                print(counter)
                counter += 1

            # experiment with valid start state and heavy mutations
            hc = Hill_climber(state)
            start = time.time()

            while time.time() - start < time_seconds:
                score_list = hc.run(1000, counter, change_light=False)
                writer.writerow(get_csv_row(counter, hc.current_state,
                                "valid", "heavy", list_to_str(score_list)))
                print(counter)
                counter += 1

        # experiment with random start state and light mutations
        hc = Hill_climber(state, valid_start_state=False)
        start = time.time()

        while time.time() - start < time_seconds:
            score_list = hc.run(1000, counter)
            writer.writerow(get_csv_row(counter, hc.current_state,
                            "random", "light", list_to_str(score_list)))
            print(counter)
            counter += 1

        # experiment with random start state and heavy mutations
        hc = Hill_climber(state, valid_start_state=False)
        start = time.time()

        while time.time() - start < time_seconds:
            score_list = hc.run(1000, counter, change_light=False)
            writer.writerow(get_csv_row(counter, hc.current_state,
                            "random", "heavy", list_to_str(score_list)))
            print(counter)
            counter += 1


def experiment_hill_climber_restart_grid_search(case_name: str, state: 'State', time_seconds: int, restart_number: int):
    with open(f"data/hill_climber_restart/experiment_hill_climber_restart_grid_search_{case_name}.csv", "w") as file:
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

        if case_name != 'netherlands':
            # experiment with valid start state and light mutations
            hcr = Hill_climber_restart(state, restart_number)
            start = time.time()

            # run grid element for 1/4 of the time
            while time.time() - start < time_seconds:

                # run gives a list with lists of results of each iteration
                best_score, best_state, score_list = hcr.run(
                    1000, counter)

                # write iterations to csv
                writer.writerow(get_csv_row(
                    counter, best_state, "valid", "light", list_to_str(score_list), best_score=best_score))

                print(counter)
                counter += 1

            # experiment with valid start start state and heavy mutations
            hcr = Hill_climber_restart(state, restart_number)
            start = time.time()

            while time.time() - start < time_seconds:
                best_score, best_state, score_list = hcr.run(
                    1000, counter, change_light=False)
                writer.writerow(get_csv_row(
                    counter, best_state, "valid", "heavy", list_to_str(score_list), best_score=best_score))

                print(counter)
                counter += 1

        # experiment with random start state and light mutations
        hcr = Hill_climber_restart(
            state, restart_number, valid_start_state=False)
        start = time.time()

        while time.time() - start < time_seconds:
            best_score, best_state, score_list = hcr.run(1000, counter)
            writer.writerow(get_csv_row(
                counter, best_state, "random", "light", list_to_str(score_list), best_score=best_score))

            print(counter)
            counter += 1

        # experiment with random start start state and heavy mutations
        hcr = Hill_climber_restart(
            state, restart_number, valid_start_state=False)
        start = time.time()

        while time.time() - start < time_seconds:
            best_score, best_state, score_list = hcr.run(
                1000, counter, change_light=False)
            writer.writerow(get_csv_row(
                counter, best_state, "random", "heavy", list_to_str(score_list), best_score=best_score))

            print(counter)
            counter += 1
