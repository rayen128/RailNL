import csv
import time

from sys import path
from code.algorithms.hill_climber import *

path.append("code/classes")
from state import State


def get_csv_line(state_line: list, start_state: str, mutation: str, runtime: float):
    state_line.append(start_state)
    state_line.append(mutation)
    state_line.append(runtime)
    return state_line


def experiment_hill_climber_choices(case_name: str, state: 'State'):
    with open(f"data/hillclimber_experiment_choices_data_{case_name}.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["state_id", "algorithm", "score", "fraction_used_connections",
                        "number_routes", "total_minutes", "is_solution", "sleeper_string", "start_state", "mutation", "runtime"])

        # hill_climber with valid start state and light mutations
        hc = Hill_climber(state)
        for i in range(10001):
            start_time = time.time()
            hc.run(100)
            runtime = time.time() - start_time
            csv_row = get_csv_line(hc.current_state.show_csv_line(
                i, "hill_climber_light_valid_start"), "valid", "light", runtime)
            writer.writerow(csv_row)

        # hill_climber with random start state and light mutations
        hc = Hill_climber(state, valid_start_state=False)
        for i in range(10001, 20001):
            start_time = time.time()
            hc.run(1000)
            runtime = time.time() - start_time
            csv_row = get_csv_line(hc.current_state.show_csv_line(
                i, "hill_climber_light_random_start"), "random", "light", runtime)
            writer.writerow(csv_row)

        # hill_climber with valid start state and heavy mutations
        hc = Hill_climber(state)
        for i in range(20001, 30001):
            start_time = time.time()
            hc.run(1000, change_light=False)
            runtime = time.time() - start_time
            csv_row = get_csv_line(hc.current_state.show_csv_line(
                i, "hill_climber_heavy_valid_start"), "valid", "heavy", runtime)
            writer.writerow(csv_row)

        # hill_climber with random start state and heavy mutations
        hc = Hill_climber(state, valid_start_state=False)
        for i in range(30001, 40001):
            start_time = time.time()
            hc.run(1000, change_light=False)
            runtime = time.time() - start_time
            csv_row = get_csv_line(hc.current_state.show_csv_line(
                i, "hill_climber_heavy_random_start"), "random", "heavy", runtime)
            writer.writerow(csv_row)
